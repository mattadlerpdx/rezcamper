#Unittest suite for EmailAddress class

import sys
sys.path.insert(0, 'C:\Users\Kira\Desktop\rezcamper\src')
from src.EmailAddress import *
import unittest

class TestValidateEmail(unittest.TestCase):
    def validEmailGiven(self):
        email = "hello@gmail.com"
        EmailAddress(email)
        EmailAddress.validateEmail()
        self.assertEqual(EmailAddress.emailNormalized, email)


if __name__ == '__main__':
    unittest.main()