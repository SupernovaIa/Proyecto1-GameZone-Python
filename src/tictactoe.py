import os
import time

class Tictactoe:

    def __init__(self):
        """
        Initializes a 3x3 game board display with each cell represented by the '·' character.
        """

        self.display = [ ["·" for _ in range(3)] for _ in range(3)]


    def show_display(self):
        """
        Displays the current state of the game board by printing each row of the display.
        """
        print("The board is: ")
        for row in self.display:
            print("".join(row))


    def turn(self, player):
        """
        Handles a single turn for the player, allowing the selection of a valid position on the board and placing the player's icon.

        Parameters:
        - player (int): The current player (1 for "O", 2 for "X").
        """

        # Select the icon based on player to play
        if player == 1:
            print("Player 1. Write an O")
            icon = "O"

        else:
            print("Player 2. Write an X")
            icon = "X"

        while True:

            # Select the position
            while True:
                selected_square = input("Select position: ").lower()

                if selected_square in "ertdfgcvb":
                    break

                else:
                    print("Choose a valid square:")
                    print("e r t")
                    print("d f g")
                    print("c v b")

            # Converting string to indices
            player_row = self.converting_positions(selected_square)[0]
            player_col = self.converting_positions(selected_square)[1]

            # Checking free slots
            if self.display[player_row][player_col] != "·":
                print("Cell already occupied, try othe location")

            # Checking indices out of range
            elif player_row not in range(3) or player_col not in range(3):
                print("Select a valid position")

            # Setting the icon
            else:
                self.display[player_row][player_col] = icon
                break
        
    
    def converting_positions(self, char: str):
        """
        Converts a given character representing a board position into corresponding row and column indices.

        Parameters:
        - char (str): A character representing the selected position (e.g., 'e', 'r', 't', etc.).

        Returns:
        - (tuple): A tuple containing the row and column indices corresponding to the selected position.
        """

        dictionary = {"e": (0,0), "r": (0,1), "t": (0,2),"d":(1,0), "f": (1,1), "g": (1,2),"c": (2,0),"v": (2,1),"b": (2,2)}
        return dictionary[char]


    def check_win(self):
        """
        Checks if there is a winning condition in the game by evaluating rows, columns, and diagonals for three matching icons ('O' or 'X').

        Returns:
        - (bool): True if there is a winner, False otherwise.
        """

        # Creating empty lists to store diagonal items
        diagonal1 = []
        diagonal2 = []

        # Starting indices for diagonals
        i = 0
        j = 2

        # Check rows
        for row in self.display:

            if row.count("O") == 3:
                print("Player 1 wins")
                return True
            
            elif row.count("X") == 3:
                print("Player 2 wins")
                return True

            # Appending diagonal items
            diagonal1.append(row[i])
            i += 1
            diagonal2.append(row[j])
            j -= 1

        # Check diagonals
        if diagonal1.count("O") == 3:
            print("Player 1 wins")
            return True

        elif diagonal1.count("X") == 3:
            print("Player 2 wins")
            return True 

        elif diagonal2.count("O") == 3:
            print("Player 1 wins")
            return True

        elif diagonal2.count("X") == 3:
            print("Player 2 wins")
            return True  

        # Check columns
        for col in zip(*self.display):
            if col.count("O") == 3:
                print("Player 1 wins")
                return True
            elif col.count("X") == 3:
                print("Player 2 wins")
                return True 


    def check_draw(self):
        """
        Checks if the game has ended in a draw by determining if there are no remaining empty spaces ('·') on the board.

        Returns:
        - (bool): True if the game is a draw, False otherwise.
        """

        # Counting empty spaces
        for row in self.display:
            if row.count("·") > 0:
                return False
            
        # If no empty spaces it's a draw
        print("It's a draw! 😅")
        return True

    def play(self):
        """
        Runs the main game loop, alternating turns between Player 1 and Player 2, and checking for a win or draw after each turn.
        """

        print("Welcome to Tic Tac Toe! ❌⭕")
        time.sleep(1)
        print("==========================")
        time.sleep(1)
        print("Instructions: ")
        print("To choose a valid square use these keys")
        print("e r t")
        print("d f g")
        print("c v b")


        # Showing display
        self.show_display()

        while True:

            # Player 1
            time.sleep(1)
            self.turn(1)
            # Clear console
            os.system('cls' if os.name == 'nt' else 'clear')
            self.show_display()

            # Check win
            if self.check_win():
                break

            # Check draw
            elif self.check_draw():
                break
            
            # Player 2
            time.sleep(1)
            self.turn(2)
            # Clear console
            os.system('cls' if os.name == 'nt' else 'clear')
            self.show_display()

            # Check win
            if self.check_win():
                break

            # Check draw
            elif self.check_draw():
                break