from fastapi import APIRouter, Depends

router = APIRouter(prefix="/usuarios", tags=["Usuario"])

from sqlalchemy.orm import Session
from app.database import get_db
from app.services.usuario_service import criar_usuario
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse
@router.post("", response_model=UsuarioResponse)
def create(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario(
        db,
        usuario.email,
        usuario.senha
    )