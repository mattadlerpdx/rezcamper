import abc
import json
from abc import ABC, abstractmethod
class InterfaceToFile(ABC):
    @abstractmethod
    def put(self):
        pass

    @abc.abstractclassmethod
    def post(self):
        pass

    @abc.abstractclassmethod
    def delete(self):
        pass

    @abc.abstractclassmethod
    def addEmail(self, alertRequest):
        pass

class InterfaceFromFile(abc):
    @abc.abstractclassmethod
    def get(self):
        pass

