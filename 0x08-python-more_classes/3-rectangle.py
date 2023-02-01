#!/usr/bin/python3


class Rectangle:
    """At this stage only creates private instance attribute by talking in two arguments.
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
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def _rectangle(self):
        string = ""
        for row in range(self.__height):
            for col in range(self.__width):
                string += '#'
            if self.__width != 0 and row < (self.__height - 1):
                string += '\n'
        return string

    def __str__(self):
        return self._rectangle()
