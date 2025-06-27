from fastapi import APIRouter , Depends,HTTPException
from app.schemas.user import Usuario
from app.models.user import UsuarioModel
from app.database import get_db
from sqlalchemy.orm import Session
from app.crud.user import obtenerUsuario,crearUsuario,getUserByID

userRouter = APIRouter(prefix="/user")

@userRouter.get("")
async def getUser(db : Session = Depends(get_db)):
    Usuario = obtenerUsuario(db)
    return Usuario


@userRouter.get("/{id}")
async def getUserById(id:int,db : Session = Depends(get_db)):
    user = getUserByID(db,id)
    if not user:
        raise HTTPException(status_code=200)
    
    return user


@userRouter.post("")
async def createUser(user:Usuario ,db : Session = Depends(get_db)):
    
    if(crearUsuario(db,user)):
        raise HTTPException(status_code=201)
    raise HTTPException(status_code=400)