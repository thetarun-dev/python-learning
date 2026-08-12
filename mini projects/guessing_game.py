
# Mini project - Guessing Game

import random
import os

# Function to generate luck no
def generate_luck_no():
    return random.randint(1,50)

'''

Functin which will hold the game logic

Game logic: game logic is simple, the program will generate a luck no which will be in range of 1 to 50 and 
user need to guess that number, if the user guess number which is low/high program need to output whether they need
lower/guess high no so that they can guess the correct no

'''
def game_logic(lucky_no):
    counter = 0

    while counter >= 0:
        user_no = int(input("Enter your guess: "))

        if user_no not in range(1, 50):
            print("Please enter the number in range of 1 to 50")
            counter += 1
        elif user_no == lucky_no/2:
            print("You are in middle")
            counter += 1
        elif user_no < lucky_no:
            print("You are too low")
            counter += 1
        elif user_no > lucky_no:
            print("You are too high")
        elif user_no == lucky_no:
            print("You guess the luck number")
            break

    return counter

# main
os.system("clear")

print("""\n

------------------------------------------------------------------------
    Hi and Welcome to Guess game - Develop by Tarun Bhandari \n\n

In this game, I will generate a lucky number in range of 1 to 50, and you
have to guess that number.
------------------------------------------------------------------------
""")

lucky_no = generate_luck_no()
steps_taken = game_logic(lucky_no)

if steps_taken < 10:
    print("Magnificent..!, you have guess the number less than 10 steps... \n Great ")
elif steps_taken == 10:
    print("Great..!, you have guess the number in just 10 steps")
elif 10 > steps_taken < 50:
    print("You have need to increase your guessing ability")
else:
    print("Man...!, I am happy that you have guess the number and it take you %d , WOW!... I am amazed buddy.. \nBetter luck next time buddy" %steps_taken)




