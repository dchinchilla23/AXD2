from pydantic import BaseModel
from datetime import date

class EntregaBase(BaseModel):
    numero_guia : str
    Ciudad_origen : str
    Ciudad_destino : str
    ciudad_destino : str
    Direccion_de_entrega : str
    Nombre_del_destinatario : str
    Fecha_estimada_de_entrega = date
    Estado_del_envio : str # Por recoger,En ruta, Entregado, Cancelado

class EntregaCreate(EntregaBase):
    pass

class Entrega(EntregaBase):
    id : int
    class Config:
        orm_mode = True    