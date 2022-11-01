#Unittest suite for EmailAddress class


from src import validateEmail

import unittest

class TestValidateEmail(unittest.TestCase):

    def testNoEmailGiven(self):
        self.assertRaises(Exception, validateEmail, None)

    def testTypeError(self):
        self.assertRaises(TypeError, validateEmail, {})
        self.assertRaises(TypeError, validateEmail, False)
        self.assertRaises(TypeError, validateEmail, [])
        self.assertRaises(TypeError, validateEmail, 1)

    def testValidEmailGiven(self):
        email = "hello@gmail.com"
        checked = validateEmail.validateEmail(email)
        self.assertEqual(checked, "hello@gmail.com")

    def testValidEmailTypoIsNormalized(self):
        email = "hello@gMail.com"
        checked = validateEmail.validateEmail(email)
        self.assertNotEqual(checked, email)

    def testValidEmailSpacesAreNormalized(self):
        email = "hello@g m a i l.com"
        checked = validateEmail.validateEmail(email)
        self.assertNotEqual(checked, email)

    def testNonValidNoAtSymbol(self):
        self.assertRaises(Exception, validateEmail, "hellogmail.com")

    def testNonValidNoUsername(self):
        self.assertRaises(Exception, validateEmail, "@gmail.com")

    def testNonValidNoDomain(self):
        self.assertRaises(Exception, validateEmail, "hello@")

    def testNonValidNoDotCom(self):
        self.assertRaises(Exception, validateEmail, "hello@gmail")

    def testNonValidExtraSymbols(self):
        self.assertRaises(Exception, validateEmail, "hello@@gmail.com")

    def testNonValidAllSymbols(self):
        self.assertRaises(Exception, validateEmail, "#$$@%^&%.23")

    def testNonValidNoSymbols(self):
        self.assertRaises(Exception, validateEmail, "just a string")

if __name__ == '__main__':
   unittest.main()
