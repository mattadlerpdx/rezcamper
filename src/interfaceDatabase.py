import abc
import json
from abc import ABC, abstractmethod
class InterfaceDatabase(ABC):
    @abstractmethod
    def get(self):
        pass

    @abc.abstractclassmethod
    def post(self):
        pass

    @abc.abstractclassmethod
    def delete(self):
        pass
    
class InterfaceJson(InterfaceDatabase):
    def get(self):
        f = open('data.json')
        data = json.load(f)
        for i in data:
            print(i)
            f.close()

    def post(self, emailToInsert, campsiteToInsert, dateToInsert):
        f = open('data.json')
        data = json.load(f)
        toAppend = {'email': emailToInsert,
                'campsite': campsiteToInsert, 'date': dateToInsert}
        data.append(toAppend)
        outFile = open("data.json", "w")
        json.dump(data, outFile)
    
    def delete(self, emailToFind):
    #this function deletes json obj from array of json objs
        f = open('data.json')
        data = json.load(f)
        for i, obj in enumerate(data):
            if (obj["email"] == emailToFind):
                data.pop(i)
        outFile = open("updated.json", "w")
        json.dump(data, outFile)

    def findCampsite(self, campsiteToFind):
        f = open('data.json')
        data = json.load(f)
        for i in data:
            if(i["campsite"] == campsiteToFind):
                print(i)
            else:
                f.close()

           
            
            
       

#InterfaceJson().get()
#InterfaceJson().post('test@gmail.com','Olympia','2023-05-21')
#InterfaceJson().get()
#InterfaceJson().delete('test@gmail.com')
#InterfaceJson().get()
#print(InterfaceJson().findCampsite('Olympia'))
