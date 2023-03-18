from dataclasses import dataclass, field
from decimal import Decimal
import requests
from datetime import date


@dataclass
class Cliente():
    nome: str
    cpf: str
    telefone: str
    cartao: str = None
    sexo: str = None
    nascimento: date = None
    email: str = None
    saldo: Decimal = None
    senha: str = None
    endereco: object = None


@dataclass
class Endereco:
    cep: str
    numero: str
    rua: str = field(init=False)
    bairro: str = field(init=False)
    complemento: str = field(init=False)

    def __post_init__(self):
        infos = self.verifica_cep()
        self.rua = infos["logradouro"]
        self.bairro = infos["bairro"]
        self.complemento = infos["complemento"] 

    def verifica_cep(self):
        resposta = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        return resposta.json()