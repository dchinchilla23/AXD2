from sqlalchemy.orm import Session
from app import database, models, schemas, crud

# Crear sesión manual
db: Session = database.SessionLocal()

# Datos de ejemplo
entrega_data = schemas.EntregaCreate(
    numero_guia=12345,
    ciudad_origen="Bogota",
    ciudad_destino="Medellin",
    direccion_entrega="Calle 123 #45-67",
    nombre_destinatario="Juan Pérez",
    fecha_estimada_entrega="2025-07-03",
    estado_envio="Por recoger"
)

try:
    nueva_entrega = crud.crear_entrega(db, entrega_data)
    print(f"Entrega creada con ID: {nueva_entrega.id}")
except Exception as e:
    print("Error:", e)
finally:
    db.close()
