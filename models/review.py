#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
import os
import models
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
