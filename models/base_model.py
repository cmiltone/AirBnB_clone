#!/usr/bin/python3
"""
module for base model class
"""
from typing import Any
import uuid
from datetime import datetime
from models import storage


class BaseModel(object):
    """Underlying model class for the app"""
    def __init__(self, *args, **kwargs):
        """initializes the base model for the app"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.fromisoformat(v))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns string representation of the class"""
        _s = "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                   self.__dict__)
        return _s

    def save(self):
        """sets the updated_at attribute as current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns dictionary containing all keys/values
        of __dict__ of the instance
        """
        _dict = {}
        keys = self.__dict__.keys()
        for key in keys:
            _dict[key] = self.__dict__[key]
        _dict['__class__'] = self.__class__.__name__
        _dict['created_at'] = self.created_at.isoformat()
        _dict['updated_at'] = self.updated_at.isoformat()

        return _dict

    def __setattr__(self, __key, __value):
        if __key != "updated_at":
            # setattr(self, __key, __value)
            self.updated_at = datetime.now()
        super(BaseModel, self).__setattr__(__key, __value)
