
from FileInterface import *


class JsonModel(InterfaceToFile, InterfaceFromFile):
    def __init__(self, filename):
        self.file = filename

    def loadFile(self):
        f = open(self.filename)
        return json.load(f)

    def findCampsite(self, campsiteToFind):
        data = self.loadFile()
        location = -1
        for i, obj in enumerate(data):
            if (obj["campsite"] == campsiteToFind):
                location = i
        return location

    def validateLocation(self, location):
        if location < 0:
            raise ValueError("No valid location in JSON file for requested campsite name.")
        else:
            return True

    def addEmail(self, alertRequest):
        location = self.findCampsite(alertRequest.campsite)
        try:
            self.validateLocation(location)
            data = self.loadFile()
            print("Placeholder for the addEmail function")
            #add the email to the JSON object at location in data

        except ValueError:
            print("Campsite requested not available in this system to monitor.")


    def put(self, emailToInsert, campsiteToInsert, dateToInsert):
        data = self.loadFile()
        toAppend = {'email': emailToInsert,
                'campsite': campsiteToInsert, 'date': dateToInsert}
        data.append(toAppend)
        outFile = open("data.json", "w")
        json.dump(data, outFile)
    
    def delete(self, emailToFind):
        data = self.loadFile()
        for i, obj in enumerate(data):
            if (obj["email"] == emailToFind):
                listobj.pop(i)
        outFile = open("updated.json", "w")
        json.dump(listobj, outFile)

    def get(self):
        f = open('data.json')
        data = json.load(f)
        for i in data:
            print(i)
            f.close()

