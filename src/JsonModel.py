
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
        #with open(self.file, 'a') as fp:
        f = open(self.file)
        data = json.load(f)
        f.close()
        print(data)
        location = self.findCampsite(alertRequest["campsite"], data)
        try:
            print("Placeholder for the addEmail function")
            #if self.validateLocation(location):
            data[location]["email"].append(alertRequest["email"])
            f = open(self.file, 'w')
            json.dump(data, f)
            f.close()
            print(data) #test to see the data is being updated
        except ValueError:
            print("Campsite requested not available in this system to monitor.")

   

    def post(self, emailToInsert, campsiteToInsert, dateToInsert):
        f = open(self.file)
        data = json.load(f)
        f.close()
        toAppend = {'email': emailToInsert,
                'campsite': campsiteToInsert, 'date': dateToInsert}
        data.append(toAppend)
        outFile = open("data.json", "w")
        json.dump(data, outFile)
       

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


