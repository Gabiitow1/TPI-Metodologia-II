from typing import List, Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from sqlmodel import Session

from app.core.database import get_session

from .schema import (
    CategoriaCreate,
    CategoriaRead,
)

from . import service


router = APIRouter(
    prefix="/api/v1/categorias",
    tags=["Categorias"],
)


@router.get(
    "/",
    response_model=List[CategoriaRead],
)
def get_categorias(
    skip: int = 0,
    limit: int = 100,
    activo: Optional[bool] = None,
    search: Optional[str] = None,
    session: Session = Depends(get_session),
):
    return service.get_all(
        session=session,
        skip=skip,
        limit=limit,
        activo=activo,
        search=search,
    )


@router.get(
    "/{categoria_id}",
    response_model=CategoriaRead,
)
def get_categoria(
    categoria_id: int,
    session: Session = Depends(get_session),
):
    categoria = service.get_by_id(
        session,
        categoria_id,
    )

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria no encontrada",
        )

    return categoria


@router.post(
    "/",
    response_model=CategoriaRead,
    status_code=status.HTTP_201_CREATED,
)
def create_categoria(
    categoria: CategoriaCreate,
    session: Session = Depends(get_session),
):
    return service.create(
        session,
        categoria,
    )


@router.put(
    "/{categoria_id}",
    response_model=CategoriaRead,
)
def update_categoria(
    categoria_id: int,
    categoria: CategoriaCreate,
    session: Session = Depends(get_session),
):
    categoria_actualizada = service.update(
        session,
        categoria_id,
        categoria,
    )

    if not categoria_actualizada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria no encontrada",
        )

    return categoria_actualizada


@router.delete(
    "/{categoria_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_categoria(
    categoria_id: int,
    session: Session = Depends(get_session),
):
    eliminado = service.delete(
        session,
        categoria_id,
    )

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria no encontrada",
        )