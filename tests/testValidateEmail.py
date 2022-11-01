#Unittest suite for EmailAddress class


from src import validateEmail

import unittest

class TestValidateEmail(unittest.TestCase):
    def testValidEmailGiven(self):
        email = "hello@gmail.com"
        checked = validateEmail.validateEmail(email)
        self.assertEqual(checked, email)

    def testValidEmailTypoIsNormalized(self):
        email = "hello@gMail.com"
        checked = validateEmail.validateEmail(email)
        self.assertNotEqual(checked, email)

    def testValidEmailSpacesAreNormalized(self):
        email = "hello@g m a i l.com"
        checked = validateEmail.validateEmail(email)
        self.assertNotEqual(checked, email)

    def testNonValidNoAtSymbol(self):
        email = "hellogmail.com"
        checked = validateEmail.validateEmail(email)
        self.assertRaises(Exception)

    def testNonValidNoUsername(self):
        email = "@gmail.com"
        checked = validateEmail.validateEmail(email)
        self.assertRaises(Exception)

    def testNonValidNoDomain(self):
        email = "hello@"
        checked = validateEmail.validateEmail(email)
        self.assertRaises(Exception)

    def testNonValidNoDotCom(self):
        email = "hello@gmail"
        checked = validateEmail.validateEmail(email)
        self.assertRaises(Exception)

    def testNonValidExtraSymbols(self):
        email = "hello@@gmail.com"
        checked = validateEmail.validateEmail(email)
        self.assertRaises(Exception)

    def testNonValidAllSymbols(self):
        email = "#$$@%^&%.23"
        checked = validateEmail.validateEmail(email)
        self.assertRaises(Exception)

    def testNonValidNoSymbols(self):
        email = "just a string"
        checked = validateEmail.validateEmail(email)
        self.assertRaises(Exception)

if __name__ == '__main__':
   unittest.main()
