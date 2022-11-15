import os
import subprocess
import urllib.request
import json

api_key = os.environ.get("NP_API_KEY")
base_url = f'developer.nps.gov/api/v1'
endpoint = "https://developer.nps.gov/api/v1/activities/parks?stateCode=or"
HEADERS = {"Authorization":f"{api_key}"}
req = urllib.request.Request(endpoint,headers=HEADERS)

