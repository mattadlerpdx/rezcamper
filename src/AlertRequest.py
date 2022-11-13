
import validateEmail as e
from src import validateDate as d
from src import validateCampsiteName as c
import json


class AlertRequest:
    def __init__(self, postInfo):
        self.email = postInfo[0]
        self.campsite = postInfo[1]
        self.date = postInfo[2]


# https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple

def validatePost(post):
    try:
        email = e.validateEmail(post["email"])
        campsite = c.validateCampsiteName(post["campsite"])
        date = d.validateDate(post["date"])
    except ValueError:
        print("The post is not valid")
    return (email, campsite, date)


def createAlertRequest(post):
    try:
        postInfo = validatePost(post)
    except ValueError:
        print("Post contains invalid information, Alert Request cannot be created.")
    return AlertRequest(postInfo)


def getPosts(jsonFile):
    return json.loads(jsonFile)


#Run and test in file
def main():
    jsonFile = "../externalFiles/posts.json"
    posts = getPosts(jsonFile)
    alerts = []
    for i in posts:
        alerts.append(createAlertRequest(posts[i]))
    print(alerts)


if __name__ == "__main__":
    main()
