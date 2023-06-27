from dataclasses import dataclass, field
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Date, ForeignKey
from typing import List
import requests


class Base(DeclarativeBase):
    pass


class ClienteTable(Base):
    __tablename__ = "clientes"

    cd_cliente:    Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nm_cliente:    Mapped[str] = mapped_column(String(50))
    nr_cpf:        Mapped[str] = mapped_column(String(15), unique=True)
    telefone:      Mapped[str] = mapped_column(String(20), nullable=True)
    email:         Mapped[str] = mapped_column(String(20), nullable=True)
    senha:         Mapped[str] = mapped_column(String(20), nullable=True)
    dt_nascimento: Mapped[str] = mapped_column(Date, nullable=True)
    sexo:          Mapped[str] = mapped_column(String(20), nullable=True)
    cd_endereco:   Mapped[List["EnderecoTable"]] = relationship()
    cd_extrato:    Mapped[List["ComprasTable"]] = relationship()
    num_cartao:    Mapped[str] = mapped_column(String(20), nullable=True)
    saldo:         Mapped[int] = mapped_column(nullable=True)


class EnderecoTable(Base):
    __tablename__ = "endereco"
    cd_endereco:   Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cd_cliente:    Mapped[int] = mapped_column(ForeignKey("clientes.cd_cliente"))
    cep:           Mapped[str] = mapped_column(String(9))
    numero:        Mapped[str] = mapped_column(String(5))
    rua:           Mapped[str] = mapped_column(String(50))
    bairro:        Mapped[str] = mapped_column(String(80))
    complemento:   Mapped[str] = mapped_column(String(30))


class ComprasTable(Base):
    __tablename__ = "compras"
    cd_compras:    Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cd_cliente:    Mapped[int] = mapped_column(ForeignKey("clientes.cd_cliente"))
    pnts_add:      Mapped[int] = mapped_column(nullable=True)
    dt:            Mapped[str] = mapped_column(Date, nullable=True)
    tipo_compra:   Mapped[str] = mapped_column(String(50), nullable=True)
    loja:          Mapped[str] = mapped_column(String(100), nullable=True)


@dataclass
class Endereco:
    cep: str
    numero: str
    rua: str = field(init=False)
    bairro: str = field(init=False)
    complemento: str = field(init=False)

    def _place_infos(self, infos):
        self.rua = infos["logradouro"]
        self.bairro = infos["bairro"]
        self.complemento = infos["complemento"]

    def verifica_cep(self):
        resposta = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        if resposta.status_code == 400:
            return 0
        self._place_infos(resposta.json())
        return 1
