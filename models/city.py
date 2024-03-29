#!/usr/bin/python3
"""
Module for City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city

    Attributes:
        state_id (str): state id.
        name (str): name of the city.
    """

    state_id = ""
    name = ""
