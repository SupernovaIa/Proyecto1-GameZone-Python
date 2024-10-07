import json
import random
import time
import os

class TriviaCrack:

    def __init__(self, file_path = "asset/questions.json"):
        """
        Initializes the class by loading quiz data from a JSON file and setting the categories attribute.

        Parameters:
        - file_path (str): Path to the JSON file containing quiz data. Defaults to 'questions.json'.
        """

        # Open file with questions per categories
        with open(file_path, 'r') as json_file:
            loaded_quiz_data = json.load(json_file)

        # Extract categories
        self.categories = loaded_quiz_data["categories"]


    def select_question(self):
        """
        Selects a random question from a randomly chosen category.

        Returns:
        - category (str): The selected category.
        - question (dict): A randomly selected question from the chosen category.
        """

        # Select a random category
        while True:
            try:
                category = random.choice(list(self.categories.keys()))
                questions = self.categories[category]['questions']
                question = self.categories[category]['questions'].pop(random.randint(0, len(questions) - 1))
                break
            except:
                pass

        return category, question


    def play(self):
        """
        Plays a quiz game where the player answers randomly selected questions from different categories. The game continues until the player answers incorrectly or wins by reaching a score of 10.
        """
        # Starting score
        score = 0
        print("Welcome to trivia game 🧠❓")

        while True:

            # Get info from a random question
            info = self.select_question()
            categroy = info[0]
            question = info[1]
            print(f"The following question is about {categroy}")
            print(question['question'])
            print(question['options'])

            # Type the answer
            while True:
                answer = input("Enter your answer:").upper()
                
                # Clear console
                os.system('cls' if os.name == 'nt' else 'clear')
                # Check if valid
                if answer in "ABCD":
                    break
                else:
                    print("Select A, B, C or D")

            # Check if correct
            if answer == question['correct_answer']:
                score += 1
                print("Correct answer! 🥳")
                print(f"You have answered {score} questions correctly")

                # Check if won the game
                if score >= 10:
                    print("You are a winner! 🏆")
                    break

            # I incorrect you are out
            else:
                print("Incorrect! 😡")
                print(f"Correct answer was {question['correct_answer']}")
                time.sleep(0.5)
                print("You're out 🙃")
                break