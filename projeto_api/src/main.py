from fastapi import FastAPI
from fastapi.responses import JSONResponse
from db.engine import get_session
from schemas.cliente import ClienteInsert, ClientePatch, EnderecoBase, PontuarCliente
from schemas.premios import PremioInsert, PremioResgate
from schemas.response_related import ApiResponse
from models.cliente import ClienteTable, Endereco, EnderecoTable, ComprasTable
from models.premios import PremioTable
from sqlalchemy import text
from funcs.controller_funcs import delete_stmt, init_cliente, init_compras, init_endereco, init_premios, get_cliente, get_premio, commit_db, patch_cliente
from constantes import SCHEMA
from funcs.cpf_validation import CPF

app = FastAPI()

session = get_session()

session.execute(text(f"USE {SCHEMA}"))


@app.get("/extrato")
def extrato(cd_cliente: int):
    resultado = session.query(ComprasTable).filter_by(cd_cliente=cd_cliente)
    compras = {}
    for x, i in enumerate(resultado):
        compras[x + 1] = i.__dict__
    return (compras)


@app.get("/")
def root():
    return "Bem Vindo ao DUDU FIDELIDADE!!!"


@app.get("/clientes")
def mostra_cliente(cd_client: int = None, nr_cpf: str = None):

    results = session.query(ClienteTable)

    if cd_client:
        results = results.filter_by(cd_client=cd_client)
    if nr_cpf:
        results = results.filter_by(nr_cpf=nr_cpf)

    return (results.all())


@app.get("/premios")
def mostra_premios(cd_premio: int = None):

    results = session.query(PremioTable)

    if cd_premio:
        results = results.filter_by(cd_premio=cd_premio)

    return (results.all())


@app.post("/pontuar")
def pontuar(informacoes: PontuarCliente):
    cliente = get_cliente(session, informacoes.cd_cliente, True)
    cliente.saldo += informacoes.pnts_add

    compras = init_compras(informacoes)
    commit_db(session, compras)

    return ("Pontos adicionados!")


@app.post("/cliente", responses={400: {"model": ApiResponse}})
def cadastra_cliente(cliente: ClienteInsert, cep_e_num: EnderecoBase):
    endereco = Endereco(cep_e_num.cep, cep_e_num.num)
    cpf = CPF(cliente.nr_cpf)
    if not endereco.verifica_cep():
        return JSONResponse(status_code=400, content={"status": 400, "message": "CEP inválido"})
    if not cpf.cpf_validation():
        return JSONResponse(status_code=400, content={"status": 400, "message": "CPF inválido"})

    endereco = init_endereco(endereco)
    cliente = init_cliente(cliente, endereco)
    commit_db(session, cliente)

    return ("Sucesso!!!")


@app.post("/premios")
def cadastra_premio(premio: PremioInsert):
    premio = init_premios(premio)
    commit_db(session, premio)

    return ("Sucesso!")


@app.post("/premio")
def resgata_premio(info_resgate: PremioResgate):
    premio = get_premio(session, info_resgate.cd_premio, True)
    cliente = get_cliente(session, info_resgate.cd_cliente, True)
    cliente.saldo -= info_resgate.qnt_resgate * premio.custo
    premio.qnt_estoque -= info_resgate.qnt_resgate
    commit_db(session, premio, cliente)

    return ("Sucesso!")


@app.patch("/cliente_atualiza", responses={400: {"model": ApiResponse}})
async def atualiza_cliente(cliente: ClientePatch):
    c_db = get_cliente(session, cliente.cd_cliente, True)
    if c_db is not None:
        c_db = patch_cliente(c_db, cliente)
        return JSONResponse(status_code=200)
    else:
        return JSONResponse(status_code=400, content={"status": 400, "message": "Cliente não encontrado"})


@app.delete("/cliente_deleta")
def deleta_cliente(cd_cliente: int):
    cliente = get_cliente(session, cd_cliente, True)

    if cliente is not None:
        delete_stmt(session, EnderecoTable, cliente.cd_cliente)
        delete_stmt(session, ComprasTable, cliente.cd_cliente)
        delete_stmt(session, ClienteTable, cliente.cd_cliente)

        session.commit()
        return ("Deletado")
    else:
        # RAISE ERROR
        return ("Cliente não encontrado")
