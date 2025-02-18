import requests
import  pytest

def test_get_book_id():
    url = 'https://fakerestapi.azurewebsites.net/api/v1/Authors/authors/books/448'
    header = {'accept':'text/plain'}
    response = requests.get(url , headers=header)
    print(response.json())
    assert response.status_code == 200
