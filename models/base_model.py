#!/usr/bin/python3
"""
module for base class
"""
import uuid
from datetime import datetime


class BaseModel:
    """Underlying model class for the app"""
    def __init__(self):
        """initializes the model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns string representation of the class"""
        return "[{}] {} {}".format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        """sets the updated_at attribute as current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns dictionary containing all keys/values
        of __dict__ of the instance
        """
        _dict = {}
        keys = self.__dict__.keys()
        for key in keys:
            _dict[key] = self.__dict__[key]
        _dict['__class__'] = BaseModel.__name__
        _dict['created_at'] = self.created_at.isoformat()
        _dict['updated_at'] = self.updated_at.isoformat()
        
        return _dict