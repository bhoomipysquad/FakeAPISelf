from xml.etree.ElementTree import indent
import pytest
import requests

def test_put_author():
    url = 'https://fakerestapi.azurewebsites.net/api/v1/Authors/90'
    header = {'accept': 'text/plain'}
    pyload = {
                "id": 90,
                "idBook": 0,
                "firstName": "string1",
                "lastName": "string"
              }
    responce = requests.put(url , headers=header , json=pyload)
    print(responce.json())
    assert responce.status_code == 200

