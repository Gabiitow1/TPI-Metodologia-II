from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session

from .schema import (
    ProductoCategoriaCreate,
    ProductoCategoriaRead,
)

from . import service


router = APIRouter(
    prefix="/api/v1/productos",
    tags=["Clasificacion"],
)


@router.get(
    "/{producto_id}/categorias",
    response_model=List[ProductoCategoriaRead],
)
def get_categorias_producto(
    producto_id: int,
    session: Session = Depends(get_session),
):
    relaciones = service.get_all(session)

    return [
        relacion
        for relacion in relaciones
        if relacion.producto_id == producto_id
    ]


@router.post(
    "/{producto_id}/categorias",
    response_model=ProductoCategoriaRead,
)
def create_relacion(
    producto_id: int,
    relacion: ProductoCategoriaCreate,
    session: Session = Depends(get_session),
):
    relacion.producto_id = producto_id

    return service.create(
        session,
        relacion
    )