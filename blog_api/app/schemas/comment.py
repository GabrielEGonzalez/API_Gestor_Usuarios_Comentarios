import datetime
from pydantic import BaseModel , Field , EmailStr

class ComentarioBase(BaseModel):
    usuario_id: int = Field(..., gt=0)
    post_id: int = Field(..., gt=0)
    contenido: str = Field(..., min_length=10, max_length=500)
    fecha: datetime.datetime
    estado: str

class ComentarioCreate(ComentarioBase):
    pass

class ComentarioResponse(ComentarioBase):
    id: int

    class Config:
        orm_mode = True