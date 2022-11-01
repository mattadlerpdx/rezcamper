#https: // docs.python.org/3/library/time.html#time.strftime
from datetime import datetime
import unittest


def validateDate(input):
    if type(input) is not str:
        raise TypeError("Input must be string")
        #checks the following input format: day/month/year
    if input != datetime.strptime(input, "%Y-%m-%d").strftime('%Y-%m-%d'):
        print(input)
        raise ValueError("Incorrect format")
    else:
        return input == datetime.strptime(input, "%Y-%m-%d").strftime('%Y-%m-%d')
