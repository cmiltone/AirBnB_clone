#!/usr/bin/python3
"""
module for file storage class
"""
import json
from io import StringIO


class FileStorage:
    """a class to serialize and deserialize instances to and from JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objects_dict = {}
        for k in FileStorage.__objects.keys():
            objects_dict[k] = FileStorage.__objects[k].to_dict()
        with open(self.__file_path, "w+") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                data = f.read()
                objs = json.loads(data)
                from models.base_model import BaseModel
                from models.amenity import Amenity
                from models.city import City
                from models.place import Place
                from models.review import Review
                from models.state import State

                for k, v in objs.items():
                    name = v.get('__class__')
                    FileStorage.__objects[k] = eval(str(name))(objs[k])
        except (Exception):
            pass
