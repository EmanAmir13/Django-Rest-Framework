import json

import requests

# URL = "http://127.0.0.1:8000/api/v1/student-info/2"
#
# r = requests.get(url=URL)
# data = r.json()
#
# print(data)

URL = "http://127.0.0.1:8000/api/v1/student-create/"
data = {
    'name': 'Mahnoor',
    'roll_no': 14,
    'city': 'KPK'
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
