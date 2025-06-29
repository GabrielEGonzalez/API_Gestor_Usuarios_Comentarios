from app.models.comment import Comment

from app.schemas.comment import ComentarioBase, ComentarioResponse
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def obtenerComment(db:Session) -> list[Comment]:
    """
    Retrieves all comments from the database.
    """
    comentarios = db.query(Comment).all()
    return comentarios

def getCommentPOST(db:Session, post: int) -> list[Comment]:
    """
    Retrieves comments associated with a specific post ID.
    """
    listComment = db.query(Comment).filter(Comment.post_id == post).all()
    return listComment

def createComment(db:Session, comentario_data: ComentarioBase) -> Comment:
    """
    Creates a new comment in the database.
    """
    try:
        
        create_comment_db = Comment(
            usuario_id=comentario_data.usuario_id,
            post_id=comentario_data.post_id,
            contenido=comentario_data.contenido,
            fecha=comentario_data.fecha,
            estado=comentario_data.estado
        )
        db.add(create_comment_db)
        db.commit()
        db.refresh(create_comment_db)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error creating comment: {e}")
    return create_comment_db

def updateComment(db:Session, id: int, comentario_data: ComentarioBase) -> Comment:
    """
    Updates an existing comment's content or state in the database.
    """
    try:
        db_comment = db.query(Comment).filter(Comment.id == id).first()

        if not db_comment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment with ID {id} not found")

        # Actualiza solo los campos que quieres permitir
        db_comment.contenido = comentario_data.contenido
        db_comment.estado = comentario_data.estado
        db_comment.fecha = comentario_data.fecha

        db.commit()
        db.refresh(db_comment)
        return db_comment
    except HTTPException as e:
        raise e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error updating comment: {e}")

def deleteComment(db:Session, id: int):
    """
    Deletes a comment from the database by its ID.
    """
    try:
        comment_to_delete = db.query(Comment).filter(Comment.id == id).first()

        if not comment_to_delete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment with ID {id} not found")

        db.delete(comment_to_delete)
        db.commit()
        return {"mensaje": f"Comentario con ID {id} eliminado exitosamente"}
    except HTTPException as e:
        raise e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error deleting comment: {e}")
