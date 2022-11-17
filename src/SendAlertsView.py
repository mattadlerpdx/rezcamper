


class SendAlertsView:
    def __init__(self,emails):
        self.emails = emails

    def displayEmails(self):
        print(f'These emails should receive an alert that their campsites are available: {self.emails}')


