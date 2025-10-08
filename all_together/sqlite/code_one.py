import sqlite3
import time

# db init functions

def get_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(f"Error: {e}")
        raise

def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """
    try:
        with connection:
            connection.execute(query)
        print("table was created")
    except Exception as e:
        print(f'Error: {e}')
        raise

def register_user(connection, name, username, email, password):
    query = "INSERT INTO users (name, username, email, password) VALUES (?,?,?,?)"
    try:
        with connection:
            connection.execute(query,(name, username, email, password))
            print("you have been registered")
    except Exception as e:
        print(f'Error: {e}')
        raise

def check_details(connection,username):
    query = "SELECT name, email FROM users WHERE username = ?"
    try:
        with connection:
            rows = connection.execute(query,(username,))
            for row in rows:
                print(f'your name is: {row[0]} \nand your email is: {row[1]}')
    except Exception as e:
        print(f'Error {e}')
        raise

def verify_user(connection, username, password):
    query = "SELECT password FROM users WHERE username = ?"
    try:
        with connection:
            rows = connection.execute(query,(username,)).fetchone()
            if rows:
                for row in rows:
                    if row == password:
                        print("correct Details")
                        return True
                    else:
                        print("wrong Password")
                        return False
            else:
                print("wrong username")
                return False
    except Exception as e:
        print(f"Error: {e}")
        raise




def main():
    #initializing connection
    connection = get_connection("my_database.db")
    create_table(connection)

    def register(name, username, email, password):
        register_user(connection, name, username, email, password)
        return True

    def login(username, password):
        if verify_user(connection,username, password):
            print("logged in")
            return True
        else:
            print("login failed")
            return False
        
        
    try:
        #application logic
        def normal_app_state():
            print("not logged in" + " "*10  + time.ctime())
            print("1. Register \n 2. Login \n 3. Exit")
            answer = int(input("Choose an option: "))
            while answer != 3:
                if answer == 1:
                    name = input("Enter your name: ")
                    username = input("Enter your username: ")
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    if register(name,username,email,password):
                        answer = 2
                elif answer == 2:
                    username = input("your username here: ")
                    password = input("your password here: ")
                    if login(username,password):
                        logged_in_state()
                        answer = 0
                elif answer == 3:
                    break
                else:
                    answer = int(input("Choose an option: "))
            answer = 0        
        
        def logged_in_state():
            print(f"logged In as {None}" + " "*10 + time.ctime())
            print("1. Create Note \n 2. Send message \n 3. logout")
            reply = int(input("choose a number in the options: "))
            while reply !=3:
                if reply == 1:
                    print("function coming soon")
                elif reply == 2:
                    print("function coming soon")
                elif reply == 3:
                    print("logging out")
                    time.sleep(2)
                    print("logged out")
                    normal_app_state()
            reply = 0

        normal_app_state()
        
            

        
    finally:
        connection.commit()
        connection.close()




if __name__ == "__main__":
    main()