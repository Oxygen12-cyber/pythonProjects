

import requests
from datetime import datetime

API_URL = "http://127.0.0.1:8000"
request = requests.get(API_URL)
print(request)

def register():
    pass

# login function
def login():
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
    pass
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
        

if __name__ == "__main__":
    main()