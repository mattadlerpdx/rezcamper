import os
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
pass_key = f'https://developer.nps.gov/api/v1/activities?parkCode=or&api_key={api_key}'
HEADERS = {"Authorization":f"{api_key}"}
req = urllib.request.Request(endpoint,headers=HEADERS)
# Additional code would follow

response = urllib.request.urlopen(pass_key).read()
data = json.loads(response.decode('utf-8'))
#print(data['total'])
#print(data['limit'])
#print(data['start'])
count = 0
with open('data_output.json', 'w') as fp:
    for line in data['data']:
        fp.write(json.dumps(line) + '\n')
        print(line)