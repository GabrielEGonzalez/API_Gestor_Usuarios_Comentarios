from fastapi import FastAPI
from pydantic import BaseModel , Field , EmailStr

class Direccion(BaseModel):
    cuidad : str
    pais : str
    zip : str


class Usuario(BaseModel):
    id: int = Field()
    nombre : str = Field()
    email: EmailStr
    direccion : Direccion

