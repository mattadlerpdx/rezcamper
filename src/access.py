import os
import subprocess
import urllib.request
import json

api_key = os.environ.get("NP_API_KEY")
'''
import urllib.request, json
# Configure API request
endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=me"
HEADERS = {"Authorization":str(api_key)}
req = urllib.request.Request(endpoint,headers=HEADERS)

# Execute request and parse response
response = urllib.request.urlopen(req).read()
data = json.loads(response.decode('utf-8'))
# Additional code would follow
'''

import urllib.request, json
# Configure API request
endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=me"
api_key = os.environ.get('NP_API_KEY')
pass_key = f'https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key={api_key}'
HEADERS = {"Authorization":f"{api_key}"}
req = urllib.request.Request(endpoint,headers=HEADERS)
# Additional code would follow

response = urllib.request.urlopen(pass_key).read()
data = json.loads(response.decode('utf-8'))

# Prepare and execute output
print(data["data"][0]["fullName"] + " can be found at " + data["data"][0]["latLong"] + ".")