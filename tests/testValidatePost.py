
from src import ReceivePost as r
import unittest


class TestValidatePost(unittest.TestCase):
    def testInvalidEmail(self):
        mockPost = {"email": "hellogmail.com",
                    "date": "02-03-2023", "campsite": "Yellowstone"}
        mockReceivePost = r.ReceivePost(mockPost)
        self.assertRaises(ValueError, mockReceivePost.validatePost)

    def testValidPost(self):
        mockPost = {"email": "hello@gmail.com",
                    "date": "02-03-2023", "campsite": "Yellowstone"}
        mockReceivedPost = r.ReceivePost(mockPost)
        mockReceivedPost.validatePost()
        self.assertTrue(mockReceivedPost.valid)


if __name__ == '__main__':
    unittest.main()
