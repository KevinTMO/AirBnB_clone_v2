#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.db_storage import DBStorage


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
    """
    Add conditional depending value of env variable
    HBNB_TYPE_STORAGE
    If equal to db
    """
else:
    storage = FileStorage()
    storage.reload()
