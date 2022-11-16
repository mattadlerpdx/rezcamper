
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
        post["Campsite"] = input("Enter campsite name: ")
        post["Date"] = input ("Enter date: ")
        return post

    def validatePost(self, post):
        try:
            email = validateEmail(post["email"])
            campsite = validateCampsiteName(post["campsite"])
            date = validateDate(post["date"])
        except ValueError:
            print("The post is not valid")
        return AlertRequest(email, campsite, date)

    def updateEmail(self, post):
        alertRequest = self.validatePost(post)
        self.interface.addEmail(alertRequest)



