
from FileInterface import *


class JsonModel(InterfaceToFile, InterfaceFromFile):
    def __init__(self, filename):
        self.file = filename

    def loadFile(self):
        f = open(self.file)
        return json.load(f)
        f.close()

    def findCampsite(self, campsiteToFind):
        data = self.loadFile()
        location = -1
        count = 0
        for i in data:
            if (i["campsite"] == campsiteToFind):
                location = count
            count += 1
        return location

    def validateLocation(self, location):
        if location < 0:
            raise ValueError("No valid location in JSON file for requested campsite name.")
        else:
            return True

    def addEmail(self, alertRequest):
        #location is the index in the list of CAMPSITE json objects in our data.json file
        location = self.findCampsite(alertRequest["campsite"])
        try:
            print("Placeholder for the addEmail function")

            print(self.validateLocation(location))
            #data = self.loadFile()
            #Now we need to get to the "email" key at the campsite at index i, and change it to alertRequest.email
            #add the email to the JSON object at location in data

        except ValueError:
            print("Campsite requested not available in this system to monitor.")

    def post(self, emailToInsert, campsiteToInsert, dateToInsert):
        f = open('data.json')
        data = json.load(f)
        toAppend = {'email': emailToInsert,
                'campsite': campsiteToInsert, 'date': dateToInsert}
        data.append(toAppend)
        outFile = open("data.json", "w")
        json.dump(data, outFile)

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
                data.pop(i)
        outFile = open("updated.json", "w")
        json.dump(data, outFile)

    def get(self):
        f = open('data.json')
        data = json.load(f)
        for i in data:
            print(i)
            f.close()


#JsonModel().get()
#JsonModel().post('test@gmail.com','Olympia','2023-05-21')
#JsonModel().get()
#JsonModel().delete('test@gmail.com')
#JsonModel().get()
#print(JsonModel().findCampsite('Olympia'))


