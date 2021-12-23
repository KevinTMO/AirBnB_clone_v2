#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
import os
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    name = ""
