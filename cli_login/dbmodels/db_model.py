from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, Mapped,mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

# DB INITIALIZATION
Base = declarative_base()
engine = create_engine("sqlite:///my_database.db", echo=True)
Session = sessionmaker(bind=engine)

# session dependency with yield
def get_db():
    with Session() as session:
        yield session

# DEFINING MODELS
class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    products = relationship("Inventory", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"{self.username}'s email is {self.email}"
    
class Inventory(Base):
    __tablename__ = "inventory"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    price: int = Column(Integer, nullable=False)
    description: str = Column(String, nullable=False)
    user = relationship("User",back_populates="products")
    user_id = Column(Integer, ForeignKey("user.id"))

    def __repr__(self):
        return f"product {self.name}'s price is {self.price}"

Base.metadata.create_all(engine)

# BASIC FUNCTIONALITIES
def create_user():
    pass

def get_user_by_email(email):
    pass

def delete_user(user):
    pass
