
import random

answer = random.randint(1,100)

done = False

while not done:
    number = float(raw_input("Please enter your guess (0-100): "))
    if number > answer :
        print("Your guess is too big")
    elif number < answer :
        print("Your guess is too small")
    else :
        print("You are correct")
        done = True
