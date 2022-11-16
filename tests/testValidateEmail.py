#Unittest suite for EmailAddress class


from src import validate

import unittest

class TestValidateEmail(unittest.TestCase):

    def testNoEmailGiven(self):
        self.assertRaises(Exception, validate, None)

    def testTypeError(self):
        self.assertRaises(TypeError, validate, {})
        self.assertRaises(TypeError, validate, False)
        self.assertRaises(TypeError, validate, [])
        self.assertRaises(TypeError, validate, 1)

    def testValidEmailGiven(self):
        email = "hello@gmail.com"
        checked = validate.validateEmail(email)
        self.assertEqual(checked, "hello@gmail.com")

    def testValidEmailTypoIsNormalized(self):
        email = "hello@gMail.com"
        checked = validate.validateEmail(email)
        self.assertNotEqual(checked, email)

    def testValidEmailSpacesAreNormalized(self):
        email = "hello@g m a i l.com"
        checked = validate.validateEmail(email)
        self.assertNotEqual(checked, email)

    def testNonValidNoAtSymbol(self):
        self.assertRaises(Exception, validate, "hellogmail.com")

    def testNonValidNoUsername(self):
        self.assertRaises(Exception, validate, "@gmail.com")

    def testNonValidNoDomain(self):
        self.assertRaises(Exception, validate, "hello@")

    def testNonValidNoDotCom(self):
        self.assertRaises(Exception, validate, "hello@gmail")

    def testNonValidExtraSymbols(self):
        self.assertRaises(Exception, validate, "hello@@gmail.com")

    def testNonValidAllSymbols(self):
        self.assertRaises(Exception, validate, "#$$@%^&%.23")

    def testNonValidNoSymbols(self):
        self.assertRaises(Exception, validate, "just a string")

if __name__ == '__main__':
   unittest.main()
