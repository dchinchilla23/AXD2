from pydantic import BaseModel
from datetime import date
from typing import Optional

# Base schema para reutilizar campos
class EntregaBase(BaseModel):
    numero_guia: Optional[int] = None
    ciudad_origen: Optional[str] = None
    ciudad_destino: Optional[str] = None
    direccion_entrega: Optional[str] = None
    nombre_destinatario: Optional[str] = None
    fecha_estimada_entrega: Optional[date] = None
    estado_envio: Optional[str] = None  # Por recoger, En ruta, Entregado, Cancelado

# Para crear una nueva entrega (POST)
class EntregaCreate(EntregaBase):
    numero_guia: int
    ciudad_origen: str
    ciudad_destino: str
    direccion_entrega: str
    nombre_destinatario: str
    fecha_estimada_entrega: date
    estado_envio: str

# Para actualizar campos parcialmente (PUT)
class EntregaUpdate(BaseModel):
    ciudad_origen: Optional[str] = None
    ciudad_destino: Optional[str] = None
    direccion_entrega: Optional[str] = None
    nombre_destinatario: Optional[str] = None
    fecha_estimada_entrega: Optional[date] = None
    estado_envio: Optional[str] = None

# Para respuesta al cliente (GET, POST, PUT)
class EntregaOut(EntregaCreate):
    id: int

    class Config:
        from_attributes = True
