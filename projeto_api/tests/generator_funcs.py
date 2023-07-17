def cpf_payload(lista):
    payload = []
    for i in lista:
        data = {
        "cliente": {
            "nr_cpf": f"{i}",
            "nm_cliente": "string",
            "telefone": "string",
            "email": "string",
            "senha": "string",
            "dt_nascimento": "2023-06-28",
            "sexo": "string",
            "num_cartao": "string",
            "saldo": 0
        },
        "cep_e_num": {
            "cep": "49035-253",
            "num": 0
        }
        }
        payload.append((data, 400))
    return payload

def cep_payload(lista):
    payload = []
    for i in lista:
        data = {
        "cliente": {
            "nr_cpf": "336.252.053-78",
            "nm_cliente": "string",
            "telefone": "string",
            "email": "string",
            "senha": "string",
            "dt_nascimento": "2023-06-28",
            "sexo": "string",
            "num_cartao": "string",
            "saldo": 0
        },
        "cep_e_num": {
            "cep": f"{i}",
            "num": 0
        }
        }
        payload.append((data, 400))
    return payload
