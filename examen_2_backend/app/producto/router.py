from typing import Annotated, List, Optional

from fastapi import (
    APIRouter,
    Depends,
    Path,
    Query,
    status,
)

from sqlmodel import Session

from app.core.database import get_session

from .schema import (
    ProductoCreate,
    ProductoPublic,
)

from . import service


router = APIRouter(
    prefix="/api/v1/productos",
    tags=["Productos"],
)


@router.get(
    "/",
    response_model=List[ProductoPublic],
)
def get_productos(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    activo: Optional[bool] = None,
    disponible: Optional[bool] = None,
    categoria_id: Optional[int] = None,
    search: Optional[str] = None,
    session: Session = Depends(get_session),
):

    productos = service.get_all(
        session=session,
        skip=skip,
        limit=limit,
        activo=activo,
        disponible=disponible,
        categoria_id=categoria_id,
        search=search,
    )

    return [
        ProductoPublic(
            id=producto.id,
            nombre=producto.nombre,
            descripcion=producto.descripcion,
            precio_base=producto.precio_base,
            unidad_venta_id=producto.unidad_venta_id,
            stock_cantidad=producto.stock_cantidad,
            disponible=producto.disponible,
            activo=producto.activo,
            hay_stock=producto.stock_cantidad > 0,
        )
        for producto in productos
    ]


@router.get(
    "/{producto_id}",
    response_model=ProductoPublic,
)
def get_producto(
    producto_id: Annotated[
        int,
        Path(gt=0)
    ],
    session: Session = Depends(get_session),
):

    producto = service.get_by_id(
        session,
        producto_id,
    )

    return ProductoPublic(
        id=producto.id,
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio_base=producto.precio_base,
        unidad_venta_id=producto.unidad_venta_id,
        stock_cantidad=producto.stock_cantidad,
        disponible=producto.disponible,
        activo=producto.activo,
        hay_stock=producto.stock_cantidad > 0,
    )


@router.post(
    "/",
    response_model=ProductoPublic,
    status_code=status.HTTP_201_CREATED,
)
def create_producto(
    producto: ProductoCreate,
    session: Session = Depends(get_session),
):

    nuevo = service.create(
        session,
        producto,
    )

    return ProductoPublic(
        id=nuevo.id,
        nombre=nuevo.nombre,
        descripcion=nuevo.descripcion,
        precio_base=nuevo.precio_base,
        unidad_venta_id=nuevo.unidad_venta_id,
        stock_cantidad=nuevo.stock_cantidad,
        disponible=nuevo.disponible,
        activo=nuevo.activo,
        hay_stock=nuevo.stock_cantidad > 0,
    )


@router.put(
    "/{producto_id}",
    response_model=ProductoPublic,
)
def update_producto(
    producto_id: Annotated[
        int,
        Path(gt=0)
    ],
    producto: ProductoCreate,
    session: Session = Depends(get_session),
):

    actualizado = service.update(
        session,
        producto_id,
        producto,
    )

    return ProductoPublic(
        id=actualizado.id,
        nombre=actualizado.nombre,
        descripcion=actualizado.descripcion,
        precio_base=actualizado.precio_base,
        unidad_venta_id=actualizado.unidad_venta_id,
        stock_cantidad=actualizado.stock_cantidad,
        disponible=actualizado.disponible,
        activo=actualizado.activo,
        hay_stock=actualizado.stock_cantidad > 0,
    )


@router.delete(
    "/{producto_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_producto(
    producto_id: Annotated[
        int,
        Path(gt=0)
    ],
    session: Session = Depends(get_session),
):

    service.delete(
        session,
        producto_id,
    )