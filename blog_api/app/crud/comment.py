from app.models.comment import Comment
from app.schemas.comment import Comentario
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi import status

def obtenerComment(db:Session):
    
    comentario = db.query(Comment).all()
    return comentario

def getCommentPOST(db:Session,post:int):
    
    listComment = db.query(Comment).filter(Comment.post_id == post).all()
    return listComment

def create_Comment(db:Session,comentario:Comentario):
    
    try:
        createComment = Comment(
            usuario_id=comentario.usuario_id,
            post_id=comentario.post_id,
            contenido=comentario.contenido,fecha=comentario.fecha,estado=comentario.estado
            )
        db.add(createComment)
        db.commit()
        db.refresh(createComment)
    except Exception as e:
        raise(e)
    return createComment

def updateComment(db:Session,comentario:Comentario):
    
    try:
        
        db_comment = db.query(Comment).filter(Comment.id == id).first()

        if not db_comment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment with ID {id} not found")

        
        db_comment.contenido = comentario.contenido
        db_comment.estado = comentario.estado

        db.commit()
        db.refresh(db_comment)
        return db_comment
    except HTTPException as e:
        raise e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error updating comment: {e}")

def deleteComment(db:Session,id:int):
    if(id):
        db.query(Comment).filter(Comment.id == id).delete(synchronize_session=False)
        return {"mensaje":"comentario eliminado"}