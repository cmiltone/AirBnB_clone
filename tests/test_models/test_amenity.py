#!/usr/bin/python3
"""Unittest for BaseModel class
"""


import unittest
from models.amenity import Amenity


class TestAemnityClass(unittest.TestCase):
    """Test Cases for Amenity class"""

    def test__to_dict(self):
        """Test to_dict method correctness"""
        model = Amenity()
        model.name = "WiFi"
        self.assertTrue('name' in model.to_dict())
