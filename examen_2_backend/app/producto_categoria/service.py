from fastapi import HTTPException
from sqlmodel import Session, select

from app.producto.model import Producto
from app.categoria.model import Categoria

from .model import ProductoCategoria
from .schema import ProductoCategoriaCreate


def get_all(session: Session):

    statement = select(ProductoCategoria)

    return session.exec(statement).all()


def create(
    session: Session,
    data: ProductoCategoriaCreate
):

    producto = session.get(
        Producto,
        data.producto_id
    )

    if not producto:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    categoria = session.get(
        Categoria,
        data.categoria_id
    )

    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="Categoría no encontrada"
        )

    if not producto.activo:
        raise HTTPException(
            status_code=409,
            detail="Producto anulado"
        )

    if not categoria.activo:
        raise HTTPException(
            status_code=409,
            detail="Categoría anulada"
        )

    existe = session.exec(
        select(ProductoCategoria).where(
            ProductoCategoria.producto_id == data.producto_id,
            ProductoCategoria.categoria_id == data.categoria_id
        )
    ).first()

    if existe:
        raise HTTPException(
            status_code=409,
            detail="El producto ya pertenece a esa categoría"
        )

    if data.es_principal:

        relaciones = session.exec(
            select(ProductoCategoria).where(
                ProductoCategoria.producto_id
                == data.producto_id
            )
        ).all()

        for relacion in relaciones:
            relacion.es_principal = False
            session.add(relacion)

    nueva_relacion = ProductoCategoria(
        **data.model_dump()
    )

    session.add(nueva_relacion)

    session.commit()

    session.refresh(nueva_relacion)

    return nueva_relacion