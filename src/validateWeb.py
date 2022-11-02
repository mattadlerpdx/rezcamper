#Implementationa of email verification using the email_validator library
#Citation: pypi.org/project/email-validator/

import requests
import logging

def CheckStatus(url):
    try:
        status = requests.get(url)
        return status.status_code
    except:
        logging.error(f'Error Occured: {logging.ERROR} and status is: {status}')
    


