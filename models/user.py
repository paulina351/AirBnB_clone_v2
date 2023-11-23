#!/usr/bin/python3
"""Define the User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import  relationship


class User(BaseModel, Base):
    """Represents a user from a Mysql database."""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Places", cascade="all", backref="user")
    reviews = relationship("Review", cascade="all", backref="user")
