#!/usr/bin/python3
"""Unittest for BaseModel class
"""


import unittest
from models.place import Place


class TestAemnityClass(unittest.TestCase):
    """Test Cases for Place class"""

    def test__to_dict(self):
        """Test to_dict method correctness"""
        model = Place()
        model.name = "Manhattan"
        self.assertTrue('name' in model.to_dict())
