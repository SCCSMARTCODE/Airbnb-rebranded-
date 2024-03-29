#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, INTEGER, String, ForeignKey


class City(BaseModel, Base):
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),  ForeignKey('states.id', ondelete='CASCADE'), nullable=False,)

    """ The city class, contains state ID and name """
    # state_id = ""
    # name = ""
