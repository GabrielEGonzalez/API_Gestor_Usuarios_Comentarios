from app.models.user import UsuarioModel , direccionModel
from sqlalchemy.orm import Session

def obtenerUsuario(db:Session) -> list:
    
    getusuario = db.query(UsuarioModel).all()
    listausuarios=[]
    
    for usuario in getusuario:
        
        if usuario.direccion_id:
            direccion = db.query(direccionModel).filter(direccionModel.id == usuario.direccion_id).first()
            
            model = {
                        "usuario":{
                                    "id":usuario.id,
                                    "nombre":usuario.nombre,
                                    "email":usuario.email,
                                    "direccion":direccion
                                    }
                    }
            listausuarios.append(model)

    return listausuarios

def crearUsuario(db,User):
    
    direcion = direccionModel(cuidad=User.direccion.cuidad,pais=User.direccion.pais,zip=User.direccion.zip)
    db.add(direcion)
    db.flush()
    
    usuario = UsuarioModel(nombre=User.nombre,email=User.email,direccion_id=direcion.id)
    
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    
    return usuario

def getUserByID(db:Session,id:int):
    
    usuarioid = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()
    direccion = db.query(direccionModel).filter(direccionModel.id == usuarioid.id).first()
    usuario = {"nombre":usuarioid.nombre,"email":usuarioid.email,"direccion":direccion}
    return usuario