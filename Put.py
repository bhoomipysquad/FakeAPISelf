import requests


url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/5"
header = {'accept' : 'text/plain'
             }

response = requests.get(url , headers = header)
print("Before update")
print(response.json())

# for put
header_put = {'accept' : 'text/plain',
            'Content-Type': 'application/json'
             }
put_payload = {
             "id": 6,
             "title": "Api Testing",
             "dueDate": "2025-02-17T09:17:53.832Z",
             "completed": True
              }
print("After update")

response_put = requests.put(url , headers=header_put , json = put_payload)
print(response_put.json())