#!/usr/bin/python3
"""Unittest for BaseModel class
"""


import unittest
from models.state import State


class TestAemnityClass(unittest.TestCase):
    """Test Cases for State class"""

    def test__to_dict(self):
        """Test to_dict method correctness"""
        model = State()
        model.name = "New York"
        self.assertTrue('name' in model.to_dict())
