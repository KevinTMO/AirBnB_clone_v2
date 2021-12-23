#!/usr/bin/python
"""DBStorage engine model description"""
from os import getenv
import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine



class DBStorage:
    """Database storage engine.
    Private class attributes:
        __engine: set to None.
        __session: set to None.
    """
    __engine = None
    __session = None


    """Public instance methods:
       1. __init__(self):
       2. all(self, cls=None):
       3. new(self, obj):
       4. save(self):
       5. delete(self, obj=None):
       6. reload(self):
    """
    def __init__(self):
        """Initialize new engine instance
        Engine must be linked to: MySQL DB, & user created
         dialect: hbnb_dev, and
         driver: hbnb_dev_db
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        """
        Drop all tables - if the environment variable
        (HBNB_ENV) is equal to test.
        """
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

     def all(self, cls=None):
        """
        [x]. Query on the curret DB session (self.__session) all objects (depending class)
        [x]. If cls is None, queries all types of objects.
        Return:
            Dict of queried all type OBJS classes in the format;
            * key = <class name>.<obj id> 
            * value = object
        """
        if cls is None:
            query = self.__session.query(cls).all()
        else:
            query = self.__session.query(User).all()
            query += self.__session.query(State).all()
            query += self.__session.query(City).all()
            query += self.__session.query(Amenity).all()
            query += self.__session.query(Place).all()
            query += self.__session.query(Review).all()

        dic = {}
        for obj in query:
            new_key = '{}.{}'.format(type(obj).__name__, obj.id)
            dic[new_key] = obj
        return dic


    def new(self, obj):
        """Add obj to the current DB session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of current DB session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current DB session obj if not None."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Session Maker
        Create all tables in db from the engine (self.__engine).
        """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        """scoped_session: to make sure Session is thread-safe"""
        Session = scoped_session(self._session)
        self.__session = Session()
