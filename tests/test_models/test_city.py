#!/usr/bin/python3
'''Module to test the class City'''
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestCity(unittest.TestCase):
    '''test the class City'''
    @classmethod
    def teardown(cls):
        '''delete the contents of the class when deleted'''
        del cls.city

    def test_is_subclass(self):
        '''check if City is subsclass of BaseModel'''
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attributes_City(self):
        '''check the existance of class attributes'''
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_attribute_types(self):
        '''check the type of the attrs'''
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(type(self.city.name), str)


if __name__ == '__main__':
    unittest.main()
