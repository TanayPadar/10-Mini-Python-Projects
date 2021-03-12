#Project by :- Junior Programmer / Tanay Padar
#Channel Link :- https://tinyurl.com/1smu75d8
#Channel Name :- Junior Programmer 

#Install Modules
import random

#Asking For Username/Input
generatorotp=random.randint(000000,100000)
username= input ("Username:")
print ('Hello...!',username)

#Mainloop
print('Here is your OTP for login',generatorotp)
password=input("Enter the OTP to Login:")
if password==str(generatorotp):
    print ('Login Success!!')
else:
    password!= str(generatorotp)
    print('Login Failed')