import abc
import json
from abc import ABC, abstractmethod
class InterfaceToFile(ABC):
    @abstractmethod
    def filterWebData(self):
        pass

    @abc.abstractclassmethod
    def saveCurrentRequests(self):
        pass

    @abc.abstractclassmethod
    def delete(self):
        pass

    @abc.abstractclassmethod
    def addRequest(self, alertRequest):
        pass

class InterfaceFromFile(ABC):
    @abc.abstractclassmethod
    def updateCampsitesToMonitor(self):
        pass

    def retrieveAlerts(self):
        pass

