#Implementationa of email verification using the email_validator library
#Citation: pypi.org/project/email-validator/

from email_validator import validate_email, EmailNotValidError

class EmailAddress:
    def __init__(self, email):
        self.emailReceived = email;
        self.valid = True;
        self.emailNormalized = ""

    def validateEmail(self):
        try:
            validatedEmail = validate_email(self.emailReceived)
            self.emailNormalized = validatedEmail.email
        except EmailNotValidError as error:
            print(str(error))





