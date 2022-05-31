#handy calc
#Word games/jokes
#a calculation people usually do(like currency exchange), and for that, its got to connect to the internet
#news updates
#weather
#

import time
def say_hi():
    print("Hi there,")
    
say_hi()

time.sleep(3)

print("Welcome, \n Please note that you are expected to answer(write) like this is an OBJ. I'm not so interactive yet. \n")
time.sleep(6)

print("(^_^)")
name: str = input("What's your name?: ")
print("It's nice to meet you, "+ (name[0].upper() + name[1:].lower()))
place: str= input("\nWhere are you from?: ")
print("Okay")
print("\n So, " + (name[0].upper() + name[1:].lower())+ " from " + (place[0].upper() + place[1:].lower()))
fun = input("\nWhat do you do for fun?: ")

time.sleep(3)

print("Thanks For Your Time, " + (name[0].upper() + name[1:]) + ". \nLets try this again some other time.")
print("Now, skidaddle")