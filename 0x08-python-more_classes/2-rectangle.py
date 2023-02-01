#!/usr/bin/python3
"""2-rectangle, built for alx python project 0x08 task 2.
"""


class Rectangle:
    """ At this stage class only creates private instance attribute bay 
    talking in two arguments.

    Args:
        width (int): horizontal dimension a rectangle
        height (int): vertical dimension a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter
        Returns:
            __width (int): horizontal dimension a rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """__width setter

        Args:
           value (int): horizontal dimension a rectangle

        Attribute:
            __width (int): horizontal dimension a rectangle

        Raises:
            TypeError: If `value` is not an int
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter
        
        Returns:
           __height (int): vertical dimension a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """__height getter

        Args:
           value (int): vertical dimension a rectangle

        Attributes:
            __height (int): vertical dimension a rectangle
        Raises:
           TypeError: If `value` is not an int
           ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """function that return the rectangle area

        Attributes:
           width (int): horizontal dimension a rectangle
           height (int): vertical dimension a rectangle

        """
        return (self.__width * self.__height)
    
    def perimeter(self):
        """function that return perimeter
        Returns:
           0 if either attribute is 0, or the perimeter: 

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
