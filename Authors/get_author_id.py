import pytest
import requests

def test_get_author_id():
    url = 'https://fakerestapi.azurewebsites.net/api/v1/Authors/5'
    header = {'accept':'text/plain'}
    response = requests.get(url , headers=header)
    print(response.json())
    assert response.status_code == 200
