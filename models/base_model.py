#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, INTEGER, String, DateTime, MetaData

Base = declarative_base(metadata=MetaData())


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""

        if not kwargs:
            # from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

            if kwargs:
                for key, value in kwargs.items():
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key != "__class__":
                        setattr(self, key, value)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    # def to_dict(self):
    #     """Convert instance into dict format"""
    #     dictionary = {}
    #     dictionary.update(self.__dict__)
    #     dictionary.update({'__class__':
    #                       (str(type(self)).split('.')[-1]).split('\'')[0]})
    #     dictionary['created_at'] = self.created_at.isoformat()
    #     dictionary['updated_at'] = self.updated_at.isoformat()
    #
    #     dictionary.pop('_sa_instance_state', None)
    #     return dictionary
    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)
