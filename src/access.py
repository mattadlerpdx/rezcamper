import os
import subprocess
import requests
import urllib.request
import json

api_key = os.environ.get("NP_API_KEY")
endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=me"
HEADERS = {"Authorization":f"{api_key}"}