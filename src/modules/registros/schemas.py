from pydantic import BaseModel
from datetime import datetime

class RegistroCreate(BaseModel):
    camera_id: str
    arquivo_origem: str
    placa: str
    confianca: float
    imagem_url: str
    data_hora: datetime

class RegistroResponse(RegistroCreate):
    id: int

    class Config:
        from_attributes = True