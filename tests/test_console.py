#!/usr/bin/python3
"""Unittest for console
"""


import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test Cases for Base class"""

    def test__to_dict(self):
        """Test to_dict method correctness"""
        console = HBNBCommand()
       # test it
