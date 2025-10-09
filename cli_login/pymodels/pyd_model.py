from pydantic import BaseModel, EmailStr, SecretStr, ConfigDict
from typing import Optional

class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    name: str
    username: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None

    model_config=ConfigDict(extra='ignore')

class UserLogin(BaseModel):
    email: EmailStr
    password: SecretStr

class InventoryCheck(BaseModel):
    product_name: str
    product_price: int
    product_description: str

class InventoryResponse(BaseModel):
    name: str
    price: int
    description: str
