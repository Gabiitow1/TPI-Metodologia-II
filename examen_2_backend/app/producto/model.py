from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Producto(SQLModel, table=True):
    __tablename__ = "productos"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    unidad_venta_id: int = Field(
        foreign_key="unidades_medida.id"
    )

    nombre: str

    descripcion: Optional[str] = None

    precio_base: float = Field(
        ge=0
    )

    stock_cantidad: float = Field(
        default=0,
        ge=0
    )

    disponible: bool = Field(
        default=True
    )

    activo: bool = Field(
        default=True
    )

    anulado_at: Optional[datetime] = None