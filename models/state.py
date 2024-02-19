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
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities_relation = relationship("City",
                                       backref="state",
                                       cascade="all,
                                       delete,
                                       delete-orphan")

    else:
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_l = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_l.append(city)
            return city_l
