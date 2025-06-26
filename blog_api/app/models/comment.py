import datetime
from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from app.database import Base


class CommentStatus(PyEnum):
    VISIBLE = "visible"
    HIDDEN = "oculto"
    DELETED = "eliminado"

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("Usuario.id"))
    post_id = Column(Integer, index=True)
    contenido = Column(String)
    fecha = Column(DateTime, default=datetime.datetime.now)
    estado = Column(SQLEnum(CommentStatus), default=CommentStatus.VISIBLE)

    owner = relationship("UsuarioModel", back_populates="comments")