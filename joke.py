## This will be an api call to a url for jokes

import requests

url = "https://api.icndb.com/jokes/random"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text + "\n")
print("^Now that's funny.")
