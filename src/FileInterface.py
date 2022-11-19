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
    def addRequest(self, alertRequest):
        pass

class InterfaceFromFile(ABC):
    @abc.abstractclassmethod
    def get(self):
        pass

    def retrieveAlerts(self):
        pass

