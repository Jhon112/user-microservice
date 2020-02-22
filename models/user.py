#!/usr/bin/python3
"""
User Class from Models Module
"""
import hashlib
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float


class User(BaseModel, Base):
    """
        User class handles all application users
    """
    __tablename__ = 'users'
    name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """
            instantiates user object
        """
        super().__init__(*args, **kwargs)
