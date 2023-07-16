#!/usr/bin/python3
"""Unittest for BaseModel class
"""


import unittest
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """Test Cases for Review class"""

    def test__to_dict(self):
        """Test to_dict method correctness"""
        model = Review()
        model.text = "Excellent"
        self.assertTrue('text' in model.to_dict())
