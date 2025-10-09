from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, select, update, Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel, EmailStr

# Api initialization
app = FastAPI()

# DB initialization
engine = create_engine("sqlite:///api_database.db", echo=True)
seession = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    with seession() as session:
        yield session

# DB MODELS
class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    username: str = Column(String, nullable=False)
    email:str = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"{self.name}'s username is {self.username} and email is {self.email}"

Base.metadata.create_all(engine)

# PYD MODELS
class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr

# DB OPERATIONS
def add_user(user: UserCreate):
    with Session() as db:
        try:
            a_user = User(name=user.name, username=user.username, email=user.email)
            db.add(a_user)
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"{e} \n Error occured")
        finally:
            print("user: {a_user.name} has been added")



# API OPERATIONS
# home
@app.get("/")
def home():
    return "Hello, Oxygen"

# checking user details
@app.get("/user/{user_id}")
def get_user(user_id: int, db: Session=Depends(get_db)):
     users = db.execute(select(User).where(User.id == user_id)).scalar()
     if not users:
         return f"no user found by that id"
     return users

# adding new user
@app.post("/user/register")
def add_new_user(user: UserCreate, db:Session=Depends(get_db)):
    new_user = User(name=user.name, username=user.username, email=user.email)
    user_exists = db.execute(select(User).where(User.email == new_user.email)).scalar()
    if user_exists:
        return "user already exists"
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return f"user successfully added to database{new_user}"

# updating user details
@app.put("/user/{user_id}")
def update_user_details(user_id: int, user: UserCreate, db:Session=Depends(get_db)):
    user_check = db.execute(select(User).where(User.id == user_id)).scalar()
    if not user_check:
        return "User with that id does not exist"

    if not user.model_dump(exclude_unset=True):
            return {
                "message": "Current user data",
                "current_data": {
                    "name": user_check.name,
                    "email": user_check.email,
                    "username": user_check.username
                    }
                }

    updated_details = user.model_dump(exclude_unset=True)
    db.execute(update(User).where(User.id == user_id).values(**updated_details))
    db.commit()



def main():
    name, username, email = input("your name: "), input("your username: "), input("your email: ")
    new_user = UserCreate(name=name, username=username, email=email)
    add_user(new_user)





if __name__ == "__main__":
     main()