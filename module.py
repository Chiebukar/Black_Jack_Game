from games import *
import random

print("Welcome to the simplest game")

again = None
while again != "n":
    players = []
    num = ask_number("How many players?(2-5): ", 2, 5)
    for i in range(num):
        name = input("Enter player's name: ")
        score = random.randrange(101)
        player = Player(name, score)
        players.append(player)
    print("Here are the results")
    for player in players:
        print(player)
    again = ask_yes_no("Do you want to play again?:(y/n)")


input("\n\n press the enter key to exit")






