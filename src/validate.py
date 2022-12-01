# Implementationa of email verification using the email_validator library
# Citation: pypi.org/project/email-validator/
#https: // docs.python.org/3/library/time.html#time.strftime


#from email_validator import validate_email, EmailNotValidError
from datetime import datetime
import unittest


def validateEmail(emailReceived):
    try:
        validatedEmail = validate_email(emailReceived)
        return str(validatedEmail.ascii_email)
    except EmailNotValidError as error:
        print(str(error))



def validateDate(input):
    if type(input) is not str:
        raise TypeError("Input must be string")
        #checks the following input format: day/month/year
    if input != datetime.strptime(input, "%Y-%m-%d").strftime('%Y-%m-%d'):
        print(input)
        raise ValueError("Incorrect format")
    else:
        return input == datetime.strptime(input, "%Y-%m-%d").strftime('%Y-%m-%d')

def validateCampsiteName(name):
    if type(name) is not str:
        raise TypeError("Campsite name requested is in the wrong format, string expected")
    if(name.isspace()):
        raise TypeError("Campsite nae requested must not be blank")
    if(name.isnumeric()):
        raise TypeError("Campsite name requested can not be all numbers")
    return name
