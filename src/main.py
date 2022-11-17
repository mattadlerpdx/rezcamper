from FileInterface import *
from Controller import *
from SendAlertsView import *
from JsonModel import *

def main():
    campsiteDataFile = "src/campsitesToMonitor.json"
    #toFile = InterfaceToFile()
    model = JsonModel(campsiteDataFile)
    controller = Controller(model) #This isn't right, passing the model to the Controller...
    
    makeSelection = True
    while(makeSelection):
        selection = int(input("Type 1 to make a request, Type 2 to see all emails that need to receive alerts, Type 0 to quit: "))
        if selection == 1:
            mockPost = controller.getPostAsInput()
            controller.updateEmail(mockPost)
        elif selection == 2:
            emails = controller.getEmailsForAlerts()
            sendAlerts = SendAlertsView(emails)
            sendAlerts.displayEmails()
        elif selection == 0:
            makeSelection = False
        else:
            print("That was not a valid selection, please try again.")
    

if __name__ == "__main__":
    main()
