
Incoming data to the system will be received as a JSON dictionary with the following key/value pairs:

{
    email: "myEmail@email.com"
    campsiteName: "selected site name"
    datesToMonitor: dates[]
}

Email address will be received as a string data type. To be valid it must have at least one character before the '@' symbol. and characters that surround the '.' symbol that appear after the '@' symbol. 

Campsite name will be received as a string data type, and can contain any number of characters, including spaces.

Dates to monitor will be held in a list of dates in the range the user wishes to get availability information for the selected campsite from.