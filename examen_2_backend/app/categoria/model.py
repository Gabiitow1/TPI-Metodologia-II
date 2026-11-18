from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Categoria(SQLModel, table=True):
    __tablename__ = "categorias"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    nombre: str

    descripcion: Optional[str] = None

    activo: bool = Field(
        default=True
    )

    anulado_at: Optional[datetime] = None