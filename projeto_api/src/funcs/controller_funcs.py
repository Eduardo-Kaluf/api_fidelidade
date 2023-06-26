from models.cliente import EnderecoTable, ClienteTable, ComprasTable
from models.premios import PremioTable
from sqlalchemy import delete


def init_endereco(endereco: object) -> object:
    e = EnderecoTable(
        cep         =endereco.cep,
        numero      =endereco.numero,
        rua         =endereco.rua,
        bairro      =endereco.bairro,
        complemento =endereco.complemento
    )
    return e


def init_cliente(cliente, endereco) -> object:
    c = ClienteTable(
        nm_cliente      =cliente.nm_cliente,
        nr_cpf          =cliente.nr_cpf,
        telefone        =cliente.telefone,
        email           =cliente.email,
        senha           =cliente.senha,
        dt_nascimento   =cliente.dt_nascimento,
        sexo            =cliente.sexo,
        cd_endereco     =[endereco],
        num_cartao      =cliente.num_cartao,
        saldo           =cliente.saldo
    )
    return c


def init_compras(informacoes):
    compras = ComprasTable()
    compras.cd_cliente       = informacoes.cd_cliente
    compras.pnts_add         = informacoes.pnts_add
    compras.dt               = informacoes.dt
    compras.tipo_compra      = informacoes.tipo_compra
    compras.loja             = informacoes.loja
    return compras


def init_premios(informacoes):
    premio = PremioTable()
    premio.nome              = informacoes.nome
    premio.descricao         = informacoes.descricao
    premio.custo             = informacoes.custo
    premio.qnt_estoque       = informacoes.qnt_estoque
    return premio


def patch_cliente(c_db, cliente):
    c_db.nm_cliente    = cliente.nm_cliente    or c_db.nm_cliente
    c_db.nr_cpf        = cliente.nr_cpf        or c_db.nr_cpf
    c_db.telefone      = cliente.nr_cpf        or c_db.nr_cpf
    c_db.email         = cliente.email         or c_db.email
    c_db.senha         = cliente.senha         or c_db.senha
    c_db.dt_nascimento = cliente.dt_nascimento or c_db.dt_nascimento
    c_db.sexo          = cliente.sexo          or c_db.sexo
    c_db.num_cartao    = cliente.num_cartao    or c_db.num_cartao
    c_db.saldo         = cliente.saldo         or c_db.saldo
    return c_db


def get_cliente(session, cd_cliente, first):
    resultado = session.query(ClienteTable).filter_by(cd_cliente=cd_cliente)

    if first is True:
        return resultado.first()
    else:
        return resultado


def get_premio(session, cd_premio, first):
    resultado = session.query(PremioTable).filter_by(cd_premio=cd_premio)

    if first is True:
        return resultado.first()
    else:
        return resultado


def commit_db(session, *arg):
    if arg is not None:
        for i in arg:
            session.add(i)
    session.commit()


def delete_stmt(session, table, cd_cliente):
    session.execute(delete(table).where(table.cd_cliente == cd_cliente))
