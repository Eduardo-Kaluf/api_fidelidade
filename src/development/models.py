from dataclasses import dataclass, field
from decimal import Decimal
import requests


@dataclass
class Cliente():
    cpf: str
    telefone: str
    cartao: str
    sexo: str = None
    nascimento: str = None
    email: str = None
    saldo: Decimal = None
    senha: str = None
    endereco: object = None
    nome: str = None


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
