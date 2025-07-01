from fastapi import FastAPI
from app.routes import entregas
from app.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Api entregas Axedem",
    description="Sistema de segumiento productos, ultima milla."
)
app.include_router(entregas.router)