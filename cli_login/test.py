import requests
from requests.exceptions import HTTPError
import json
import time
from typing import Optional
from pydantic import BaseModel, SecretStr


API_URL = "http://127.0.0.1:8000"

# response = requests.get(API_URL)
# print(response.headers)

# if response.status_code == 200:
#     print("True")
# else:
#     raise Exception(f"error: {Exception}")


# user_data = '{"name":"newguy","username":"femi","email":"femom@mail.com","password":"iamjane"}'
# create_user = requests.post("http://127.0.0.1:8000/register_user", data=user_data)
# print(create_user.content)
# print(create_user.response)

def register():
    requests.get("http://127.0.0.1:8000/")
    time.sleep(3)
    your_name = "james"
    username = "xoxouser"
    email = "james@mail.com"
    password = "nothing"
    user_data = '{"name" : your_name,"username" : username,"email" : email,"password" : password}'
    print(user_data)
    print(user_data.json().items())
    
    for key, value in user_data.json().items():
        if value != "":
            response = requests.post("http://127.0.0.1:8000/register_user", data=user_data)
            print(response.content)
            filtered_resp = response.json()
            print(filtered_resp)
        else:
            print(f"error: {key}:{value}")

def test():
    
    #SECRET VALUE TESTS
    # class TestModel(BaseModel):
    #     name: str
    #     password: SecretStr

    # user = TestModel(name = "james", password="112345")
    # print(f"{user.name}'s password is {user.password}")
    # print(f"{user.name}'s password is {user.password.get_secret_value()}")
    # print(f"{user.name}'s password is {user.password._secret_value}")
    

    #IF STATEMENT TEST
    name = "l"
    email= "k"
    if not name or not email:
        print("one is missing")
    else: print("all is correct")


    #API LOGIN TEST 
    # login_data = {"email":"user@mail.com","password":"123456"}
    # verify = requests.post(url=API_URL + "/login", json=login_data, timeout=8)
    # if verify.status_code == 200:
    #     print("user logged in successfully")
    #     time.sleep(3)
    #     content = verify.content
    #     print(json.loads(content)["message"])


test()