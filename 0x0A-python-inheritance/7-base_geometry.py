#!/usr/bin/python3
# 7-base_geometry.py
"""Define a class BaseGeometry"""


class BaseGeometry:
    "Represent a class BaseGeometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """That function valid integer.

        Args:
           name (string): Name is value
           value (int): That is integer
        Returns:
           TypeError: must be an integer
           ValueError: must be geated than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
