
from fastapi import FastAPI
from app.routes.user import userRouter
from app.models import comment, user
from app.database import engine , Base


app = FastAPI(
    title="Gestor de Usuarios y Comentarios del Blog",
    version="0.1.0"
    )

Base.metadata.create_all(bind=engine) 

app.include_router(userRouter)