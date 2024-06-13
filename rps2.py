# This is the second version of RPS game that aalows the player to play the game again and again using a while loop
import sys
import random
from enum import Enum

#Enum datratype
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

print(RPS(2))
print(RPS.ROCK)
print(type(RPS['ROCK']))
print(RPS.ROCK.value)
# sys.exit()
play_again = True
while play_again:
    print("")
    player_choice = input("Enter \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")
    if 1 > 2:
        print("Do some thing")

    # All user inputs are of type string
    user = int(player_choice)

    if user < 1 or user > 3:
        sys.exit("You must enter 1, 2 or 3")

    computer_choice = random.choice("123")
    python = int(computer_choice)

    print("")
    print("You choose " + str(RPS(user)).replace("RPS.", "") + ".")
    print("Python choose " + str(RPS(python)).replace("RPS.", "") + ".")
    print("")

    if user == 1 and python == 3:
        print("You Win!")
    elif user == 2 and python == 1:
        print("You Win!")
    elif user == 3 and python == 2:
        print("You win !")
    elif user == python:
        print("Tie Game")
    else:
        print("Python Wins")
    play_again = input("\n Y: To Continue\n Q: To Quit\n")
    if play_again == 'y':
        continue
    else:
        print("Thanks for playing! \n Bye !")
        play_again = False
        # break