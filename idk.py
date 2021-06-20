# Done at 12/6/2018 5:47. what was I thinking?
import os
words = ('hi\n'*5000)
try:
    file = open('passwords.txt','w')
    file.write(words)
    file.close()
    print("Done!")
except:
    print('Sorry There was an Error!')
