# Done at 3/3/2019 10:55 PM. Now, this one is used to find the number of subscribers of a youtube channel using the Library "requests"

import urllib.request
import json

name=("klauskkpm")
key = "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"

data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key).read()
subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

print(name + " has " + "{:,d}".format(int(subs)) + " subscribers!🎉")

# Pretty creative I would say.