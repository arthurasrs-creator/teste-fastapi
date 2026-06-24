from sqlalchemy import Column, Integer, String
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(100), nullable=False)
    senha = Column(String(255), nullable=False)