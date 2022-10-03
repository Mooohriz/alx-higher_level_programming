#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the square class"""

        super().__init__(size, size, x, y, id)
        """validation of attribute: size"""
        self.size = self.width

    @property
    def size(self):
        """retrieving the size using the width"""
        return self.width

    @size.setter
    def size(self, value):
        """setting the size"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """assigning arguments to each attributes using args and kwargs"""
        if args is not None and len(args) > 0:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.size = value
                elif key == 2:
                    self.x = value
                elif key == 3:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    self.id = value

    def to_dictionary(self):
        """returns dictionary representation of square"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
