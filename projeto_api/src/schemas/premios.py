from pydantic import BaseModel


class PremioBase(BaseModel):
    ...


class PremioInsert(PremioBase):
    nome:           str
    descricao:      str = None
    custo:          int = None
    qnt_estoque:    int = None


class PremioResgate(PremioBase):
    cd_premio:      int
    cd_cliente:     int
    qnt_resgate:    int
