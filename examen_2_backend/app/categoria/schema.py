from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CategoriaBase(BaseModel):

    nombre: str = Field(
        min_length=3,
        description="Nombre de la categoría"
    )

    descripcion: Optional[str] = None


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(CategoriaBase):
    pass


class CategoriaRead(CategoriaBase):

    id: int

    activo: bool

    anulado_at: Optional[datetime] = None