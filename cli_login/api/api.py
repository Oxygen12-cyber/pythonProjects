from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy import select
from sqlalchemy.orm import Session

from dbmodels.db_model import get_db, User, Inventory
from pymodels.pyd_model import UserLogin, UserCreate, UserResponse, UserUpdate, InventoryCheck, InventoryResponse


app = FastAPI(title="Cli App")

@app.get("/")
def home():
    return "hello user"

# DB OPERATIONS 
# login user
@app.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    unhashed = user.password.get_secret_value()
    existing_user = db.execute(select(User).where(User.email == user.email).where(User.password==unhashed)).scalars().first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="User not found")
    return {"message": "this user is verified"}

# create new user
@app.post("/register", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    user_exists = db.execute(select(User).where(User.email == user.email)).scalars().first()

    if user_exists:
        raise HTTPException(status_code=404, detail="User already exists")
    new_user = User(
        name=user.name, 
        username=user.username, 
        email=user.email, 
        password=user.password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#create new task
@app.post("/products/{user_email}", response_model=InventoryResponse)
def create_new_task(user_email: str, produce: InventoryCheck, db: Session = Depends(get_db)):
    user_exists = db.execute(select(User).where(User.email == user_email)).scalars().first()
    if user_exists:
        new_produce = Inventory(
            name = produce.product_name,
            price = produce.product_price,
            description=produce.product_description,
            user_id = user_exists.id
        )
        db.add(new_produce)
        db.commit()
        db.refresh(new_produce)
        return new_produce
    raise HTTPException(status_code=404, detail=f"no user by the email {user_email} exists")

#check tasks specific to user
@app.get("/products/{user_email}", response_model=list[InventoryResponse])
def check_user_tasks(user_email: str, db: Session=Depends(get_db)):
    user_exists = db.execute(select(User).where(User.email == user_email)).scalars().first()
    if user_exists:
        users_products = db.execute(select(Inventory).where(Inventory.user_id==user_exists.id)).scalars().all()
        return users_products
    raise HTTPException(status_code=404, detail="No user with email: {user_email} found!")

# change username/details
@app.patch("/users", response_model=UserResponse)
def change_username(user_email:str, user_updates: UserUpdate, db:Session=Depends(get_db)):
    user_exists = db.execute(select(User).where(User.email==user_email)).scalars().first()
    if not user_exists:
        raise HTTPException(status_code=404, detail='user with that email does not exist')
    
    updates = user_updates.model_dump(exclude_unset=True, exclude_none=True)

    for key, values in updates.items():
        setattr(user_exists, key, values)
        
    db.commit()
    db.refresh(user_exists)
    return user_exists

# delete products
@app.delete("/products/")
def delete_product(user_email:str, product_name:str, db:Session=Depends(get_db)):
    user_exists = db.execute(select(User).where(User.email==user_email)).scalars().first()
    users_product = db.execute(select(Inventory).where(Inventory.name.like(f"%{product_name}%"))).scalars().first()

    if not user_exists:
        raise HTTPException(status_code=404, detail='user with that email does not exist')
    if not users_product:
        raise HTTPException(status_code=404, detail='product with that name does not exist')
    db.delete(users_product)
    db.commit()
    db.refresh(user_exists)
    return {'message':'this product has been deleted'}

# delete user account
@app.delete("/user/")
def delete_user_account(user_email: str, db:Session=Depends(get_db)):
    user_exists = db.execute(select(User).where(User.email==user_email)).scalars().first()
    if not user_exists:
        raise HTTPException(status_code=404, detail="this user does not exists")
    db.delete(user_exists)
    db.commit()
    return {"message":"user's account has been deleted"}