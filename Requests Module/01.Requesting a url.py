import requests

r = requests.get("https://www.rishendra.com")
print(r.text)
#prints code of the website
with open ("rishendra.html", "w") as myfile:
    myfile.write(r.text)
