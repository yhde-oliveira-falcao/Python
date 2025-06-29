#This is from step 6===================================================================================================
from sqlalchemy import Column, Integer, String, UniqueConstraint
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    nationality = Column(String(50), nullable=False)
    income = Column(Integer, nullable=False)

    #__table_args__ = ( #If you want to have a constraint :)
        # Enforce name + nationality to be unique
    #    UniqueConstraint('name', name='unique_user_identity'),
    #)
