from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, timezone
from src.core.database import Base

class RegistroModel(Base):
    __tablename__ = "registros_placas"

    id = Column(Integer, primary_key=True, index=True)
    camera_id = Column(String(50), index=True)
    arquivo_origem = Column(String(255))
    placa = Column(String(10), index=True)
    confianca = Column(Float)
    imagem_url = Column(String(500))
    data_hora = Column(DateTime, default=lambda: datetime.now(timezone.utc))