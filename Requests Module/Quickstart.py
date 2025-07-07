import requests

r = requests.get("https://api.github.com/events")
'''
status code is a message a website 's server sends to the browser 
to indicate whether or not that request can be fulfilled
'''
#print(r.status_code)
#print(r.encoding)
#print(r.text)
#print(r.json())
print(type(r.json()))
print(r.headers)
print(type(r.headers))