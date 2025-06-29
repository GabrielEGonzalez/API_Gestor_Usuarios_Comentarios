import datetime
from pydantic import BaseModel , Field
from typing import Optional
from enum import Enum


class CommentStatus(str, Enum):
    VISIBLE = "VISIBLE"
    HIDDEN = "HIDDEN"
    DELETED = "DELETED"

class ComentarioBase(BaseModel):
    usuario_id: int = Field(..., gt=0)
    post_id: int = Field(..., gt=0)
    contenido: str = Field(..., min_length=10, max_length=500)
    fecha: datetime.datetime
    estado: CommentStatus = Field(CommentStatus.VISIBLE)

class ComentarioCreate(ComentarioBase):
    pass

class ComentarioResponse(ComentarioBase):
    id: int

    class Config:
        from_attributes = True