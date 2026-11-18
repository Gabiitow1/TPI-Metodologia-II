from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.core.database import get_session
from .model import UnidadMedida

router = APIRouter(
    prefix="/api/v1/unidades-medida",
    tags=["Unidades Medida"]
)


@router.get("/", response_model=list[UnidadMedida])
def get_unidades(
    session: Annotated[Session, Depends(get_session)]
):
    statement = select(UnidadMedida)

    return session.exec(statement).all()