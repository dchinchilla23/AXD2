import csv
from sqlalchemy.orm import Session
from app import database, models

# Ruta del CSV generado (ajusta si lo moviste)
csv_path = "entregas_simuladas_ok.csv"

# Abrir conexión a la base de datos
db: Session = database.SessionLocal()

# Leer e insertar cada fila del CSV
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        entrega = models.Entrega(
            numero_guia=int(row['numero_guia']),
            ciudad_origen=row['ciudad_origen'],
            ciudad_destino=row['ciudad_destino'],
            direccion_entrega=row['direccion_entrega'],
            nombre_destinatario=row['nombre_destinatario'],
            fecha_estimada_entrega=row['fecha_estimada_entrega'],
            estado_envio=row['estado_envio']
        )
        db.add(entrega)

db.commit()
db.close()

print(" Entregas importadas correctamente sin usar pandas.")
