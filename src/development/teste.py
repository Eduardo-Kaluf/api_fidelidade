from models import Cliente, Endereco
import requests
from main import app



cep = "01001000"
numero = "14223"

endereco = Endereco(cep, numero)

cliente = {
    {"cpf": "123",
           "telefone": "M",
           "cartao": "123123"}
}

#"25/05/2006", "@", "999", "123123", 421, "senha123", endereco

resposta = app.post("http://127.0.0.1:8000/integracao/cadastrar_consumidor", data=cliente) 

print(resposta)