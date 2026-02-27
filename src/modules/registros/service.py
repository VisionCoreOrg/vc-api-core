from sqlalchemy.orm import Session
from . import repository, schemas

def processar_novo_registro(db: Session, registro_in: schemas.RegistroCreate):
    return repository.criar_registro(db, registro_in)