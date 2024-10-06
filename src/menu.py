from src.sink_fleet import SinkFleet
from src.rock_paper_scissors import SpockGame

def menu():

    g = input("Select a game:")

    if g == '1':
        rounds = int(input("Select max score:"))
        game = SpockGame(rounds)
        game.play()

    elif g == '5':
        game = SinkFleet()
        game.play()