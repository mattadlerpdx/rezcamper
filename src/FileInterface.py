import abc
import json
class InterfaceToFile(abc):
    @abc.abstractclassmethod
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

