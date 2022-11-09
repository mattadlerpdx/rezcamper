#Implementationa of email verification using the email_validator library
#Citation: pypi.org/project/email-validator/

from email_validator import validate_email, EmailNotValidError


def validateEmail(emailReceived):
    try:
        validatedEmail = validate_email(emailReceived)
        return str(validatedEmail.ascii_email)
    except EmailNotValidError as error:
        print(str(error))
    