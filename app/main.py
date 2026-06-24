from fastapi import FastAPI

from app.database import Base, engine

from app.models.usuario import Usuario
Base.metadata.create_all(engine)

app = FastAPI()

from app.routers.usuario_router import router as usuario_router

app.include_router(usuario_router)

@app.get("/", tags=["Main"])
async def home():
    return {"msg": "bem vindo"}