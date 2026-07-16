import secrets
import string
import pyperclip

name = input("enter name to genarate passaword : ")
num=int(input("enter a number of pass you want : "))
char = "@#$%"
genarate_password = "".join(
    secrets.choice(string.ascii_letters + string.digits + string.punctuation)
    for i in range(num)
)

new_pass = name + genarate_password
print("your password is : ", new_pass)
print ("if you want to copy your password then say yes or no : ")
if input()=="yes":
   pyperclip.copy(genarate_password)
   print("your pass is copied!")
else:
   pass