import requests
import json

filename = input("Filename > ")
f = open(filename)
usernames = f.readlines()

for username in usernames:
    username = username.strip('\n')
    r = requests.get("https://api.twitter.com/i/users/username_available.json?username=" + str(username))
    jsondata = json.loads(r.text)
    result = jsondata['valid']
    if result == False:
        print("This username is not available | " + str(username))
    elif result == True:
        print("This username is available! | " + str(username))
    elif "rate limit" in r.text:
        print("Rate limit | " + str(username))
