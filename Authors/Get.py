import requests
import pytest

def test_get_authors():
    url = 'https://fakerestapi.azurewebsites.net/api/v1/Authors'
    header = {'accept':'text/plain'}

    response = requests.get(url , headers= header)
    print(response.json())
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


