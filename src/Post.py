from AlertRequestInfo import *

class ProcessPost:

    def __init__(self, post):
        email = post["email"]
        campsite = post["campsite"]
        dates = post[["dates"]]
        valid = False

    def validatePost(self):
        try:
            self.email = validateEmail(self.email)
            #validCampsite
            #validDates
            valid = True
        except:
            print("Error: request information provided is invalid")

    #note: is this a poorly setup function? Since it may or may not create the Alert
    def createAlertIfValid(self):
        try:
            self.validatePost()
            alert = AlertRequestInfo(self.email, self.campstie, self.dates)
            return alert
        except:
            print("Error: could not create Alert, request information provided is not valid")


