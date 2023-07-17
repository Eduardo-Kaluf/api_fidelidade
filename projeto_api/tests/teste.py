import requests


obj = {
  "cliente": {
    "nr_cpf": "33333333333",
    "nm_cliente": "Jonas",
    "telefone": "995972397",
    "email": "jonas@gmail.com",
    "senha": "jonas123",
    "dt_nascimento": "2005-04-13",
    "sexo": "Masculino",
    "num_cartao": "77886665511123",
    "saldo": 0
  },
  "cep_e_num": {
    "cep": "57018-520",
    "num": 0
  }
}



url = requests.post("http://127.0.0.1:8000/cliente", json=obj)

#print(url.text)
print(url.json())