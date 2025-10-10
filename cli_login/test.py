import requests
from requests.exceptions import HTTPError


API_URL = "http://127.0.0.1:8000"

response = requests.get(API_URL)
print(response.headers)

if response.status_code == 200:
    print("True")
else:
    raise Exception(f"error: {Exception}")


user_data = '{"name":"newguy","username":"femi","email":"femom@mail.com","password":"iamjane"}'
create_user = requests.post("http://127.0.0.1:8000/register_user", data=user_data)
print(create_user.content)
print(create_user.response)