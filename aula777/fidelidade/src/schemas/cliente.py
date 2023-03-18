from pydantic import BaseModel
from datetime import date


class ClienteBase(BaseModel):
    nr_cpf: str


class ClienteInsert(ClienteBase):
    nm_cliente: str
    fone: str
    dt_nascimento: date
    email: str

class ClienteSelect(ClienteBase):
    pass


class ClienteResponse(ClienteBase):
    nm_cliente: str
    fone: str
    dt_nascimento: date
    email: str