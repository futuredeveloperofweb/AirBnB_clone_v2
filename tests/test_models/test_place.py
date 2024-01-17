""" Unittest for class Place"""
import unittest
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def test_inheritance(self):
        """Test if Place inherits from BaseModel"""
        new_place = Place()
        self.assertIsInstance(new_place, BaseModel)

    def test_attributes(self):
        """Test the attributes of Place"""
        new_place = Place()
        self.assertTrue(hasattr(new_place, 'city_id'))
        self.assertTrue(hasattr(new_place, 'user_id'))
        self.assertTrue(hasattr(new_place, 'name'))
        self.assertTrue(hasattr(new_place, 'description'))
        self.assertTrue(hasattr(new_place, 'number_rooms'))
        self.assertTrue(hasattr(new_place, 'number_bathrooms'))
        self.assertTrue(hasattr(new_place, 'max_guest'))
        self.assertTrue(hasattr(new_place, 'price_by_night'))
        self.assertTrue(hasattr(new_place, 'latitude'))
        self.assertTrue(hasattr(new_place, 'longitude'))
        self.assertTrue(hasattr(new_place, 'amenity_ids'))

    def test_relationships(self):
        """Test the relationships of Place"""
        new_place = Place()
        self.assertTrue(hasattr(new_place, 'reviews'))
        self.assertTrue(hasattr(new_place, 'amenities'))

    def test_amenities_property(self):
        """Test amenities property"""
        new_place = Place()
        self.assertEqual(new_place.amenities, [])
        amenity1 = Amenity()
        amenity2 = Amenity()

        new_place.amenities.append(amenity1)
        new_place.amenities.append(amenity2)

        self.assertEqual(new_place.amenities, [amenity1, amenity2])


if __name__ == "__main__":
    unittest.main()
