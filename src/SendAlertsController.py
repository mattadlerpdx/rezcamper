from FileInterface import *
import smtplib
import ssl
#rezcamperpdx@gmail.com
#password: tkmleblanc

class SendAlertsController():
    def __init__(self, interface: InterfaceFromFile):
        self.interface = interface
        self.alerts = []

    def getAlerts(self):
        self.alerts = self.interface.retrieveAlerts()

    def sendEmails(self):
        self.getAlerts()
        port = 587  # For starttls
        smtpServer = "rezcamperpdx@gmail.com"
        senderEmail = "my@gmail.com"
        password = "tkmleblanc"
        message = """\Subject: testing EmailAlertScript."""
        context = ssl.create_default_context()
        with smtplib.SMTP(smtpServer, port) as server:
            for emailAddress in self.alerts:
                server.starttls(context=context)
                server.login(senderEmail, password)
                server.sendmail(senderEmail, emailAddress, message)

