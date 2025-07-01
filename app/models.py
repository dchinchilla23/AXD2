from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Entrega(Base):
    __tablename__ = "entregas"
    id = Column(Integer, primary_key=True, index=True)
    numero_guia = Column(String)
    Ciudad_origen = Column(String)
    Ciudad_destino = Column(String)
    Direccion_de_entrega = Column(String)
    Nombre_del_destinatario = Column(String)
    Fecha_estimada_de_entrega = Column(Date)
    Estado_del_envio = Column(String) # Por recoger,En ruta, Entregado, Cancelado
    
    