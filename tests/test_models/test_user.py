#!/usr/bin/python3
"""Unittest for BaseModel class
"""


import unittest
from models.user import User


class TestUserClass(unittest.TestCase):
    """Test Cases for User class"""

    def test__to_dict(self):
        """Test to_dict method correctness"""
        model = User()
        model.email = "admin@email.com"
        self.assertTrue('email' in model.to_dict())
