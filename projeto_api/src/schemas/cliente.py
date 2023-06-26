from pydantic import BaseModel
from datetime import date


class ClienteBase(BaseModel):
    nr_cpf: str


class EnderecoBase(BaseModel):
    cep: str
    num: int


class ClienteInsert(ClienteBase):
    nm_cliente: str
    nr_cpf: str
    telefone: str
    email: str = None
    senha: str = None
    dt_nascimento: date = None
    sexo: str = None
    num_cartao: str = None
    saldo: int = None


class ClienteResponse(ClienteBase):
    nm_cliente: str
    fone: str
    dt_nascimento: date
    email: str


class ClientePatch(ClienteBase):
    cd_cliente: int
    nm_cliente: str = None
    nr_cpf: str = None
    telefone: str = None
    email: str = None
    senha: str = None
    dt_nascimento: date = None
    sexo: str = None
    num_cartao: str = None
    saldo: int = None


class PontuarCliente(BaseModel):
    cd_cliente:     int
    pnts_add:       int
    dt:             date = None
    tipo_compra:    str  = None
    loja:           str  = None
