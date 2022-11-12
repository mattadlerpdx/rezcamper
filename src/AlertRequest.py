from src import AlertRequestInfo as a
from src import validateEmail as e
from src import validateDate as d


class ReceivePost:

    def __init__(self, post):
        self.email = post["email"]
        self.campsite = post["campsite"]
        self.dates = post["date"]
        self.valid = False

    def validatePost(self):
        try:
            self.email = e.validateEmail(self.email)
            # validCampsite will be called here
            self.valid = d.validateDate(self.dates)
        except ValueError:
            print("The post is not valid")
        self.valid = True

    def createAlert(self):
        try:
            self.validatePost()
            alert = a.AlertRequestInfo(self.email, self.campsite, self.dates)
            return alert
        except:
            print(
                "Error: could not create Alert")
