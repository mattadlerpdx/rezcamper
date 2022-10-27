#This file contains the implementation for verifying the email address from an incoming post



def oneOrMoreCharacters (toCheck):
    if (len(toCheck) > 0):
        return True
    return False

class Email:
    def __init__(self, address):
        self.fullAddress = address
        self.emailPieces = ()
        self.username = ""
        self.domain = ""
        self.valid = True



    def parseEmail(self):
        emailTuple = self.address.partition("@")
        self.username = emailTuple[0]
        self.domain = emailTuple[2]

    def emailParsedIntoThree(self):
        if(len(self.emailPieces) == 3):
            return True
        return False

    def atSymbolCentered(self):
        if(self.emailPieces[1] == "@"):
            return True
        return False

    def domainIsValid(self):
        if(oneOrMoreCharacters(self.domain)):
            return True
        return False

    def usernameIsValid(self):
        if(oneOrMoreCharacters(self.username)):
            return True
        return False

    def atSymbolPresent(self):
        if("@" in self.fullAddress):
            return True
        return False       

    #eeeehhhhhhhh I hate this function below. How can I make this better?
    def emailAddressIsValid(self):
        if(not self.atSymbolPresent()):
            print("no @ present")
        else:
            self.parseEmail()
            if(not self.emailParsedIntoThree()):
                print("Email incomplete")
            else:
                if(not self.atSymbolCentered()):
                    print("incorrect format")
                else:
                    if(not self.domainIsValid()):
                        print("not enough characters for domain name")
                    else:
                        if(self.usernameisValid()):
                            self.valid = True
                        





