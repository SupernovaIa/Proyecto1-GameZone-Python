from src.sink_fleet import SinkFleet
from src.rock_paper_scissors import SpockGame
from src.hangman import Hangman
from src.tictactoe import Tictactoe

def menu():

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
        pass
    
    elif g == '5':
        game = SinkFleet()
        game.play()