#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import shlex
from os import getenv
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """Get a list of all related City objects."""
        var = models.storage.all()
        city_list = []  # Changed variable name from 'l' to 'city_list'
        result = []  # Changed variable name from 'rs' to 'result'

        for key in var:
            city_key = key.replace('.', ' ')
            city_key = shlex.split(city_key)
            if city_key[0] == 'City':
                city_list.append(var[key])

        for city in city_list:
            if city.state_id == self.id:
                result.append(city)

        return result
