from fastapi import FastAPI
from pydantic import BaseModel , Field , EmailStr

class Direccion(BaseModel):
    cuidad : str
    pais : str
    zip : str


class Usuario(BaseModel):
    nombre : str
    email: EmailStr
    direccion : Direccion

