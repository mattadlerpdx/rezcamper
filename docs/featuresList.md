## 1. USER INTERACTION FEATURES: Stretch Goals 
	-	User selects a campsite to monitor 
		- our app will offer a menu of campsites we monitor that the person using it can select from. 
		-	User searches for a campsite to monitor - it would be great if the person using the app could quickly search via keyword to see if a campsite they are interested in is included in our database, then choose to select it 
	-	User searches for type of campsite and set of type gets monitored 
	-	User selects the dates they wish to monitor - a person should be able to select a specific date window for the campsite they selected. This could be selected from a calendar selection tool or they could enter the dates directly. 
	-	User narrows down which type of campsite they want an alert for: tent, yurt, RV, etc 
		-	User enters information - Once a campsite location has been selected, the person should be able to provide the e-mail address where they want to receive a status alert. We would gather this email information through a submittable form. It would also be nice to get their name so we could personalize the outgoing e-mail alert. 
	-	get /post/delete user email from DB(taken from UI, our website)
	-	Store user information 
		- Keep track of each user’s data for each request: name, email, campsite requested to monitor, dates requested to monitor 
	-	Update user information 
		- if user decides to change dates/locations, our app allows them to change their current request 
	-	Send status change alert to user 
		- if a site opens (changes status from filled to reservable), the app immediately sends an e-mail to each user that has made a request on that site, for those dates. 
	- Sends recommendations based on sites User is interested in 
 
 
### ***DATA GATHERING FEATURES*** 
	-	Get campsite information from a campsite reservation site (like KOA, fs.usda.gov, NPS.gov) - regularly scrape data from an existing reservation site, providing a snapshot of all the sites availability status’s. 
	-	get/ post /delete reservation dates and availability status info (scrape from website) 
	-	15 minute freshness 
	-	Push Recommendations based on what’s available 
	-	Push alerts when reserved sites are available
### ***DATA STORAGE FEATURES***
	-	Store user information in a database - maintain objects for each user who has made a request:
		-	Add new user 
		-	Delete existing user
		-	Update user
		-	Store Campsite data in database - as we scrape campsite availability, update a database with campsites availability status for each date. To do this we need the following features:
		-	Retrieve campsite
	-	Update campsites availability status 
	-	Update our database of campsites the app monitors - expand the number of campsites we offer monitoring and alert send outs on. Initially we will start this out super small with just a handful of sites, but want it to be scalable for the future, ideally one day including all campsites in a specific area. To do this we better be able to:
	-	Add new campsite location
	-	Delete existing campsite location
	-	Update campsite information
	-	Stretch: Monitor weather related events (Fires, Storms, Closures, etc.)
