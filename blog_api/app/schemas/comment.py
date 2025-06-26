import datetime
from pydantic import BaseModel , Field , EmailStr

class Comentario(BaseModel):
    id:int=Field(...,gt=0)
    usuario_id:int=Field(...,gt=0)
    post_id:int = Field(...,gt=0)
    contenido:str = Field(...,min_length=10,max_length=500)
    fecha: datetime
    estado:str