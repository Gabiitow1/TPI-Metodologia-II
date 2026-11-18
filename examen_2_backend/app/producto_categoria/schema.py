from pydantic import BaseModel


class ProductoCategoriaCreate(BaseModel):

    producto_id: int

    categoria_id: int

    es_principal: bool = False


class ProductoCategoriaRead(BaseModel):

    producto_id: int

    categoria_id: int

    es_principal: bool