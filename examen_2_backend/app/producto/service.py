from datetime import datetime
from typing import Optional

from fastapi import HTTPException
from sqlmodel import Session, select

from app.unidad_medida.model import UnidadMedida
from app.producto_categoria.model import ProductoCategoria

from .model import Producto
from .schema import ProductoCreate


def get_all(
    session: Session,
    skip: int = 0,
    limit: int = 100,
    activo: Optional[bool] = None,
    disponible: Optional[bool] = None,
    categoria_id: Optional[int] = None,
    search: Optional[str] = None,
):

    statement = select(Producto)

    if activo is not None:
        statement = statement.where(
            Producto.activo == activo
        )

    if disponible is not None:
        statement = statement.where(
            Producto.disponible == disponible
        )

    productos = session.exec(statement).all()

    if categoria_id is not None:

        relaciones = session.exec(
            select(ProductoCategoria).where(
                ProductoCategoria.categoria_id
                == categoria_id
            )
        ).all()

        productos_categoria = {
            relacion.producto_id
            for relacion in relaciones
        }

        productos = [
            producto
            for producto in productos
            if producto.id in productos_categoria
        ]

    if search:

        productos = [
            producto
            for producto in productos
            if search.lower()
            in producto.nombre.lower()
        ]

    return productos[skip : skip + limit]


def get_by_id(
    session: Session,
    producto_id: int,
):

    producto = session.get(
        Producto,
        producto_id,
    )

    if not producto:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    return producto


def create(
    session: Session,
    data: ProductoCreate,
):

    unidad = session.get(
        UnidadMedida,
        data.unidad_venta_id,
    )

    if not unidad:
        raise HTTPException(
            status_code=404,
            detail="Unidad de medida no encontrada",
        )

    repetido = session.exec(
        select(Producto).where(
            Producto.nombre == data.nombre,
            Producto.activo == True,
        )
    ).first()

    if repetido:
        raise HTTPException(
            status_code=409,
            detail="Ya existe un producto con ese nombre",
        )

    producto = Producto(
        **data.model_dump()
    )

    session.add(producto)

    session.commit()

    session.refresh(producto)

    return producto


def update(
    session: Session,
    producto_id: int,
    data: ProductoCreate,
):

    producto = session.get(
        Producto,
        producto_id,
    )

    if not producto:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    if not producto.activo:
        raise HTTPException(
            status_code=409,
            detail="El producto está anulado",
        )

    unidad = session.get(
        UnidadMedida,
        data.unidad_venta_id,
    )

    if not unidad:
        raise HTTPException(
            status_code=404,
            detail="Unidad de medida no encontrada",
        )

    repetido = session.exec(
        select(Producto).where(
            Producto.nombre == data.nombre,
            Producto.activo == True,
            Producto.id != producto_id,
        )
    ).first()

    if repetido:
        raise HTTPException(
            status_code=409,
            detail="Ya existe un producto con ese nombre",
        )

    producto.nombre = data.nombre
    producto.descripcion = data.descripcion
    producto.precio_base = data.precio_base
    producto.unidad_venta_id = data.unidad_venta_id
    producto.stock_cantidad = data.stock_cantidad
    producto.disponible = data.disponible

    session.add(producto)

    session.commit()

    session.refresh(producto)

    return producto


def delete(
    session: Session,
    producto_id: int,
):

    producto = session.get(
        Producto,
        producto_id,
    )

    if not producto:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    if not producto.activo:
        raise HTTPException(
            status_code=409,
            detail="El producto ya está anulado",
        )

    producto.activo = False
    producto.anulado_at = datetime.now()

    session.add(producto)

    session.commit()

    return True