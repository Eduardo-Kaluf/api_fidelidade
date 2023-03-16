from fastapi import FastAPI
from models import Cliente


app = FastAPI()

@app.get("/")
def root():
    return "rooot"

@app.post("/integracao/cadastrar_consumidor")
async def create(cliente: Cliente):
    return cliente
