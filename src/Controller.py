
# https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple

from validate import *
from FileInterface import *
from SendAlertsView import *
from JsonModel import *


class Controller:
    def __init__(self, campsiteDataFile):
        self.campsiteDataFile = campsiteDataFile
        self.model = JsonModel(campsiteDataFile)
        self.alertView = SendAlertsView(self.model)

    def consoleMenu(self):
        makeSelection = True
        while(makeSelection):
            selection = int(input("Type 1 to make a request, Type 2 to see all emails that will receive alerts, Type 0 to quit"))
            if selection == 1:
                mockPost = self.getPostAsInput()
                self.sendRequestToModel(mockPost, self.model)
            elif selection == 2:
                self.alertView.displayEmails()
            elif selection == 0:
                makeSelection = False
            else:
                print("That was not a valid selection, please try again")

    #placeholder until the UI is set up
    def getPostAsInput(self):
        post = {}
        post["email"] = input("Enter email: ")
        post["campsite"] = input("Enter campsite name: ")
        post["date"] = input ("Enter date: ")
        return post

    def validatePost(self, post):
        validPost = {}
        try:
            validPost["email"] = validateEmail(post["email"])
            validPost["campsite"] = validateCampsiteName(post["campsite"])
            if validateDate(post["date"]):
                validPost["date"] = post["date"]
            return True
        except ValueError:
            print("The post is not valid")
        except EmailNotValidError:
            print("The post is not valid")
        
    def sendRequestToModel(self, post, interface: InterfaceToFile):
        try:
            if self.validatePost(post):
                if(interface.addRequest(post)):
                    print(f'Your request has been processed. {post["email"]} will recieve an alert if {post["campsite"]} becomes available')
        except ValueError:
            print("Could not create alert request, no request processed")

 



