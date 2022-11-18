
from FileInterface import *
import json


class JsonModel(InterfaceToFile, InterfaceFromFile):
    def __init__(self, filename):
        self.file = filename

    def loadFromFile(self):
        f = open(self.file, 'r')
        data = json.load(f)
        f.close()
        print(data)
        return data

    def dumpToFile(self, data):
        f = open(self.file, 'w')
        json.dump(data, f, indent=4, separators=(',',':'), sort_keys=True)
        f.close()

    def findCampsite(self, campsiteToFind, data):
        location = -1
        index = 0
        for i in data:
            if (i["campsite"] == campsiteToFind):
                location = index
            index += 1
        if(location < 0):
            raise ValueError ("Campsite requested not available in this system to monitor.")
        return location

    def appendRequest(self, alertRequest, location, data):
        data[location]["requests"].append(alertRequest)
        self.dumpToFile(data)

    def addRequest(self, alertRequest):
        data = self.loadFromFile()
        print(data)
        print(alertRequest)
        try:
            index = self.findCampsite(alertRequest["campsite"], data)
            self.appendRequest(alertRequest, index, data)
            return True
        except ValueError:
            print("Could not add this request to the file.")


    #Need to update these when we solidify json formatting
    def getCampsiteEmails(self, campsite, data):
        try:
            location = self.findCampsite(campsite, data)
            emails = data[location]["requests"]["email"]
            return emails
        except ValueError:
            print("Campsite requested not found")

    def retrieveAllEmails(self):
        data = self.loadFromFile()
        allEmails = []
        for i in data:
            if(i["availability"] == "open"):
                allEmails += self.getCampsiteEmails(i["campsite"], data)
        return allEmails
    
    #Update these below to post and put for an entire Campsite object
    def post(self, emailToInsert, campsiteToInsert, dateToInsert):
        f = open(self.file)
        data = json.load(f)
        f.close()
        toAppend = {'email': emailToInsert,
                'campsite': campsiteToInsert, 'date': dateToInsert}
        data.append(toAppend)
        outFile = open("data.json", "w")
        json.dump(data, outFile, indent=2)

    def put(self, emailToInsert, campsiteToInsert, dateToInsert):
        f = open(self.file)
        data = json.load(f)
        f.close()
        toAppend = {'email': emailToInsert,
                'campsite': campsiteToInsert, 'date': dateToInsert}
        data.append(toAppend)
        outFile = open("data.json", "w")
        json.dump(data, outFile)
     
    def delete(self, emailToFind):
        f = open(self.file)
        data = json.load(f)
        f.close()
        for i, obj in enumerate(data):
            if (obj["email"] == emailToFind):
                data.pop(i)
        outFile = open("updated.json", "w")
        json.dump(data, outFile)
     
    def get(self):
        f = open(self.file)
        data = json.load(f)
        f.close()
        for i in data:
            print(i)
   


#JsonModel().get()
#JsonModel().post('test@gmail.com','Olympia','2023-05-21')
#JsonModel().get()
#JsonModel().delete('test@gmail.com')
#JsonModel().get()
#print(JsonModel().findCampsite('Olympia'))


