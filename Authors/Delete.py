import pytest
import requests


def test_delete_author():
    url = 'https://fakerestapi.azurewebsites.net/api/v1/Authors/40'
    header = {'accept': '*/*'}
    response = requests.delete(url,headers=header)
    assert  response.status_code == 200

def test_get_after_delete():
    url = 'https://fakerestapi.azurewebsites.net/api/v1/Authors/40'
    header = {'accept': '*/*'}
    new_response = requests.get(url,headers=header)
    if new_response.status_code == 200:
        print("successfully deleted")
    else:
        print(new_response.json())


if __name__ == "__main__":
     pytest.main()



