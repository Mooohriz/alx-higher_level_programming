#!/usr/bin/python3
"""Define a class Base"""


import json
import csv
import turtle


class Base:
    """the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        objs = []
        if list_objs is not None:
            for obj in list_objs:
                objs.append(cls.to_dictionary(obj))
        file1 = cls.__name__ + ".json"
        with open(file1, "w") as f:
            f.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", 'r') as file1:
                json_file = Base.from_json_string(file1.read())
                return [cls.create(**lst) for lst in json_file]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes the CSV str representation of list_objs to a file"""
        fields = []
        with open(cls.__name__ + ".csv", 'w') as f:
            if list_objs is None or len(list_objs) <= 0:
                f.write('[]')
            else:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes the CSV str representation of list_objs 4rm a file"""
        fields = []
        filename = str(cls.__name__) + ".csv"
        try:
            with open(filename, "r", newline="") as file1:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file1, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []
    
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""
        t = turtle.Turtle()
        t.screen.bgcolor('#000000')
        t.shape('turtle')
        t.color('#ffffff')
        t.penup()
        t.goto(-200, 200)
        for rect in list_rectangles:
            t.goto(t.xcor() + (rect.width + 20), t.ycor() - (rect.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.penup()

        t.goto(-200, -20)
        for squ in list_squares:
            t.goto(t.xcor() + (squ.width + 20), t.ycor() - (squ.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(squ.width)
                t.left(90)
                t.forward(squ.height)
                t.left(90)
            t.penup()
        t.Screen().exitonclick()
