#!/usr/bin/python3
"""Define a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ the class Rectangle that inherits from class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieving the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieving the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """retrieving x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """retrieving y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the width"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """printing the rectangle using '#'"""
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for row in range(self.__height)))

    def __str__(self):
        """string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigning arguments to each attributes using args and kwargs"""
        if args is not None and len(args) > 0:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.width = value
                elif key == 2:
                    self.height = value
                elif key == 3:
                    self.x = value
                elif key == 4:
                    self.y = value

        else:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    self.id = value

    def to_dictionary(self):
        """returns dictionary representation of Rectangle"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
