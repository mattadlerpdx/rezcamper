
from FileInterface import *


class JsonModel(InterfaceToFile, InterfaceFromFile):
    def __init__(self, filename):
        self.file = filename

    def loadFile(self):
        f = open(self.file)
        return json.load(f)
        

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
        #with open(self.file, 'a') as fp:
        f = open(self.file)
        data = json.load(f)
            #location is the index in the list of CAMPSITE json objects in our data.json file
        location = self.findCampsite(alertRequest["campsite"])
        try:
            print("Placeholder for the addEmail function")

                #if self.validateLocation(location):
                    
            data[location]["email"].append(alertRequest["email"])

                #data = self.loadFile()
                #Now we need to get to the "email" key at the campsite at index i, and change it to alertRequest.email
                #add the email to the JSON object at location in data
            print(data)
        except ValueError:
            print("Campsite requested not available in this system to monitor.")

   

    def post(self, emailToInsert, campsiteToInsert, dateToInsert):
        data = self.loadFile()
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
        data = self.loadFile()
        for i in data:
            print(i)
   


#JsonModel().get()
#JsonModel().post('test@gmail.com','Olympia','2023-05-21')
#JsonModel().get()
#JsonModel().delete('test@gmail.com')
#JsonModel().get()
#print(JsonModel().findCampsite('Olympia'))


