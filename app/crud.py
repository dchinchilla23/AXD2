from sqlalchemy.orm import Session
from app import models, schemas
from datetime import date

CIUDADES_CAPACIDAD = {
    "Bogota": 10,
    "Medellin": 5,
    "cali": 7,   
}

def crear_entrega(db: Session, entrega: schemas.EntregaCreate):
    ciudad = entrega.ciudad_destino
    capacidad_max = CIUDADES_CAPACIDAD.get(ciudad,999)
    
    total = db.query(models.Entrega).filter(
        models.Entrega.Ciudad_destino == ciudad,
        models.Entrega.Fecha_estimada_de_entrega == entrega.Fecha_estimada_de_entrega
    ).count()
    
    if total >= capacidad_max:
        raise ValueError(f"La capacidad maxima de {ciudad} es de {capacidad_max}")
      
    db_entrega = models.Entrega(**entrega.dict())
    
    db.add(db_entrega)
    db.commit()
    db.refresh(db_entrega)
    return db_entrega

def obtener_por_guia(db: Session, numero_guia: int):
    return db.query(models.Entrega).filter(models.Entrega.Numero_guia == numero_guia).first()
    