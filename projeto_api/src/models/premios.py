from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class PremioTable(Base):
    __tablename__ = "premios"
    cd_premio:     Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:          Mapped[str] = mapped_column(String(200))
    descricao:     Mapped[str] = mapped_column(String(2000), nullable=True)
    custo:         Mapped[int] = mapped_column(nullable=True)
    qnt_estoque:   Mapped[int] = mapped_column(nullable=True)
