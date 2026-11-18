from typing import Optional

from pydantic import BaseModel, Field


class ProductoBase(BaseModel):

    nombre: str = Field(
        min_length=3,
        max_length=100
    )

    descripcion: Optional[str] = None

    precio_base: float = Field(
        ge=0
    )

    unidad_venta_id: int

    stock_cantidad: float = Field(
        default=0,
        ge=0
    )

    disponible: bool = True


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(ProductoBase):
    pass


class ProductoPublic(BaseModel):

    id: int

    nombre: str

    descripcion: Optional[str] = None

    precio_base: float

    unidad_venta_id: int

    stock_cantidad: float

    disponible: bool

    activo: bool

    hay_stock: bool


class ProductoRead(ProductoPublic):
    pass