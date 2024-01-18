#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import shlex
from os import getenv
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities_relation = relationship("City", backref="state",
                                   cascade="all, delete-orphan")

    @property
    def cities(self):
        """Get a list of all related City objects."""
        var = models.storage.all()
        city_list = []
        result = []

        for key in var:
            city_key = key.replace('.', ' ')
            city_key = shlex.split(city_key)
            if city_key[0] == 'City':
                city_list.append(var[key])

        for city in city_list:
            if city.state_id == self.id:
                result.append(city)

        return result
