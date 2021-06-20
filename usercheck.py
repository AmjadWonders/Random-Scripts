# Done at 7/21/2018 12:41. this checks the availability for usernames. you should add a list.text file containing the list of usernames generated for it to work.
# You can generate the usernames from my username generator ;)
import os
import sys
import requests
available = 0
unavailable = 0
aavailable = ("")
space = ('\n')
print("Instagram Username Availabitiy Checker")

baseURL = ("https://www.instagram.com/")
# file handle fh
f = open('list.txt', 'r')
for word in f:
    for word in word.split():
        print(word)
        newurl = (baseURL + word)
        print("checking availability")
        r = requests.get(newurl)
        if r.status_code == 404:
            aavailable += space
            aavailable += word
            print("**Username Available**")
            available += 1
            print(available, "available", unavailable, "unavailable")
        else:
            print("**Account Already Exists**")
            unavailable += 1
            print(available, "available", unavailable, "unavailable")
            print(" ")
print("Available:", aavailable)
