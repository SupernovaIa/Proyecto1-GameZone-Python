from src.battleship import Battleship
from src.spock_game import SpockGame
from src.hangman import Hangman
from src.tictactoe import Tictactoe
from src.trivia import TriviaCrack
import time
import os

def menu():

    play = True

    while play:

        # Clear console
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Welcome to the game room 🕹️")

        g = input("Select a game:")

        if g == '1':
            rounds = int(input("Select max score:"))
            game = SpockGame(rounds)
            game.play()

        elif g == '2':
            lives = int(input("Select the amount of lives:"))
            game = Hangman(lives)
            game.play()

        elif g == '3':
            game = Tictactoe()
            game.play()

        elif g == '4':
            game = TriviaCrack()
            game.play()
        
        elif g == '5':
            game = Battleship()
            game.play()

        while True:
            play_again = input("Do you wanna play more? (y/n) 🕹️").lower()

            if play_again in ['y', 'n']:

                if play_again == "y":
                    play = True
                    break

                elif play_again == "n":
                    play = False
                    break

            else:
                print("Please, say yes (y) or no (n)")

    # Clear console
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Goodbye! 😊")
    time.sleep(2)
    # Clear console
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Loser 😒")
    time.sleep(4)