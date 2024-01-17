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
        l = []
        rs = []
        for ky in vr:
            ct = ky.replace('.', ' ')
            ct = shlex.split(ct)
            if (ct[0] == 'City'):
                lista.append(var[ky])
        for x in l:
            if (x.state_id == self.id):
                result.append(x)
        return (rs)
