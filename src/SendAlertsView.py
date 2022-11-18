
from FileInterface import *

class SendAlertsView():
    def __init__(self, interface: InterfaceFromFile):
        self.interface = interface
        self.alerts = []

    def getAlerts(self):
        self.alerts = self.interface.retrieveAlerts()

    def displayEmails(self):
        self.getAlerts()
        print(f'These emails should receive an alert that their campsites are available: {self.alerts}')


