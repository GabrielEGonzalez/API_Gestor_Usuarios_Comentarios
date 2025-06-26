from app.models.user import UsuarioModel , direccionModel
from sqlalchemy.orm import Session

def obtenerUsuario(db:Session):
    
    getusuario = db.query(UsuarioModel).all()
    return getusuario

def crearUsuario(db,User):
    
    direcion = direccionModel(cuidad=User.cuidad,pais=User.pais,zip=User.zip)
    db.add(direcion)
    db.flush()
    
    usuario = UsuarioModel(nombre=User.nombre,email=User.email,direccion_id=direcion.id)
    
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    
    return usuario

def getUserByID(db:Session,id:int):
    
    usuarioid = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()
    return usuarioid