# rezcamper
This application is implemented with Python/flask for the user interface/api. A json file will be used for the backend storage of campsites we manage requests for.

The current UI is a console based menu. Run ```python3 src/main.py``` from the terminal to run the program.

This repo contains code for a camping reservation application that allows you to put in a request for a campsite you are interested in getting an alert for when a site becomes is available. The application monitors the availability status of campsite information gathered from the National Parks API. (insert link here)

The application checks pulls data from the API and stored in in our internal JSON file. Requests made by users are added to their corresponding campsite JSON object in that internal file. If a campsite in our file shows a status of "available", any requests our application has logged for that campsite will have alerts sent to the email addresses associated. The internal JSON file will not be committed to this repo until we have established some encryption to protect the email address data.

As of now, the email sending functionality is still buggy, and they are not being correctly sent out. but we can verify that the correct emails are being collected.


