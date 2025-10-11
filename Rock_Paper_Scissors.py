import random
from tkinter import *
import tkinter as tk




def wHich_game():
    x = int(input("Welcome! Which type of rock paper scissors do you want to play? The classic one (1)," \
    " the one from the Big Bang Theory (2) or exit the game (3)? "))
    while not (x == 1 or x == 2 or x):
        x = int(input("Please, pick 1, 2 or 3: "))
    if x == 1:
        classic_rps()
    if x == 2:
        bbt_rps()
    if x == 3:
        print("Goodbye!")
        exit()
    
def classic_rps():
    print("\n")
    print("===================")
    print("Rock Paper Scissors")
    print("===================")
    print("\n")

    print("Welcome to Rock Paper Scissors! Please, choose one of the options below:")
    print("1) ✊")
    print("2) ✋")
    print("3) ✌️")
    choix = ["✊", "✋", "✌️"]
    n = len(choix)

    choix_player = int(input("Pick a number: ")) - 1
    while not (0 <= choix_player <= n-1):
        choix_player = int(input("Pick a number: ")) - 1
    choix_cpu = random.choice(choix)


    print(f"You chose: {choix[choix_player]}")
    print(f"CPU chose: {choix_cpu}") 

    player = choix[choix_player]
    cpu = choix_cpu

    if (player == "✊" and cpu == "✌️") or (player == "✋" and cpu == "✊")  or (player == "✌️" and cpu == "✋"):
        rematch = str(input("You win! Can I get a rematch (Y/N)? "))
        if rematch.lower() == "y":
            classic_rps()
        else:
            wHich_game()
    elif player == cpu:
        rematch = str(input("It's a tie! Can I get a rematch? (Y/N)? "))
        if rematch.lower() == "y":
            classic_rps()
        else:
            wHich_game()
    else:
        rematch = str(input("CPU wins! Do you want a rematch (Y/N)? "))
        if rematch.lower() == "y":
            classic_rps()
        else:
            wHich_game()

def bbt_rps():
    print("\n")
    print("================================")
    print("Rock Paper Scissors Lizard Spock")
    print("================================")
    print("\n")

    print("Welcome to Rock Paper Scissors Lizard Spock! Please, choose one of the options below:")
    print("1) ✊")
    print("2) ✋")
    print("3) ✌️")
    print("4) 🦎")
    print("5) 🖖")
    choix = ["✊", "✋", "✌️", "🦎", "🖖"]
    n = len(choix)

    choix_player = int(input("Pick a number: ")) -1
    while not (0 <= choix_player <= n-1):
        choix_player = int(input("Pick a number: "))-1
    choix_cpu = random.choice(choix)


    print(f"You chose: {choix[choix_player]}")
    print(f"CPU chose: {choix_cpu}") 

    player = choix[choix_player]
    cpu = choix_cpu

    if (player == "✊" and (cpu == "✌️" or cpu == "🦎")):
        rematch = str(input("You win! Can I get a rematch (Y/N)? "))
        if rematch.lower() == "y":
            bbt_rps()
        else:
            wHich_game()
    elif(player == "✋" and (cpu == "✊" or cpu == "🖖")):
        rematch = str(input("You win! Can I get a rematch (Y/N)? "))
        if rematch.lower() == "y":
            bbt_rps()
        else:
            wHich_game()
    elif(player == "✌️" and (cpu == "✋" or cpu == "🦎")):
        rematch = str(input("You win! Can I get a rematch (Y/N)? "))
        if rematch.lower() == "y":
            bbt_rps()
        else:
            wHich_game()
    elif (player == "🦎" and (cpu == "✋" or cpu == "🖖")):
        rematch = str(input("You win! Can I get a rematch (Y/N)? "))
        if rematch.lower() == "y":
            bbt_rps()
        else:
            wHich_game()
    elif (player == "🖖" and (cpu == "✊" or cpu == "✌️")):
        rematch = str(input("You win! Can I get a rematch (Y/N)? "))
        if rematch.lower() == "y":
            bbt_rps()
        else:
            wHich_game()
    elif player == cpu:
        rematch = str(input("It's a tie! Can I get a rematch? (Y/N)? "))
        if rematch.lower() == "y":
            bbt_rps()
        else:
            wHich_game()
    else:
        rematch = str(input("CPU wins! Do you want a rematch (Y/N)? "))
        if rematch.lower() == "y":
            bbt_rps()
        else:
            wHich_game()


#wHich_game()

