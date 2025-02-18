import requests
import pytest

def test_post_author():
    url = 'https://fakerestapi.azurewebsites.net/api/v1/Authors'
    header = {'accept': 'text/plain', 'Content-Type':'application/json'}
    payload = {
                 "id": 749,
                 "idBook": 448,
                 "firstName": "string1",
                 "lastName": "string2"
              }

    response = requests.post(url , headers= header, json=payload)
    print(response.json())
    data = response.json()

    # Assert the response contains the fields we sent in the request
    assert data["id"] == payload["id"], "Author ID mismatch"
    assert data["firstName"] == payload["firstName"], "Author firstName mismatch"
    assert data["lastName"] == payload["lastName"], "Author lastName mismatch"
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


if __name__ == "__main__":
    pytest.main()


