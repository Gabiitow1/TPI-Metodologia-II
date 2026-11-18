from enum import Enum
from typing import Optional

from sqlmodel import SQLModel, Field


class TipoUnidad(str, Enum):
    peso = "peso"
    volumen = "volumen"
    contable = "contable"


class UnidadMedida(SQLModel, table=True):
    __tablename__ = "unidades_medida"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    nombre: str = Field(
        unique=True
    )

    simbolo: str = Field(
        unique=True
    )

    tipo: TipoUnidad