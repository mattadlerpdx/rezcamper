# ***File Hierarchy***

```
project
|   app.py
|   README.md
|
|___UI_UX_folder
|   |  index.html
|   |  style.css
|   |
|___database_folder
|       person.db
|       site.db
|       tmp.db
|___App_Engine_Folder    
|   |   site_scraper.py
    |   database_update.py
    |   send_msg.py       
```
### Note: Matt, Tito and Kira wrote this together in a google doc, then moved the text over to this file

# ***Data Flows***

Big Picture:

    User --> Post (Alert Request) --> System --> File

    Web Data --> System --> File

    File --> System --> Alert --> User

Specifics:

#1: Handliing a Post (Request for an Alert)
DATA IN:    Post enters system --> Validate post data --> check if campsite requested by post is in file --> if in file, write email from post to file
DATA OUT:   if campsite from post not in file, send error alert back to that email "Campsite not available to monitor" --> Error Alert leaves system

#2: Updating file with webdata for campsites
DATA IN:    Web Data for Campsites enters system --> file is updated based on web data
DATA OUT:   If any campsite's availability status changes* on an update, retreive emails stored in the file for that campsite --> Send Alerts notifying all emails how the               availability of the Campsite has changed  --> Alerts leave system

*For campsites with no availability status change, no data leaves the system



