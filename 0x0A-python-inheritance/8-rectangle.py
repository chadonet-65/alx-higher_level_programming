#!/usr/bin/python3
# 8-rectangle.py
"""Defines a base geometry class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry



class Rectangle(BaseGeometry):
    """Represent a class rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new class.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
