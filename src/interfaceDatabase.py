import abc
import json


class InterfaceDatabase(abc):
    @abc.abstractclassmethod
    def get(self):
        pass

    @abc.abstractclassmethod
    def put(self):
        pass

    @abc.abstractclassmethod
    def post(self):
        pass

    @abc.abstractclassmethod
    def delete(self):
        pass


class InterfaceJson(InterfaceDatabase):
    def get(self):
        f = open('data.json')
        data = json.load(f)
        for i in data['Campsites']:
            print(data)
        f.close()

    def put(self, emailToInsert, campsiteToInsert, dateToInsert):
        f = open('data.json')
        data = json.load(f)
        data['email'] = emailToInsert
        data['campsite'] = campsiteToInsert
        data['date'] = dateToInsert
    
    def post(self, emailToPost, campsiteToPost, dateToPost):
       newPost = {"email": emailToPost,
                  "campsite": campsiteToPost, "date": dateToPost}
       jsonString = json.dumps(newPost)
       jsonFile = open("newJsonFile.json", "w")
       jsonFile.write(jsonString)
       jsonFile.close()
       

    def delete(self, emailToFind):
        f = open('data.json')
        data = json.load(f)
        if (data['email'] == emailToFind):
            data['email'] = None
            data['campsite'] = None
            data['date'] = None

    def findCampsite(self, campsiteToFind):
        f = open('data.json')
        data = json.load(f)
        if (data['campsite'] == campsiteToFind):
            return True
        else:
            return False