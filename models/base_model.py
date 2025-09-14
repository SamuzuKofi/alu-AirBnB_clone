import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


class BaseModel:

    id = Column(String(60), primary_key=True,
                     default=str(uuid.uuid4()))
    created_at = Column(DateTime,
                        default=datetime.utcnow())
    updated_at = Column(DateTime,
                        default=datetime.utcnow())

    def __init__(self):
        pass

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



def add(x,y):
        return x + y
def subtract(x,y):
        return x - y
def multiply(x,y):
        return x * y
def divide(x,y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
def modulus(x,y):
        return x % y
def power(x,y):
        return x ** y