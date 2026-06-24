from fastapi import FastAPI

from app.database import Base, engine

from app.models.usuario import Usuario
Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/", tags=["Main"])
async def home():
    return {"msg": "bem vindo"}