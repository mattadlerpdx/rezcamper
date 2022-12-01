import unittest
from src import JsonModel
from src import FileInterface

class TestLoadFromFile(unittest.TestCase):
    def testNoFile(self):
        file = ""
        model = JsonModel.JsonModel(file)
        self.assertRaises(Exception, model.loadFromFile, file)

if __name__ == '__main__':
   unittest.main() 