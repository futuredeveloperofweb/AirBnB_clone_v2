#!/usr/bin/python3
""" Unittest for db_storage"""
import unittest
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.engine import db_storage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up the test"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        cls.engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                   .format(user, passwd, host, db),
                                   pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(cls.engine)

    def setUp(self):
        """Set up the test"""
        self.storage = db_storage.DBStorage()
        self.session = scoped_session(
            sessionmaker(bind=self.storage._DBStorage__engine,
                         expire_on_commit=False))

    def tearDown(self):
        """Tear down the test"""
        self.storage.close()
        self.session.remove()

    def test_all(self):
        """Test all method"""
        new_state = State(name="California")
        new_city = City(name="San Francisco", state_id=new_state.id)
        self.storage.new(new_state)
        self.storage.new(new_city)
        self.storage.save()
        objects = self.storage.all()
        self.assertEqual(type(objects), dict)
        key_state = "{}.{}".format(type(new_state).__name__, new_state.id)
        key_city = "{}.{}".format(type(new_city).__name__, new_city.id)
        self.assertIn(key_state, objects)
        self.assertIn(key_city, objects)
        self.assertEqual(objects[key_state], new_state)
        self.assertEqual(objects[key_city], new_city)

    def test_all_with_class(self):
        """Test all method with specific class"""
        new_state = State(name="California")
        new_city = City(name="San Francisco", state_id=new_state.id)
        self.storage.new(new_state)
        self.storage.new(new_city)
        self.storage.save()
        objects = self.storage.all(State)
        self.assertEqual(type(objects), dict)
        key_state = "{}.{}".format(type(new_state).__name__, new_state.id)
        key_city = "{}.{}".format(type(new_city).__name__, new_city.id)
        self.assertIn(key_state, objects)
        self.assertNotIn(key_city, objects)
        self.assertEqual(objects[key_state], new_state)

    def test_new(self):
        """Test new method"""
        new_state = State(name="California")
        self.storage.new(new_state)
        key_state = "{}.{}".format(type(new_state).__name__, new_state.id)
        objects = self.storage.all()
        self.assertIn(key_state, objects)
        self.assertEqual(objects[key_state], new_state)

    def test_save(self):
        """Test save method"""
        new_state = State(name="California")
        self.storage.new(new_state)
        self.storage.save()
        key_state = "{}.{}".format(type(new_state).__name__, new_state.id)
        objects = self.storage.all()
        self.assertIn(key_state, objects)
        self.assertEqual(objects[key_state], new_state)

    def test_delete(self):
        """Test delete method"""
        new_state = State(name="California")
        self.storage.new(new_state)
        self.storage.save()
        key_state = "{}.{}".format(type(new_state).__name__, new_state.id)
        objects = self.storage.all()
        self.assertIn(key_state, objects)
        self.storage.delete(new_state)
        self.storage.save()
        objects = self.storage.all()
        self.assertNotIn(key_state, objects)

    def test_reload(self):
        """Test reload method"""
        new_state = State(name="California")
        self.storage.new(new_state)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertIn(key_state, objects)
        self.assertEqual(objects[key_state], new_state)

    def test_close(self):
        """Test close method"""
        self.storage.close()
        self.assertIsNone(self.storage._DBStorage__session)


if __name__ == "__main__":
    unittest.main()
