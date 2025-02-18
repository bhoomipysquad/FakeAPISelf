import requests

url = 'https://gorest.co.in/public/v2/users'
header = { 'Content-Type': 'application/json',
           'Authorization' : 'Bearer ec1a5713623d266455e18b8bf52ed0a58f86bf69ad901737422a6c7acf276f5e'
}
body = {
  "name": "Bhoomi",
  "email": "mishra_sachin8989d0@nader.example",
  "gender": "male",
  "status": "inactive"
       }

response = requests.post(url , headers=header , json = body)

print(response.json())
if response.status_code == 201:
    print("New contact created")


get_response = requests.get(url , headers=header)
print(get_response.json())
