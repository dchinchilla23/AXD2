from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

# Dependencia para obtener la base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear una entrega
@router.post("/entregas/", response_model=schemas.EntregaOut)
def registrar_entrega(entrega: schemas.EntregaCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_entrega(db, entrega)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Consultar entrega por nuemro de guia
@router.get("/entregas/{numero_guia}", response_model=schemas.EntregaOut)
def get_entrega(numero_guia: int, db: Session = Depends(get_db)):
    entrega = crud.get_entrega_by_guia(db, numero_guia)
    if not entrega:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    return entrega

# Actualizar entrega por nuemro de guia 
@router.put("/entregas/{numero_guia}", response_model=schemas.EntregaOut)
def actualizar_entrega(numero_guia: int, datos_actualizados: schemas.EntregaUpdate, db: Session = Depends(get_db)):
    entrega = crud.get_entrega_by_guia(db, numero_guia)
    if not entrega:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")

    try:
        return crud.update_entrega(db, entrega, datos_actualizados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
