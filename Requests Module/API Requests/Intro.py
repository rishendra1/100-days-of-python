import requests
import json

Response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
#Output will be a large JSON object that contains the most recently active
# questions on Stack Overflow.
#print(Response.json())
print(Response.json()['items'])
