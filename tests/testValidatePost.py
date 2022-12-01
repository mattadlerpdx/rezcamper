
from src import Controller
import unittest


class TestValidatePost(unittest.TestCase):
    def testInvalidEmail(self):
        mockPost = {"email": "hellogmail.com",
                    "date": "02-03-2023", "campsite": "Yellowstone"}
        self.assertRaises(ValueError, Controller.validatePost(mockPost))

    def testValidPost(self):
        mockPost = {"email": "hello@gmail.com",
                    "date": "02-03-2023", "campsite": "Yellowstone"}
        self.assertTrue(Controller.validatePost(mockPost))

    def testNoPostData(self):
        mockPost = {}
        self.assertRaises(ValueError, Controller.validatePost(mockPost))


if __name__ == '__main__':
    unittest.main()
