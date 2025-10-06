from sqlalchemy import create_engine, Integer, ForeignKey, String, Column
from pydantic import BaseModel
from sqlalchemy.orm import Session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base



engine = create_engine("sqlite:///alchemist.db", echo=True)
session =  sessionmaker(bind=engine)
Base = declarative_base()


class Alchemists(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    power = relationship("ChemistAbility", back_populates="ability", uselist=False)

    def __repr__(self):
        return f"user{self.id}'s name is {self.name} and power is {self.power}"
    
class ChemistAbility(Base):
    __tablename__ = "abilities"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    ability = relationship("Alchemists", back_populates="power")

    def __repr__(self):
        return f"user{self.user_id}'s power is {self.ability} and and it can: {self.description}"

Base.metadata.create_all(engine)

db = session()

def add_users(name, power, description, ability):
    user = Alchemists(name=name, power=power)
    ability = ChemistAbility(description=description, ability=user)
    db.add(user)
    db.add(ability)
    db.commit()
    db.refresh(user)
    return user



add_users("james","super-speed","be very fast in doing things", "super-snap, super-fast, speed-thinking")






