
from FileInterface import *
from access import *
import json

class JsonModel(InterfaceToFile, InterfaceFromFile):
    def __init__(self, campsitesToMonitor, key):
        self.file = campsitesToMonitor
        self.webKey = key

#### UTILITY FUNCTIONS ####

    def loadFromFile(self):
        f = open(self.file, 'r')
        data = json.load(f)
        f.close()
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

    def delete(self, emailToFind):
        data = self.loadFromFile()
        for i, obj in enumerate(data):
            if (obj["email"] == emailToFind):
                data.pop(i)
        outFile = open("updated.json", "w")
        json.dump(data, outFile)

### REQUEST PROCESSING #####

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

### ALERTS PROCESSING ###
    
    def retrieveAlerts(self):
        data = self.loadFromFile()
        allEmails = []
        for campsite in data:
            if(self.siteAvailable(campsite)):
                allEmails += self.getAvailableSiteEmails(campsite)
        return allEmails

    def getAvailableSiteEmails(self, campsite):
        emails = []
        for request in campsite["requests"]:
            emails.append(request["email"])
        return emails

    def siteAvailable(self, campsite):
        if(campsite["availability"] == "open"):
            return True
        return False

### WORKING WITH THE WEBSCRAPING DATA #####

    def getWebData(self):
        parkAPI = NPSParkData(self.webKey)
        webData = parkAPI.campInfo()
        return webData

    def filterWebData(self):
        #### temporary link to test file, call getWebData() when JSON bug fixed
        f = open("src/testWebFile.json", 'r')
        sites = json.load(f)
        f.close()
        ####
        data = []
        for camp in sites:
            singleSite = {"campsite":"", "availability":"", "requests":[]}
            singleSite["campsite"] = camp["name"]
            if camp["reservationUrl"]:
                singleSite["availability"] = "open"
            else:
                singleSite["availability"] = "closed"
            data.append(singleSite)
        return data

    def saveCurrentRequests(self, data):
        sitesMonitored = self.loadFromFile()
        for monitored in sitesMonitored:
            for site in data:
                if monitored["campsite"] == site["campsite"]:
                    site["requests"] = monitored["requests"]
        return data
    
    def updateCampsitesToMonitor(self):
        webData = self.filterWebData()
        toDump = self.saveCurrentRequests(webData)
        self.dumpToFile(toDump)
            
    


