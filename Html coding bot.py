# Done at 12/25/2018 8:23 PM. Now, this is a pretty creative one. I had this beautiful idea while showering to create a python script that codes HTML code for you. Nice one.
startd = input("Enter a Title Name: ")
pinput = input("Enter a Paragraph: ")
pinput2 = input("Enter other paragraph: ")
choice = input("want to Enter other Paragraph ?")
start = ("<html>\n")
end = ("</html>")
head = ("<head>\n")
ehead = ("</head>\n")
body = ("<body>\n")
ebody = ("</body>\n")
para = ("<p>")
epara = ("</p>\n")
title = ("<title>")
etitle = ("</title>\n")
def html():
    html = ""
    if len(startd) > 1:
        html += start
        html += head
        html += title + startd + etitle
        html += ehead
        html += body
        html += para + pinput + epara
        if choice == "":
            print(pinput2)
            html += para + pinput2 + epara
            html += body
        else:
            html += body
        print(html)
html()


