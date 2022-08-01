"""
projekt_2_(2): Druhá varianta druhého projektu do ENGETO Online Akademie

Author: Lukáš Horák
email: tatranka520@gmail.com
discord: Vypyx#2641
"""

import random
import time
print("Hello there")

print("-" * 50)
time.sleep(1)
print("Let's play a game of Mastermind")
time.sleep(1)
print("You will have to guess a randomly generated \n4 digit number")
time.sleep(1)
print("You have 10 attempts to guess the number")
time.sleep(1)
input("Press ENTER to continue...")
print("-" * 50)
random.seed()
answer = ""
answer = str(random.randrange(1000, 9999))
answer.split()
winratings = {
    0: "win1",
    1: "win1",
    2: "win1",
    3: "win2",
    4: "win2",
    5: "win2",
    6: "win3",
    7: "win3",
    8: "win3",
    9: "win4",
    "win1": "Amazing, you did perfectly. \nThe number was: ",
    "win2": "Good job, you did well. \nThe number was: ",
    "win3": "Good job, could be better though. \nThe number was: ",
    "win4": "That was close, try harder next time. \nThe number was: "
    }
for i in range(10):
    guess = input("Take a guess (4 digits): ")
    guess.split()
    inCorrectPos = 0
    inWrongPos = 0
    for k in range(4):
        if answer[k] == guess[k]:
            inCorrectPos += 1
            continue
        for l in range(4):
            if answer[k] == guess[l]:
                inWrongPos += 1
                break
    if inCorrectPos == 4:
        print("-" * 50)
        print(winratings[winratings[i]] + answer[0] + answer[1] + answer[2] + answer[3])
        time.sleep(2)
        quit(0)
    print("In correct position - " + str(inCorrectPos) + " - In wrong position - " + str(inWrongPos))
print("-" * 50)
print("So close, yet so far. \nThe answer was: " + answer[0] + answer[1] + answer[2] + answer[3] + "\nBetter luck next time.")
