from fastapi import FastAPI
from src.core.database import engine, Base
from src.modules.registros.router import router as registros_router

# Cria as tabelas no MySQL automaticamente, futuro implementar o Alembic.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="VisionCore API", version="1.0")

# Registra os controllers
app.include_router(registros_router)

@app.get("/")
def root():
    return {"message": "VisionCore API Online"}