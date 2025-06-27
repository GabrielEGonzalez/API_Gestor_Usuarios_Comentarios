from .. import models,schemas,crud,database
from fastapi import APIRouter , Depends,Path
from app.crud.comment import obtenerComment,getCommentPOST,createComment,updateComment,deleteComment
from app.schemas.comment import Comentario
from typing import Annotated
from sqlalchemy.orm import Session

comentario = APIRouter(prefix="/comentarios")

@comentario.get('')
async def getcomment(db:Session=Depends(database.get_db)):
    coment = obtenerComment(db)
    return coment

@comentario.get('/por_post/{post}')
async def getPostID(post:int=Path(gt=0),db:Session=Depends(database.get_db)):
    getpost = getPostID(db,post)
    return getpost

@comentario.post('')
async def createComment(comentario:Comentario,db:Session=Depends(database.get_db)):
    
    comment = createComment(db,comentario)
    return comment

@comentario.put('/{id}')
async def updateComment():
    return

@comentario.delete('/{id}')
async def deleteComment(db:Session=Depends(database.get_db),id:int=Path(...,gt=0)):
    mensaje = deleteComment(db,id)
    return mensaje