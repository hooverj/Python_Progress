from random import *

print("Welcome to Jordan's AMAZING compliment machine.")
print("---------------------------")
name = input('What is your name?:')
compliments = [ "you are excellent and above average." , "good going on being so great all the time." , "your outfit really brings out your eyes." , "you are looking lovely today." , "are you pregnant? Cuz you're glowing ;).", "Do you have car insurance? Cuz I wanna hit it from the back." ]
print("Dear", name)
print(choice(compliments))
