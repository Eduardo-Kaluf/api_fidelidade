import pytest
import requests as re
import json
from generator_funcs import cpf_payload, cep_payload


cpfs = ["111.222.333-51", "SALVE", " ", "", 1, "123"]
ceps = ["12345-51", "123", "STRING", "", " ", 123, 49035-253]

@pytest.mark.parametrize(("payload", "expected"), cpf_payload(cpfs))
def test_wrong_cpfs(payload, expected):
    url = "http://127.0.0.1:8000/cliente"
    response = re.post(url, data=json.dumps(payload))
    assert response.status_code == expected

@pytest.mark.parametrize(("payload", "expected"), cep_payload(ceps))
def test_wrong_ceps(payload, expected):
    url = "http://127.0.0.1:8000/cliente"
    response = re.post(url, data=json.dumps(payload))
    assert response.status_code == expected
