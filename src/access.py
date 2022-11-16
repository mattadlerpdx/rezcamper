import os
import urllib.request
import json
from api_lists import API_METHODS

def formatMethod(method) -> str:
    if '/' in method:
        name = method.replace('/','-')
    else:
        name = method
    return name

def collectParkData():
    '''
        Function: Collects park data
        Uses a data structure from api_lists.py
        and iterates through API Call
        to make api request using. 
        These API Call Names are used 
        to label the JSON File Output
    '''
    api_key = os.environ["NP_API_KEY"]

    for method in API_METHODS:
        # Configure API request
        end_point = f'https://developer.nps.gov/api/v1/{method}?parkCode=or&api_key={api_key}'
        response = urllib.request.urlopen(end_point).read()
        data = json.loads(response.decode('utf-8'))
        name = formatMethod(method)
        with open(f'../json_files/{name}_data.json','w') as fp:
            for line in data['data']:
                fp.write(json.dumps(line) + '\n')

if __name__ == "__main__" :
    collectParkData()