#!/usr/bin/python3
"""Unittest for BaseModel class
"""


import unittest
from models.city import City


class TestAemnityClass(unittest.TestCase):
    """Test Cases for City class"""

    def test__to_dict(self):
        """Test to_dict method correctness"""
        model = City()
        model.name = "New York"
        self.assertTrue('name' in model.to_dict())
