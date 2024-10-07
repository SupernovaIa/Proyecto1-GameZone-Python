import random
import os
import time

class Hangman:

    def __init__(self, lives: int):
        
        words_list = [
            "apple", "banana", "orange", "grape", "strawberry",
            "elephant", "giraffe", "dolphin", "kangaroo", "crocodile",
            "computer", "python", "keyboard", "monitor", "internet",
            "mountain", "ocean", "desert", "river", "valley",
            "soccer", "basketball", "baseball", "tennis", "cricket",
            "piano", "guitar", "violin", "trumpet", "drums",
            "galaxy", "planet", "asteroid", "comet", "meteor",
            "science", "chemistry", "physics", "biology", "mathematics",
            "friendship", "happiness", "adventure", "mystery", "fantasy"
        ]

        # Choose a random word
        word_index = random.randint(0, len(words_list) - 1)
        self.word_to_guess = words_list[word_index]
        # Get nuber of characters
        self.length_word = len(self.word_to_guess)
        self.display = ["_"] * self.length_word
        self.lives = lives
        
        # Already tried characters
        self.tried_characters = []


    def turn(self):
        """
        Handles a single turn in the guessing game, allowing the player to input a letter, checks its validity, and updates the game state accordingly.
        """

        # Start a flag if the letter is guessed
        guessed = False
        # Try a character
        while True:
            char_trial = input("Try a char: ").strip().lower()

            if len(char_trial) == 1 and char_trial.isalpha():
                
                if char_trial not in self.tried_characters:
                    break

                else:
                    print(f"You've already used {char_trial}. Try something different.")

            else:
                print("Enter one letter, and only one: ")

        # Clear console
        os.system('cls' if os.name == 'nt' else 'clear')

        # Store the character
        self.tried_characters.append(char_trial)

        # Check if guessed and, if so, add to display
        for i in range(self.length_word):
            if self.word_to_guess[i] == char_trial:
                self.display[i] = char_trial
                guessed = True
                print(f"Congrats! The letter {char_trial} is in the word 😇")

        # If not guessed substract a live
        if not guessed:
            print("I'm sorry. That letter is wrong 🙃")
            self.lives -= 1

            
    def check_win(self):
        """
        Checks if the player has won by verifying if there are no more blank spaces ('_') in the word display.

        Returns:
        - (bool): True if the player has won, False otherwise.
        """

        # Check win condition
        if '_' not in self.display:
            print(f"You won! The word was {self.word_to_guess} 🥳")
            return True
        
        return False


    def play(self):
        """
        Manages the main game loop for the Hangman game, displaying the current state of the game, handling player input, and checking for win/loss conditions.
        """

        # Clear console
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Welcome to the Hangman Game 🎻😵")
        time.sleep(1)
        # Show the display
        print("---------------------------")
        time.sleep(1)
        print("This is our word to guess: ")
        time.sleep(1)
        print(self.display)
        time.sleep(1)
        print("---------------------------")
        time.sleep(1)
        print(f"You have {self.lives} lives remaining")

        while self.lives > 0:

            # Turn
            self.turn()

            # Show the display
            print("---------------------------")
            print("This is our word to guess: ")
            print(self.display)

            # Show used letters
            print("---------------------------")
            print("You have already used these letters:")
            print(self.tried_characters)

            # Check if win
            if self.check_win():
                break

            # Lives remaining
            print("---------------------------")
            print(f"You have {self.lives} lives remaining")

        if self.lives == 0:
            print("You are dead 💀 (and are also a loser 🤣)")
            print(f"The word was {self.word_to_guess}")