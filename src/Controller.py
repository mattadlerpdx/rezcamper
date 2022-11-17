
# https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple

from validate import *
from FileInterface import *


class Controller:
    def __init__(self, interface):
        self.interface = interface

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
            return validPost
        except ValueError:
            print("The post is not valid")
        except EmailNotValidError:
            print("The post is not valid")
        
    def updateEmail(self, post):
        try:
            alertRequest = self.validatePost(post)
            self.interface.addEmail(alertRequest)
            print(f'Your request has been processed. {post["email"]} will recieve an alert if {post["campsite"]} becomes available')
        except ValueError:
            print("Could not create alert request")

    def getEmailsForAlerts(self):
        return self.interface.retrieveAllEmails()



