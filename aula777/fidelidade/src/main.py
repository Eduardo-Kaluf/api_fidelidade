from fastapi import FastAPI
from schemas.cliente import ClienteInsert, ClienteSelect, ClienteResponse


app = FastAPI()

@app.get("/")
def root():
    return "rooot"

@app.get("/cliente")
def mostra_cliente(cliente: ClienteSelect):
    return cliente.__dict__

@app.post("/cliente")
def cadastra_cliente(cliente: ClienteInsert):
    return ClienteResponse(
        cd_cliente=1,
        nm_cliente=cliente.nm_cliente,
        nr_cpf=cliente.nr_cpf,
        dt_nascimento=cliente.dt_nascimento,
        email=cliente.email,
        fone=cliente.fone
    )
