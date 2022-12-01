# rezcamper


This repo contains code for a camping reservation application that allows you to put in a request for a campsite you are interested in getting an alert for when a site becomes is available. The application monitors the availability status of campsite information gathered from the National Parks API. (insert link here)

The application pulls data from the API and stores it in our internal JSON file. Requests made by users are added to their corresponding campsite JSON object in that internal JSON file. If a campsite in our file shows a status of "available", any requests our application has logged for that campsite will have alerts sent to the email addresses associated. The internal JSON file will not be committed to this repo with real email addresses, until we have established some encryption to protect the email address data.

This application is implemented with Python/flask for the user interface/api. A json file will be used for the backend storage of campsites we manage requests for.

The current UI is a console based menu. To run:

  Open two terminals. In the first terminal run this command to enable email results to be viewable in the console:

  ```python -m smtpd -c DebuggingServer -n localhost:1025```

  In the second terminal run

 ```python3 src/main.py``` to run the program.
 
  If you select the option to send emails, you can view the confirmation messages in the first terminal. As of now emails are not actually being sent due to an issue with gmail no longer supports our chosen email server script.
  
  As of 11/30/2022 option 3 on the console menu, to update the campsites we monitor with real webdata, does not work due to a bug in converting our API data file into an iterable list of JSON objects. A fix in being worked on.


