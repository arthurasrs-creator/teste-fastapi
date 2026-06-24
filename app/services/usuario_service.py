from sqlalchemy.orm import Session
from app.models.usuario import Usuario

from fastapi import HTTPException
from werkzeug.security import generate_password_hash

def criar_usuario(db: Session, email:str, senha:str):
    usuario = db.query(Usuario).get(email)
    if usuario:
        raise HTTPException(
            401,detail="email ja em uso"
        )
    
    senha_hash = generate_password_hash(senha)

    novo_usuario = Usuario(email=email, senha=senha_hash)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario