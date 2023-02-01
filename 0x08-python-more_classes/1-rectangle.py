#!/usr/bin/python3
"""1-rectangle, built for alx python project 0x08 task 1.
"""


class Rectangle:
    """At this stage the class only creates private instance attributes by
    talking in two argulents.

    Args:
        width (int): horizontal dimension of rectangle, defaults to 0
        height (int): vertical dimension of rectangle, defaults to 0

    """
    def __init__(self, width=0, height=0):
        # attribute assigment here engages setters 
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter

        Returns:
               __width (int): horizontal dimension

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
               value (int): horizontal dimension 

        Attributes:
               __width (int): horizontal dimension a rectangle

        Raises:
             TypeError : If `value` is not an int
             ValueError: If `value` is len than 0.

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
        """__height setter

        Args:
           __height (int): vertical dimension
           value (int) : vertical dimension

        Raises:
            TypeError: If `value` is not an int
            ValueError: If `value` less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
