from sqlalchemy.orm import Session
from .models import RegistroModel
from .schemas import RegistroCreate

def criar_registro(db: Session, registro: RegistroCreate):
    db_registro = RegistroModel(**registro.model_dump())
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro

def listar_registros(db: Session, limite: int = 10):
    return db.query(RegistroModel).order_by(RegistroModel.data_hora.desc()).limit(limite).all()