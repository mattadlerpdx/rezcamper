
import unittest
from src.validateDate import validateDate


class TestValidateDate(unittest.TestCase):

    def testTypeError(self):
        self.assertRaises(TypeError, validateDate.validateDate, None)
        self.assertRaises(TypeError, validateDate.validateDate, {})
        self.assertRaises(TypeError, validateDate.validateDate, False)
        self.assertRaises(TypeError, validateDate.validateDate, [1, 2])

    def testTrue(self):
        self.assertTrue(validateDate.validateDate("1994-11-05"))

    def testValueError(self):
        self.assertRaises(ValueError, validateDate.validateDate, "1994/11/05")
        self.assertRaises(ValueError, validateDate.validateDate, "1994 11 05")


if __name__ == '__main__':

    unittest.main()
