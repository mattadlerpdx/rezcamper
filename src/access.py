import os
import urllib.request
import json
from pathlib import Path
from api_lists import API_METHODS

api_key = os.environ["NP_API_KEY"]

for method in API_METHODS:
    # Configure API request
    pass_key = f'https://developer.nps.gov/api/v1/{method}?parkCode=or&api_key={api_key}'
    response = urllib.request.urlopen(pass_key).read()
    data = json.loads(response.decode('utf-8'))
    if '/' in method:
        name = method.replace('/','-')
    else:
        name = method
    with open(f'../json_files/{name}_data.json','w') as fp:
        for line in data['data']:
            fp.write(json.dumps(line) + '\n')