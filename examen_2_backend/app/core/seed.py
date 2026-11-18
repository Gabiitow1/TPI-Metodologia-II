from sqlmodel import Session, select

from app.core.database import engine
from app.unidad_medida.model import (
    UnidadMedida,
    TipoUnidad
)


def seed_unidades():

    with Session(engine) as session:

        existe = session.exec(
            select(UnidadMedida)
        ).first()

        if existe:
            return

        unidades = [
            UnidadMedida(
                nombre="kilogramo",
                simbolo="kg",
                tipo=TipoUnidad.peso
            ),
            UnidadMedida(
                nombre="gramo",
                simbolo="g",
                tipo=TipoUnidad.peso
            ),
            UnidadMedida(
                nombre="litro",
                simbolo="L",
                tipo=TipoUnidad.volumen
            ),
            UnidadMedida(
                nombre="mililitro",
                simbolo="mL",
                tipo=TipoUnidad.volumen
            ),
            UnidadMedida(
                nombre="pieza",
                simbolo="u",
                tipo=TipoUnidad.contable
            ),
            UnidadMedida(
                nombre="docena",
                simbolo="doc",
                tipo=TipoUnidad.contable
            )
        ]

        session.add_all(unidades)
        session.commit()