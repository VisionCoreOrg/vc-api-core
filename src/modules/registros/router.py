from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from . import schemas, service, repository

router = APIRouter(prefix="/api/vagas", tags=["Registros de Placas"])

@router.post("/registro", response_model=schemas.RegistroResponse, status_code=201)
def registrar_placa(registro: schemas.RegistroCreate, db: Session = Depends(get_db)):
    return service.processar_novo_registro(db, registro)

@router.get("/registros", response_model=list[schemas.RegistroResponse])
def obter_registros(limit: int = 10, db: Session = Depends(get_db)):
    return repository.listar_registros(db, limit)