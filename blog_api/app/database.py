from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base , sessionmaker

engine = create_engine("sqlite:///./sql_app.db")
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db # Permite que el código que lo usa acceda a la sesión
    finally:
        db.close() # Asegura que la sesión se cierre al finalizar