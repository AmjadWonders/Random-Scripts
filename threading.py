# Done at 11/17/2018. this is pretty epic I would say, such a good waste of time.
import os
def a(data, age):
    return "Hi " + data + "\n" + "You are " + age + " years old" + "\n"
l = ''
while True:
    data = input("Enter name: ")
    age = input("Enter age: ")
    print(data)
    c = [data, age]
    b = a(data, age)
    print(b)
    l += "Name: " + data + " , " + "Age: " + age
    file = open("Students", "w")
    file.write(l)
file.close()