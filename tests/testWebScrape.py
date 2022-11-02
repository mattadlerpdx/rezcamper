#Unittest suite for EmailAddress class


from src import validateWeb

import unittest

class TestValidateEmail(unittest.TestCase):
    def testValidEmailGiven(self):
        url = 'http://www.mountainproject.com'
        status = validateWeb.CheckStatus(url)
        self.assertEqual(status, 200)

if __name__ == '__main__':
   unittest.main()
