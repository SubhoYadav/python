# This is the fourth version of RPS game that implements a feature to keep the track of how many times the game is played
import sys
import random
from enum import Enum

game_count = 0
def play_again_function():
    #Enum datratype
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(type(RPS['ROCK']))
    # print(RPS.ROCK.value)
    # sys.exit()
    player_choice = input("Enter \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

    # All user inputs are of type string
    if player_choice not in ["1","2","3"]:
        print("You must enter 1, 2 or 3")
        play_again_function()

    user = int(player_choice)

    computer_choice = random.choice("123")
    python = int(computer_choice)

    print("")
    print("You choose " + str(RPS(user)).replace("RPS.", "") + ".")
    print("Python choose " + str(RPS(python)).replace("RPS.", "") + ".")
    print("")

    def decide_result(user, python):
        if user == 1 and python == 3:
            return "You Win!"
        elif user == 2 and python == 1:
            return "You Win!"
        elif user == 3 and python == 2:
            return "You win !"
        elif user == python:
            return "Tie Game"
        else:
            return "Python Wins"
    
    game_result = decide_result(user, python)
    print(game_result)

    global game_count
    game_count += 1
    print("Game is played " + str(game_count) + " no. of times")

    while True:
      play_again = input("\n Y: To Continue\n Q: To Quit\n")
      if play_again not in ["y", "q"]:
        continue
      else:
          break

    if play_again == 'y':
        play_again_function()
    else:
        print("Thanks for playing! \n Bye !")
        # sys.exit()
        return

play_again_function()