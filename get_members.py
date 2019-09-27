import os
import sys

import requests
import json

# get api-key 
token = sys.argv[1]
headers = {"X-API-Key": token}

END_POINT = 'https://eactivities.union.ic.ac.uk/API/CSP'

# get society code
response = requests.get(END_POINT, headers=headers)
society_code = json.loads(response.text)[0]['Code']
print(society_code)

# get members 
year = '19-20'
members_url = os.path.join(END_POINT, society_code, 'reports', 'members?year={}'.join(year))
response = requests.get(members_url, headers=headers)
print(json.loads(response.text))
