#!/usr/bin/python3
"""
    contains Base Class for this project
"""
import json
import csv


class Base:
    """
        base class for this whole project
        Attributes:
            __nb_objs (int)
            id (int)
        Methods:
            __init__()
    """

    __nb_objs = 0

    def __init__(self, id=None):
        """
           Initializes the class attributes
           Args:
               id (int)
        """
        if id is None:
            Base.__nb_objs += 1
            self.id = Base.__nb_objs
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dicts):
        """
            returns JSON string representation of list_dicts
        """
        if list_dicts is None or len(list_dicts) == 0:
            return "[]"
        return json.dumps(list_dicts)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes JSON string of list_objs to a file
        """
        json_file = cls.__name__ + ".json"
        content = []

        if list_objs is not None:
            for obj in list_objs:
                obj = obj.to_dictionary()
                json_dict = json.loads(cls.to_json_string(obj))
                content.append(json_dict)

        with open(json_file, "w") as jfile:
            json.dump(content, jfile)

    @staticmethod
    def from_json_string(json_string):
        """
            returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            mod = Rectangle(2, 7)
        elif cls.__name__ == "Square":
            mod = Square(6)
        mod.update(**dictionary)
        return (mod)

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances
        """
        fname = cls.__name__ + ".json"

        try:
            with open(fname, encoding='utf8') as jfile:
                content = cls.from_json_string(jfile.read())
        except:
            return []

        instances = []

        for instance in content:
            temp = cls.create(**instance)
            instances.append(temp)

        return instances
