import os
import urllib.request
import json
from pathlib import Path
from api_lists import JSON_KEYS, API_METHODS

api_key = os.environ["NP_API_KEY"]
HOME = os.environ['HOME']

# Configure API request
pass_key = f'https://developer.nps.gov/api/v1/campgrounds?parkCode=or&api_key={api_key}'

response = urllib.request.urlopen(pass_key).read()
data = json.loads(response.decode('utf-8'))

#with open('data_output.json', 'w') as fp:
for method in API_METHODS:
    with open(f'../json_files/{method}_data.json','w') as fp:
        for key in JSON_KEYS:
            for line in data[key]:
                fp.write(json.dumps(line) + '\n')