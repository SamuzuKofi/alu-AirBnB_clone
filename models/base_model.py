import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    __abstract__ = True

    id = Column(String(60), primary_key=True,
                     default=lambda:str(uuid.uuid4()))
    created_at = Column(DateTime,
                        default=datetime.utcnow)
    updated_at = Column(DateTime,
                        default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
            """Initialize BaseModel"""
            if kwargs:
                for key, val in kwargs.items():
                    if key == '__class__':
                        continue
                    if key in ('created_at', 'updated_at') and isinstance(val, str):
                        val = datetime.fromisoformat(val)
                    setattr(self, key, val)
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.utcnow()
                self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary