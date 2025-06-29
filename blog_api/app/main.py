from fastapi import FastAPI
from app.routes.user import userRouter
from app.routes import comment as comment_routes # Renombrado para evitar conflicto de nombres
from app.models import comment, user # Asegúrate de que estos modelos estén bien definidos
from app.database import engine , Base


app = FastAPI(
    title="Gestor de Usuarios y Comentarios del Blog",
    version="0.1.0"
)

# Esto creará las tablas en tu base de datos si no existen
Base.metadata.create_all(bind=engine)

app.include_router(userRouter)
# Incluye el router de comentarios desde el módulo importado
app.include_router(comment_routes.router) # Corregida la inclusión del router