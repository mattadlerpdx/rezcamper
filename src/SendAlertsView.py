
from FileInterface import *
import smtplib
from email.mime.text import MIMEText
class SendAlertsView():
    def __init__(self, interface: InterfaceFromFile):
        self.interface = interface
        self.alerts = []

    def getAlerts(self):
        self.alerts = self.interface.retrieveAlerts()

    def displayEmails(self):
        self.getAlerts()
        print(f'These emails should receive an alert that their campsites are available: {self.alerts}')
        sender = 'admin@example.com'
        port = 1025
        msg = MIMEText('testTEXT')
        msg['Subject']= 'You ahve an opening'
        msg['From'] = 'admin@example.com'
        for reciever in self.alerts:
            msg['To'] = reciever
            with smtplib.SMTP('localhost',port) as server:
                server.sendmail(sender,reciever,msg.as_string())
                print('sent to: ', reciever) 


