from pydantic import BaseModel, EmailStr, SecretStr


class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: SecretStr

class UserResponse(BaseModel):
    name: str
    username: str
    email: EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: SecretStr

class InventoryCheck(BaseModel):
    product_name: str
    product_price: str
    product_description: str


test_user = UserCreate(name="james", username="xoxouser12", email="james@mail.com", password="123456")

print(test_user)