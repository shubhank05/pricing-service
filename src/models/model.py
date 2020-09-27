from abc import ABCMeta, abstractmethod
from common.database import Database
from typing import Union, Dict
class Model(metaclass=ABCMeta):
    collection: str
    _id: str

    def __init__(self,*args,**kwargs):
        pass
    def save_to_mongo(self):
        Database.update(self.collection, {"_id":self._id}, self.json())
    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id":self._id}, self.json())
    @classmethod
    def get_by_id(cls, _id: str) -> "Model":
        return cls.find_one_by("_id",_id)
    @abstractmethod
    def json(self):
        raise NotImplementedError
    @classmethod
    def all(cls):
        element_from_db = Database.find(cls.collection,{})
        return [cls(**elem) for elem in element_from_db]
    @classmethod
    def find_one_by(cls, attribute, value: Union[str,Dict]):
        return cls(**Database.find_one(cls.collection,{attribute:value}))
    @classmethod
    def find_many_by(cls, attribute, value):
        return [cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]
