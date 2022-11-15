import os
import urllib.request
import json

api_key = os.environ["NP_API_KEY"]
# Configure API request
pass_key = f'https://developer.nps.gov/api/v1/campgrounds?parkCode=or&api_key={api_key}'

response = urllib.request.urlopen(pass_key).read()
data = json.loads(response.decode('utf-8'))

JSON_KEYS = [
    'total',
    'limit',
    'start',
    'data',
]

with open('data_output.json', 'w') as fp:
    for line in data['data']:
        fp.write(json.dumps(line) + '\n')