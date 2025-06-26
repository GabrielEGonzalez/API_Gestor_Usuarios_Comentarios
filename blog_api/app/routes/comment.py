from .. import models,schemas,crud,database
from fastapi import APIRouter , Depends,Path
from app.schemas.comment import Comentario
from typing import Annotated
from sqlalchemy.orm import Session

comentario = APIRouter(prefix="/comentarios")

@comentario.get('')
async def getcomment(db:Session=Depends(database.get_db)):
    return

@comentario.get('/por_post/{post}')
async def getPostID(post:int=Path(gt=0),db:Session=Depends(database.get_db)):
    return

@comentario.post('')
async def createComment(comentario:Comentario,db:Session=Depends(database.get_db)):
    return

@comentario.put('/{id}')
async def updateComment():
    return

@comentario.delete('/{id}')
async def deleteComment():
    return