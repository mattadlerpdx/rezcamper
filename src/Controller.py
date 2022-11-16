
# https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple

from validate import *
from FileInterface import *
import json

class AlertRequest:
    def __init__(self, email, campsite, date):
        self.email = email
        self.campsite = campsite
        self.date = date


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
        except ValueError:
            print("The post is not valid")
        return validPost

    def updateEmail(self, post):
        alertRequest = self.validatePost(post)
        print(alertRequest)
        self.interface.addEmail(alertRequest)



