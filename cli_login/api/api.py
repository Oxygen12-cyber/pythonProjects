from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from dbmodels.db_model import get_db, User, Inventory
from pymodels.pyd_model import UserCreate, UserLogin


app = FastAPI()

@app.get("/")
def home():
    return "hello user"

# DB OPERATIONS 
@app.post("/")
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    pass