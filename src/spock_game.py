import random
import os

class SpockGame:

    def __init__(self, rounds: int):
        """ Initializes the Spock game, a variation of the traditional rock-paper-scissors game, where the player competes against the computer over a set number of rounds.

        Parameters:
        - rounds (int): The number of rounds required to win the game.
        """

        # Options available ordered by win condition
        self.options = ('rock', 'lizard', 'spock', 'scissors', 'paper')
        # Score
        self.score = {"Computer": 0, "Player": 0}
        self.rounds = rounds

    def player(self):
        """
        Handles the player's and computer's selection in the game.

        The computer selects a random option from the available choices, while the player is prompted to input their choice from the same set of options. The method ensures that the player selects a valid option and then computes the difference between the player's and the computer's choices for determining the winner.
        """

        # Computer plays randomly
        computer_index = random.randint(1, len(self.options)) - 1
        computer = self.options[computer_index]

        # We choose our option
        while True:
            player = input("Choose one option (rock, lizard, spock, scissors, paper): ")
            if player in self.options:
                break
            else:
                print("Select a valid option (rock, lizard, spock, scissors, paper): ")

        # Assign values
        player_index = self.options.index(player)

        # Clear console
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==========================")
        # Print selections
        print(f"You chose {player} and machine {computer}")

        # Compute the index different to get win condition
        self.diff = computer_index - player_index

    def turn(self):
        """
        Determines the outcome of the current game turn based on the win conditions.
        """

        # Set win conditions
        computer_win_conditions = [2, 4, -1, -3]
        player_win_conditions = [1, 3, -2, -4]

        # Check winner
        if self.diff == 0:
            print("It's a draw")

        elif self.diff in player_win_conditions:
            self.score['Player'] += 1
            print("Player wins!")

        elif self.diff in computer_win_conditions:
            self.score['Computer'] += 1
            print("Computer wins!")

    
    def show_score(self):
        print("--------------------------")
        print(f"The first player to score {self.rounds} points wins")
        print("--------------------------")
        print(f"  🔥 Current Score 🔥  ")
        print("--------------------------")
        print(f"  Player:   {self.score['Player']}")
        print(f"  Computer: {self.score['Computer']}")
        print("==========================\n")
    
    
    def play(self):

        # Clear console
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Welcome to the Spock Game ✋🪨✂️🦎🖖")
        print("--------------------------")
        print(f"The first player to score {self.rounds} points wins")

        # Initialize number of rounds
        number_of_wins = 0

        # We stop when a player reaches certain amount of wins
        while number_of_wins < self.rounds:

            # Set the options
            self.player()
            # Compute winner
            self.turn()
            # Compute the number of wins
            number_of_wins = max(self.score['Player'], self.score['Computer'])

            # Display current results
            self.show_score()

        if self.score['Player'] > self.score['Computer']:
            print("You won this time to the Spock Game 🥳")

        else: 
            print("You are a loser 🤣")