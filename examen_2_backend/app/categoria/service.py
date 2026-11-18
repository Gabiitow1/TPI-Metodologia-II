from datetime import datetime
from typing import Optional

from fastapi import HTTPException
from sqlmodel import Session, select

from .model import Categoria
from .schema import CategoriaCreate


def get_all(
    session: Session,
    skip: int = 0,
    limit: int = 100,
    activo: Optional[bool] = None,
    search: Optional[str] = None,
):

    statement = select(Categoria)

    if activo is not None:
        statement = statement.where(
            Categoria.activo == activo
        )

    categorias = session.exec(
        statement
    ).all()

    if search:
        categorias = [
            categoria
            for categoria in categorias
            if search.lower()
            in categoria.nombre.lower()
        ]

    return categorias[skip: skip + limit]


def get_by_id(
    session: Session,
    categoria_id: int
):

    categoria = session.get(
        Categoria,
        categoria_id
    )

    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="Categoría no encontrada"
        )

    return categoria


def create(
    session: Session,
    data: CategoriaCreate
):

    existe = session.exec(
        select(Categoria).where(
            Categoria.nombre == data.nombre,
            Categoria.activo == True
        )
    ).first()

    if existe:
        raise HTTPException(
            status_code=409,
            detail="Ya existe una categoría con ese nombre"
        )

    categoria = Categoria(
        **data.model_dump()
    )

    session.add(categoria)

    session.commit()

    session.refresh(categoria)

    return categoria


def update(
    session: Session,
    categoria_id: int,
    data: CategoriaCreate
):

    categoria = session.get(
        Categoria,
        categoria_id
    )

    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="Categoría no encontrada"
        )

    if not categoria.activo:
        raise HTTPException(
            status_code=409,
            detail="La categoría está anulada"
        )

    repetida = session.exec(
        select(Categoria).where(
            Categoria.nombre == data.nombre,
            Categoria.activo == True,
            Categoria.id != categoria_id
        )
    ).first()

    if repetida:
        raise HTTPException(
            status_code=409,
            detail="Ya existe una categoría con ese nombre"
        )

    categoria.nombre = data.nombre
    categoria.descripcion = data.descripcion

    session.add(categoria)

    session.commit()

    session.refresh(categoria)

    return categoria


def delete(
    session: Session,
    categoria_id: int
):

    categoria = session.get(
        Categoria,
        categoria_id
    )

    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="Categoría no encontrada"
        )

    if not categoria.activo:
        raise HTTPException(
            status_code=409,
            detail="La categoría ya está anulada"
        )

    categoria.activo = False
    categoria.anulado_at = datetime.now()

    session.add(categoria)

    session.commit()

    return True