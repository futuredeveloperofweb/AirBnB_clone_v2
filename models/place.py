#!/usr/bin/python3
"""This module defines the Place class."""
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import shlex
import models
from models.base_model import BaseModel, Base

# Association Table for the many-to-many relationship between Place and Amenity
place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """This class represents a Place in the application.

    Attributes:
        city_id (str): The ID of the City to which this Place belongs.
        user_id (str): The ID of the User who owns this Place.
        name (str): The name of the Place.
        description (str): A description of the Place.
        number_rooms (int): The number of rooms in the Place.
        number_bathrooms (int): The number of bathrooms in the Place.
        max_guest (int): The maximum number of guests the Place.
        price_by_night (int): The price per night for staying in the Place.
        latitude (float): The latitude coordinate of the Place.
        longitude (float): The longitude coordinate of the Place.
        amenity_ids (list): A list of Amenity IDs associated with the Place.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Returns a list of Review objects associated with this Place."""
            all_objects = models.storage.all()
            reviews_list = [all_objects[key] for key in
                            all_objects if
                            shlex.split(key.replace('.', ' '))[0] == 'Review']
            return [review for review in
                    reviews_list if review.place_id == self.id]

        @property
        def amenities(self):
            """Returns a list of Amenity IDs associated with this Place."""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Appends Amenity IDs to the amenity_ids attribute."""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
