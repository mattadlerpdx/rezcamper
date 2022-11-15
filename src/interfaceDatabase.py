import abc
import json
class InterfaceDatabase(abc):
    @abc.abstractclassmethod
    def get(self):
        pass

    @abc.abstractclassmethod
    def put(self):
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

    def put(self, emailToInsert, campsiteToInsert, dateToInsert):
        f = open('data.json')
        data = json.load(f)
        toAppend = {'email': emailToInsert,
                'campsite': campsiteToInsert, 'date': dateToInsert}
        data.append(toAppend)
        outFile = open("data.json", "w")
        json.dump(data, outFile)
    
    def delete(self, emailToFind):
        f = open('data.json')
        data = json.load(f)
        for i, obj in enumerate(data):
            if (obj["email"] == emailToFind):
                listobj.pop(i)
        outFile = open("updated.json", "w")
        json.dump(listobj, outFile)

    def findCampsite(self, campsiteToFind):
        f = open('data.json')
        data = json.load(f)
        for i, obj in enumerate(data):
            if (obj["campsite"] == campsiteToFind):
                return True
            else:
                return False