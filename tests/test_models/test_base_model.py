#!/usr/bin/python3
"""Unittest for BaseModel class
"""


import unittest
from models.base_model import BaseModel


class TestBaseClass(unittest.TestCase):
    """Test Cases for Base class"""

    def test__to_dict(self):
        """Test to_dict method correctness"""
        model = BaseModel()
        model.name = "Bobby"
        self.assertTrue('name' in model.to_dict())
