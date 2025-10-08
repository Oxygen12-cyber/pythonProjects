from sqlalchemy import create_engine, select, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
import time


# Creating the DB
engine = create_engine('sqlite:///joshvideo.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Defining models 
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    tasks = relationship('Task', back_populates='user', cascade="all, delete-orphan")

    def __repr__(self):
        return f"username: {self.name}\nemail: {self.email}"


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship('User',back_populates='tasks')

    def __repr__(self):
        return f"{self.user}'s task title is: {self.title} and description is {self.description}"

Base.metadata.create_all(engine)

# Utility functions
def get_user_by_email(email):
    return session.execute(select(User).where(User.email==email)).scalars().first()

def get_tasks_by_email(email):
    user = get_user_by_email(email)
    return session.scalars(select(Task).where(email==user.email)).all()

#  confirmation for loop
def confirm_action(prompt:str) -> bool:
    return input(f'{prompt}(yes/no: ').strip().lower() == "yes"

# CRUD Ops
def add_user():
    name, email = input("enter user name: "), input("enter the email: ")
    if get_user_by_email(email):
        print(f"user already exists: {email}")
        return 
    with session as sess:
        try:
            sess.add(User(name=name, email=email))
            sess.commit()
            print(f"User: {name} is now added")

        except Exception as e:
            sess.rollback()
            print(f'Error {e}')

def add_task():
    email = input("enter your email to add tasks: ")
    user = get_user_by_email(email)
    if not user:
        print(f'no user found with that email {email}')
        return
    
    title, description = input('enter the title: '), input('enter the description: ')
    session.add(Task(title=title, description=description, user=user))
    session.commit()
    print(f"tasks added to {user.email}'s account")

# Queries
def query_users():
    stmt = select(User)
    users = session.execute(stmt).scalars().all()
    print(users)

def query_tasks():
    email  = input("enter your email: ")
    taskss = get_tasks_by_email(email)
    if not taskss:
        print("no email found")
        return
    print(taskss)

def update_user():
    email = input("type in your email: ")
    with session as sess:
        user = get_user_by_email(email)
        if not user:
            print(f"user not found with that email")
            return 
        new_username = input("enter your new username: ")
        user.name = new_username
        sess.commit()
        print(f"username for {email} has been changed to {user.name}")

def delete_user():
    email = input("your email")
    info = get_user_by_email(email)
    
    if not info:
        print("email not found")
        return
    
    user = session.get(User,info.id)
    with session as sess:
        sess.delete(user)
        print("user {info.name} and his tasks will be deleted")

        sess.commit()

def delete_task():
    pass


# MAIN Ops
# main function
def main():
    actions = {
        "1":add_user,
        "2":add_task,
        "3":query_users,
        "4":query_tasks,
        "5":update_user,
        "6":delete_user,
        "7":delete_task,
        
    }
    
    while True:
        print("\n Options: \n 1. Add user\n 2. Add task\n 3. Query users\n 4. query tasks\n 5. Update user\n 6. Delete user\n 7. delete Task\n 8. Exit")
        choice = input("Enter an option: ")
        if choice == "8":
            print("logging out")
            time.sleep(2)
            break
        action = actions.get(choice)
        time.sleep(2)
        if action:
            action()
        else:
            print("that is not an option!!!")

if __name__ == "__main__":
    main()