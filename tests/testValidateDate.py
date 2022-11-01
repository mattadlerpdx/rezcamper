
import unittest
from src import validateDate


class TestValidateDate(unittest.TestCase):

    def testTypeError(self):
        self.assertRaises(TypeError, validateDate, None)
        self.assertRaises(TypeError, validateDate, {})
        self.assertRaises(TypeError, validateDate, False)
        self.assertRaises(TypeError, validateDate, [1, 2])

    def testTrue(self):
        self.assertTrue(validateDate("1994-11-05"))

    def testValueError(self):
        self.assertRaises(ValueError, validateDate, "1994/11/05")
        self.assertRaises(ValueError, validateDate, "1994 11 05")


if __name__ == '__main__':

    unittest.main()
