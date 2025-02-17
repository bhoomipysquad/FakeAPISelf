import requests


url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/5"
header = {'accept' : 'text/plain'
         }

response = requests.get(url , headers = header)

print(response.status_code)
print(response.json())

assert response.status_code == 200
