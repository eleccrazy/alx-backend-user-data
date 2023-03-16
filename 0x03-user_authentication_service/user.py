#!/usr/bin/env python3
"""
File: user.py
Desc: This python module contains code for creating a user model.
Author: Gizachew Bayness
Date Created: Mar 16 2023
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """User class"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(205))
    reset_token = Column(String(250))
