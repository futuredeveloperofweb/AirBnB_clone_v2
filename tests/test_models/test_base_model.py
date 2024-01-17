#!/usr/bin/python3
""" unittest for base_model"""
import unittest
from models.base_model import BaseModel
import datetime
import json
import os
import pycodestyle
import pep8


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except SomeSpecificException:
            pass

    def test_default(self):
        """Test default instantiation of BaseModel"""
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_save(self):
        """Testing save"""
        i = BaseModel()
        i.save()
        key = "BaseModel." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test string representation of BaseModel"""
        i = BaseModel()
        self.assertEqual(str(i),
                         '[BaseModel] ({}) {}'.format(i.id, i.__dict__))

    def test_todict(self):
        """Test to_dict method of BaseModel"""
        i = BaseModel()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_id(self):
        """Test type of id attribute in BaseModel"""
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test type of created_at attribute in BaseModel"""
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test type of updated_at attribute in BaseModel"""
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_uuid(self):
        """Test UUID uniqueness"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """Test __str__ method"""
        instance6 = BaseModel()
        string_output =
        "[BaseModel] ({}) {}".format(instance6.id, instance6.__dict__)
        self.assertEqual(string_output, str(instance6))

    def test_pycodestyle(self):
        """Test PEP8 compliance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_checking_for_docstring_BaseModel(self):
        """Check docstrings in BaseModel"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """Check existence of essential methods in BaseModel"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_save_BaseModel(self):
        """Test the save method in BaseModel"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """Test the to_dict method in BaseModel"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
