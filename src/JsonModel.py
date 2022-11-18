
from FileInterface import *
import json


class JsonModel(InterfaceToFile, InterfaceFromFile):
    def __init__(self, filename):
        self.file = filename

    def findCampsite(self, campsiteToFind, data):
        location = -1
        index = 0
        for i in data:
            if (i["campsite"] == campsiteToFind):
                location = index
            index += 1
        return location

    def validateLocation(self, location):
        if location < 0:
            raise ValueError("No valid location in JSON file for requested campsite name.")
        else:
            return True

    def addEmail(self, alertRequest):
        f = open(self.file)
        data = json.load(f)
        f.close()
        location = self.findCampsite(alertRequest["campsite"], data)
        if self.validateLocation(location):
            data[location]["email"].append(alertRequest["email"])
            f = open(self.file, 'w')
            json.dump(data, f, indent=4, separators=(',',':'), sort_keys=True)
            f.close()
        else:
            raise ValueError("Campsite requested not available in this system to monitor.")

    def retrieveEmails(self, campsite, data):
        location = self.findCampsite(campsite, data)
        try:
            self.validateLocation(location)
            emails = data[location]["email"]
            return emails
        except ValueError:
            print("Campsite requested not found")

    def retrieveAllEmails(self):
        f = open(self.file)
        data = json.load(f)
        f.close()
        allEmails = []
        for i in data:
            if(i["availability"] == "open"):
                allEmails += self.retrieveEmails(i["campsite"], data)
        return allEmails
    

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


