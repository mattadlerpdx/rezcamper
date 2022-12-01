import os
import sys
import urllib.request
import json
import logging
from api_lists import API_METHODS as ParkFeatures

def formatMethod(method):
    if '/' in method:
        name = method.replace('/','-')
        return name
    return method

class NPSParkData:
    def __init__(self, key):
        self.key = key

    def collectParkData(self):
        """
            Function: Collects park data
            Uses a data structure from api_lists.py
            and iterates through API Call
            to make api request using. 
            These API Call Names are used 
            to label the JSON File Output
        """
        if self.key == None:
            logging.warn("Key has not been set "
                    "Make sure you have proper credentials\n")
            return
        campgrounds = []
        for method in ParkFeatures:
            # Configure API request
            try:
                end_point = f'https://developer.nps.gov/api/v1/{method}?parkCode=or&api_key={self.key}'
                response = urllib.request.urlopen(end_point).read()
                data = json.loads(response.decode('utf-8'))
                name = formatMethod(method)
                with open(f'../json_files/{name}_data.json','w') as fp:
                    for line in data['data']:
                        fp.write(json.dumps(line))
            except:
                logging.error(f"Something went wrong with the API Calls: {logging.ERROR}")
                return
    
    def campInfo(self) -> list:
        """
            collect park info
            based on existing park information
            calls api endpoint and writes 
            json objects in to a list
        """
        campgrounds = []
        try:
            end_point = f'https://developer.nps.gov/api/v1/campgrounds?parkCode=or&api_key={self.key}'
            response = urllib.request.urlopen(end_point).read()
            data = json.loads(response.decode('utf-8'))
            for line in data['data']:
                campgrounds.append(json.dumps(line))
            return campgrounds
        except:
            logging.error(f"Something went wrong with the API Calls: {logging.ERROR}")
            return

                
if __name__ == "__main__" :
    API = os.environ["NP_API_KEY"] if os.environ["NP_API_KEY"] else None
    if API is None:
        logging.error(f"No API Key Set")
        sys.exit()
    NPSData = NPSParkData(API)
    if not os.path.isdir(f'../json_files'):
        NPSData.collectParkData()
    campgrounds = NPSData.campInfo()