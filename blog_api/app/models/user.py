# blog_api/app/models/user.py (assuming this is your user model file)

from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class UsuarioModel(Base):
    __tablename__ = "Usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    email = Column(String, unique=True, index=True)
    direccion_id = Column(Integer, ForeignKey("direccion.id"))

    direccion_rel = relationship("direccionModel", back_populates="usuarios")
    comments = relationship("Comment", back_populates="owner")


class direccionModel(Base):
    __tablename__ = "direccion"
    id = Column(Integer, primary_key=True, autoincrement=True) 
    cuidad = Column(String) 
    pais = Column(String)
    zip = Column(String)

    usuarios = relationship("UsuarioModel", back_populates="direccion_rel")