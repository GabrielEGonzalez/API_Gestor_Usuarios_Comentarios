from fastapi import APIRouter , Depends, Path, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.crud import comment as crud_comment
from app.schemas.comment import ComentarioBase, ComentarioResponse
from app.database import get_db

router = APIRouter(prefix="/comentarios", tags=["Comentarios"]) 

@router.get('', response_model=List[ComentarioResponse])
async def get_all_comments(db:Session=Depends(get_db)):
    """
    Obtiene una lista de todos los comentarios.
    """
    comentarios = crud_comment.obtenerComment(db)
    return comentarios

@router.get('/por_post/{post_id}', response_model=List[ComentarioResponse])
async def get_comments_by_post_id(post_id: int = Path(gt=0), db:Session=Depends(get_db)):
    """
    Obtiene una lista de comentarios filtrados por el ID del post.
    """
    comments = crud_comment.getCommentPOST(db, post_id)
    if not comments:
        return []
    return comments

@router.post('', response_model=ComentarioResponse, status_code=status.HTTP_201_CREATED)
async def create_new_comment(comentario_data: ComentarioBase, db:Session=Depends(get_db)):
    """
    Crea un nuevo comentario en la base de datos.
    """
    try:
        new_comment = crud_comment.createComment(db, comentario_data)
        return new_comment
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error creating comment: {e}")

@router.put('/{comment_id}', response_model=ComentarioResponse)
async def update_existing_comment(comment_id: int, comentario_data: ComentarioBase, db:Session=Depends(get_db)):
    """
    Actualiza un comentario existente por su ID.
    """
    try:
        updated_comment = crud_comment.updateComment(db, comment_id, comentario_data)
        return updated_comment
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error updating comment: {e}")

@router.delete('/{comment_id}', status_code=status.HTTP_200_OK)
async def delete_comment(db:Session=Depends(get_db), comment_id:int=Path(...,gt=0)):
    """
    Elimina un comentario por su ID.
    """
    try:
        mensaje = crud_comment.deleteComment(db, comment_id)
        return mensaje
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error deleting comment: {e}")
