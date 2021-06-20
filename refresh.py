# done at 10/22/2018 9:09 PM. this was done when I was pretty amazed by the branch of cybersecurity, I tried using python to solve one of the CTF Competetions.

import urllib.request
captcha = "ndkankd8"
while True:
    r = urllib.request.urlopen("http://ctf.slothparadise.com/walled_garden.php?name=d&captcha=" + captcha).read()
    b = r.split(b"<pre>")
    c = b[1].split(b"</pre>")
    d = c[0]
    captcha = (d.decode("ascii"))
    
