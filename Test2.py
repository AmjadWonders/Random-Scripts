# Done at 10/6/2018. Another username generator."test2" is a good reference that its in the same idea as our old "test".
import random
import os
print("@cokz Usernames Generator!")
print("Your Working directory is " + os.getcwd())
users_to_generate = ("abcdefghijklmnopqrstuvwxyz0123456789_")
i = 0
save = ['']
userinput = int(input("USERS AMOUNT:"))
userinput2 = int(input("Enter The Length of The Username:"))
while userinput != i:
    i = i + 1
    a = random.choices(users_to_generate, k=int(userinput2))
    save += a + '\n'
    print(''.join(a))
user_choice = input("Do You Want To Save it?\n[Y/N} ")
if user_choice == "y":
    file = open("Output.txt", "w")
    file.write(str(save))
    file.close()
    print("Done!")
if user_choice == "n":
    print("Okay Have a Nice Day!")