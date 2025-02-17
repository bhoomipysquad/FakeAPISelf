import requests

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
header = { 'Accept' : 'text/plain',
           'Content-Type' : 'application/json'
         }

request_pay_load = {
                 "id": 155,
                 "title": "Bhoomi",
                 "dueDate": "2025-02-17T08:36:53.201Z",
                 "completed": True
                   }

response = requests.post(url ,
                         headers = header ,
                         json = request_pay_load
                         )

print(response.status_code)
print(response.json())
data = response.json()

assert response.status_code == 200
assert  data['id'] == 155
