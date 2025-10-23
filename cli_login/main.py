import requests
import logging
from datetime import datetime
import json

API_URL = "http://127.0.0.1:8000/"
request = requests.get(API_URL)
print(request)

def register():
    your_name = input(str("Your name: "))
    username = input(str("Your Username: "))
    email = input(str("Your Email: "))
    password = input(str("Your Password: "))
    user_data = {"name" : your_name,"username" : username,"email" : email,"password" : password}
    for key, value in user_data.items():
        if not value:
            return f"error: {value}"
    send = requests.post(url=API_URL + "register_user", json=user_data, timeout=4)
    print()
    return send.content


# login function
def login():

    #take input
    email = str(input("your email: "))
    password = str(input("your password: "))
    #validate input
    if not email and password:
        login_data = {"email":email,"password":password}
    #send to api
        verify = requests.post(url=API_URL+"/login", json=login_data, timeout=8)
    #get api response
    try:
        verify.status_code == 200
    except Exception as e:
        print(e)

    #parse session data
    with open("SESSION.json", "r+") as session:
        pass 

# add task
def add_new_product():
    pass

# check tasks
def check_my_product():
    pass

# Edit my details
def change_username():
    pass
def change_name():
    pass

# remove task
def del_product():
    pass

# delete accound
def del_my_account():
    pass

# logout
def logout():
    pass




def main():
    
    # actions = {
    #     "1":register,
    #     "2":login,   
    # }
    # def get_state():
    #     return f"logged in as: {""}"
    
    # while True:
    #     print(f"{get_state()}{" " * 40} current time is: {datetime.now().strftime("%d-%m-%y %H:%M")}")
    #     print("\n Options: \n 1. register\n 2. login\n 3. Exit")
    #     choice = input("Enter an option: ")
    #     if choice == "3":
    #         print("logging out")
    #         time.sleep(2)
    #         break
    #     action = actions.get(choice)
    #     if action:
    #         time.sleep(2)
    #         action()
    #     else:
    #         print(f"wrong choice, choose again")

    # logged_in_actions = {
    #     "1": add_new_task,
    #     "2": check_my_tasks,
    #     "3": change_username,
    #     "4": change_name,
    #     "5": del_task,
    #     "6": del_my_account,
    #     "6": logout,
    # }
    register()

if __name__ == "__main__":
    main()