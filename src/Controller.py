
# https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple

from validate import *
from interfaceDatabase import *
import json

class AlertRequest:
    def __init__(self, email, campsite, date):
        self.email = email
        self.campsite = campsite
        self.date = date


class Controller:
    def __init__(self):
        self.toJson = InterfaceToJson()

    def validatePost(self, post):
        try:
            email = validateEmail(post["email"])
            campsite = validateCampsiteName(post["campsite"])
            date = validateDate(post["date"])
        except ValueError:
            print("The post is not valid")
        return AlertRequest(email, campsite, date)

    def getPosts(jsonFile):
        return json.loads(jsonFile)

    def updatetModelWithPost(self, post):
        
        alertRequest = self.validatePost(post)
        self.toJson.addEmail(alertRequest)




#Run and test in file
def main():
    mock = Controller()
    mockPosts = "../externalFiles/posts.json"
    posts = mock.getPosts(mockPosts)
    alerts = []
    for i in posts:
        alerts.append(mock.validatePost(posts[i]))


if __name__ == "__main__":
    main()
