import random
import time
import os

class Ship:

    def __init__(self, positions: list, owner: str):
        """
        Initializes a Ship object with a list of positions and an owner (either player or machine), marking all positions as active.

        Parameters:
        - positions (list): List of positions to be initialized as active.
        - owner (str): The owner of the object.
        """

        self.alive = True
        self.owner = owner
        # Store the positions in a dictionary
        self.positions = {}

        # Initialize positions as True, which means active
        for position in positions:
            self.positions[position] = True

    def hit(self, cell: tuple):
        """
        Registers a hit on the specified cell, updates the ship's status, and checks if it is sunk.

        Parameters:
        - cell (tuple): The position of the cell being hit.

        Returns:
        - (bool): True if the cell was a valid hit, False otherwise.
        """

        # If the ship is in the cell attacked, that cell becomes inactive
        if cell in self.positions:
            self.positions[cell] = False

            # Check if the ship is sunk
            if list(self.positions.values()).count(True) == 0:
                self.alive = False
                print("Ship sunk!")
            
            return True
        
        return False
    


class Battleship:
    
    def __init__(self):

        """
        Initializes the game board with player and machine boards, labels, ships, and attack logs.
        """

        # Board building
        self.machine_board = [["🟦" for _ in range(11)] for _ in range(11)]
        self.player_board = [["🟦" for _ in range(11)] for _ in range(11)]
    
        letters = " ABCDEFGHIJ"
        numbers = [" ", "1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ", "5️⃣ ", "6️⃣ ", "7️⃣ ", "8️⃣ ", "9️⃣ ", "0️⃣ "]

        for i in range(len(self.player_board[0])):
            self.player_board[i][0] = letters[i]
            self.player_board[0][i] = numbers[i]

        for i in range(len(self.player_board[0])):
            self.machine_board[i][0] = letters[i]
            self.machine_board[0][i] = numbers[i]

        # Ships are stored in a list of dictionaries
        self.ships = [
            { "name": "Aircraft carrier", "size": 5 },
            { "name": "Battleship", "size": 4 },
            { "name": "Submarine", "size": 3 },
            { "name": "Destroyer", "size": 3 },
            { "name": "Patrol boat", "size": 2 }
            ]
        
        # Attacks are stroed in a dictionary
        self.attacks = {"player": [], "machine": []}


    def show_board(self, side: str, delay = 0):
        """
        Displays the board for the specified side (player or machine).

        Parameters:
        - side (str): The side whose board is to be displayed. Should be either 'player', 'machine' or 'machine_shown'.
        - delay (float): Delay to print every row in seconds. Default is 0.
        """

        # Displays player board
        if side == "player":
            for row in self.player_board:
                print("".join(row))
                time.sleep(delay)

        # Displays machine board with shown ships
        elif side == "machine_shown": 
            for row in self.machine_board:
                print("".join(row))
                time.sleep(delay)

        # Displays machine board with hidden ships
        elif side == "machine":
            for row in self.machine_board:
                for i in range(len(row)):
                    if row[i] == "🟪":
                        row[i] = "🟦"
                print("".join(row))
                time.delay(delay)
                 
        else:
            print("Side not valid. Try either 'player', 'machine' or 'machine_shown.")


    def get_position_indices(self, position: str):
        """
        Converts a position in the format XY (string) where X is the name of the row (A-J) and Y is the number of the column (1-10).

        Args: 
            position (str): String in the position.

        Returns:
            tuple: Integers with rows and columns indices.
        """

        letters = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i":9, "j": 10}

        row = letters[position[0].lower()]
        column = int(position[1:])

        return row, column
    
    def set_player_ships(self):
        """
        Places the player's ships on the board by allowing the player to choose the orientation and starting position for each ship.
        """
        # Interval to sleep for inputs
        interval = 0.2

        # Let's create the ships 1 by 1
        for i in range(len(self.ships)):
                
            valid = False

            while not valid:
        
                # Size of the ship
                size = self.ships[i]['size']
                print(f"Let's build the boat {self.ships[i]['name']} of size {size}")

                # Get the orientation of the ship
                while True:
                    orientation = input("Vertical or horizontal? (v/h)").lower()
                    time.sleep(interval)

                    # Check if orientation is valid
                    if orientation == "v" or orientation == "h":
                        break

                    else:
                        print("Orientation not valid. Try either 'v' or 'h'.")
                        time.sleep(interval)

                # Get the starting cell in indices
                while True:
                    string_cell = input("Starting cell (eg. A2)")
                    time.sleep(interval)

                    valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
                    valid_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

                    # Check if selected cell is valid
                    if string_cell[0].lower() in valid_letters and string_cell[1:] in valid_numbers:
                        break

                    else: 
                        print("Type a valid cell")
                        time.sleep(interval)

                # Get the indices for the selected cell
                starting_position = self.get_position_indices(string_cell)

                # Empty array to store the positions in tuples
                positions = []

                # Build ship depending on chosen orientation 
                if orientation == "h":
                    for j in range(self.ships[i]['size']):
                        positions.append((starting_position[0], starting_position[1] + j))

                elif orientation == "v":
                    for j in range(self.ships[i]['size']):
                        positions.append((starting_position[0] + j, starting_position[1]))

                # Check if values are correct
                for position in positions:
                    if self.player_board[position[0]][position[1]] == "🟦":
                        valid = True

                    else:
                        valid = False
                        break

            for position in positions:
                self.player_board[position[0]][position[1]] = "🟩"

            # Instance Ship Class with the position values and store it in the list
            self.ships[i]['player'] = Ship(positions, "player")

            # Clear console
            os.system('cls' if os.name == 'nt' else 'clear')

            # Show the board after each ship is in place
            self.show_board("player")


    def set_machine_ships(self):
        """
        Places the machine's ships on the board by randomly choosing the orientation and starting position for each ship.
        """
        
        # Let's create the ships 1 by 1
        for i in range(len(self.ships)):
                
            valid = False

            while not valid:
        
                # Size of the ship
                size = self.ships[i]['size']

                # Get the orientation of the ship
                orientation = random.choice(["v", "h"])

                # Get the starting cell in indices
                starting_position = (random.randint(1, 11 - self.ships[i]['size']), random.randint(1, 11 - self.ships[i]['size']))

                # Empty array to store the positions in tuples
                positions = []

                # Build ship depending on chosen orientation
                if orientation == "h":
                    for j in range(self.ships[i]['size']):
                        positions.append((starting_position[0], starting_position[1] + j))

                elif orientation == "v":
                    for j in range(self.ships[i]['size']):
                        positions.append((starting_position[0] + j, starting_position[1]))

                # Check if values are correct
                for position in positions:
                    if self.machine_board[position[0]][position[1]] == "🟦":
                        valid = True

                    else:
                        valid = False
                        break

            for position in positions:
                self.machine_board[position[0]][position[1]] = "🟪"

            # Instance Ship Class with the position values and store it in the list
            self.ships[i]['machine'] = Ship(positions, "machine")

        # Show the board after all ships in place
        #self.show_board("machine_shown")


    def launch_attack(self, side: str):
        """
        Launches an attack on the specified side's board, either 'player' or 'machine', and updates the board based on the result.

        Parameters:
        - side (str): The side to attack, either 'player' or 'machine'.
        """

        # Set an interval time to sleep for inputs
        interval = 0.2
        
        if side == 'player':

            while True:

                while True:
                    # Where to attack
                    string_cell = input("Select cell to attack(eg. A2)")
                    time.sleep(interval)

                    # Check if selected cell is valid
                    if len(string_cell) == 2 and string_cell[0].lower() in "abcdefghij" and string_cell[1] in "123456789":
                        break

                    # Case for a10, b10, c10, etc
                    elif len(string_cell) == 3 and string_cell[0].lower() in "abcdefghij" and string_cell[1:] == "10":
                        break

                    else: 
                        print("Type a valid cell")

                # Get the indices for the selected cell
                attack_position = self.get_position_indices(string_cell)

                # Check if cell was attacked before
                if attack_position not in self.attacks["player"]:
                    
                    # If it was, launch the attack
                    for i in range(len(self.ships)):
                        hit = self.ships[i]['machine'].hit(attack_position)

                        if hit:
                            icon = "❌"
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("You hit the ship! 💥")

                            if not self.ships[i]['machine'].alive:
                                print("Ship sunk! 💀")
                            break
                            
                    if not hit:
                        icon = "💧"
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Water! 💦")

                    # Flag as attacked
                    self.attacks['player'].append(attack_position)

                    # Update the board
                    self.machine_board[attack_position[0]][attack_position[1]] = icon
                    break

        elif side == 'machine':

            while True:

                # Where to attack (placeholder for random choice)
                attack_position = (random.randint(1, 10), random.randint(1, 10))

                # Check if cell was attacked before
                if attack_position not in self.attacks["machine"]:
                    
                    # If it was, launch the attack
                    for i in range(len(self.ships)):
                        hit = self.ships[i]['player'].hit(attack_position)

                        if hit:
                            icon = "❌"
                            print("Your ship got hit! 💥")

                            if not self.ships[i]['player'].alive:
                                print("Your ship is sunk! 💀")
                            break

                    if not hit:
                        icon = "💧"
                        print("Water! 💦")

                    # Flag as attacked
                    self.attacks['machine'].append(attack_position)

                    # Update the board
                    self.player_board[attack_position[0]][attack_position[1]] = icon
                    break


    def check_win(self, side: str):
        """
        Checks if the specified side has won by verifying if all the opponent's ships are sunk.

        Parameters:
        - side (str): The side to check for victory, either 'player' or 'machine'.

        Returns:
        - (bool): True if the specified side has won, False otherwise.
        """

        if side == 'machine':
            return True if len(list(filter(lambda x: x['player'].alive, self.ships))) < 1 else False

        elif side == 'player':
            return True if len(list(filter(lambda x: x['machine'].alive, self.ships))) < 1 else False
            
        else:
            print('Wrong side imput. Try either "player" or "machine".')

    
    def welcome(self):
        welcome_msg = r"""
  ██████  ██▓ ███▄    █  ██ ▄█▀   ▄▄▄█████▓ ██░ ██ ▓█████      █████▒ ██▓    ▓█████ ▓█████ ▄▄▄█████▓
▒██    ▒ ▓██▒ ██ ▀█   █  ██▄█▒    ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██   ▒ ▓██▒    ▓█   ▀ ▓█   ▀ ▓  ██▒ ▓▒
░ ▓██▄   ▒██▒▓██  ▀█ ██▒▓███▄░    ▒ ▓██░ ▒░▒██▀▀██░▒███      ▒████ ░ ▒██░    ▒███   ▒███   ▒ ▓██░ ▒░
  ▒   ██▒░██░▓██▒  ▐▌██▒▓██ █▄    ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░▓█▒  ░ ▒██░    ▒▓█  ▄ ▒▓█  ▄ ░ ▓██▓ ░ 
▒██████▒▒░██░▒██░   ▓██░▒██▒ █▄     ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒█░    ░██████▒░▒████▒░▒████▒  ▒██▒ ░ 
▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒     ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░    ▒ ░    ░ ▒░▓  ░░░ ▒░ ░░░ ▒░ ░  ▒ ░░   
░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░       ░     ▒ ░▒░ ░ ░ ░  ░    ░      ░ ░ ▒  ░ ░ ░  ░ ░ ░  ░    ░    
░  ░  ░   ▒ ░   ░   ░ ░ ░ ░░ ░      ░       ░  ░░ ░   ░       ░ ░      ░ ░      ░      ░     ░      
      ░   ░           ░ ░  ░                ░  ░  ░   ░  ░               ░  ░   ░  ░   ░  ░         
                                                                                                    
"""
        print(welcome_msg)


    def message_for_loser(self):
        loser_msg = r"""
▓██   ██▓ ▒█████   █    ██     ▄▄▄       ██▀███  ▓█████     ▄▄▄          ██▓     ▒█████    ██████ ▓█████  ██▀███  
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒████▄    ▓██ ▒ ██▒▓█   ▀    ▒████▄       ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒▒███      ▒██  ▀█▄     ▒██░    ▒██░  ██▒░ ▓██▄   ▒███   ▓██ ░▄█ ▒
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄    ░██▄▄▄▄██    ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  
  ░ ██▒▓░░ ████▓▒░▒▒█████▓     ▓█   ▓██▒░██▓ ▒██▒░▒████▒    ▓█   ▓██▒   ░██████▒░ ████▓▒░▒██████▒▒░▒████▒░██▓ ▒██▒
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░    ▒▒   ▓▒█░   ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░     ▒   ▒▒ ░   ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ▒     ░░   ░    ░        ░   ▒        ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░     ░░   ░ 
 ░ ░         ░ ░     ░              ░  ░   ░        ░  ░         ░  ░       ░  ░    ░ ░        ░     ░  ░   ░     
 ░ ░                                                                                                              
"""
        print(loser_msg)


    def message_for_winner(self):
        winner_msg = r"""
                                                ('-.      _  .-')      ('-.            ('-.             (`\ .-') /`               .-') _       .-') _     ('-.    _  .-')   ,---. 
                                               ( OO ).-. ( \( -O )   _(  OO)          ( OO ).-.          `.( OO ),'              ( OO ) )     ( OO ) )  _(  OO)  ( \( -O )  |   | 
  ,--.   ,--. .-'),-----.  ,--. ,--.           / . --. /  ,------.  (,------.         / . --. /       ,--./  .--.    ,-.-')  ,--./ ,--,'  ,--./ ,--,'  (,------.  ,------.  |   | 
   \  `.'  / ( OO'  .-.  ' |  | |  |           | \-.  \   |   /`. '  |  .---'         | \-.  \        |      |  |    |  |OO) |   \ |  |\  |   \ |  |\   |  .---'  |   /`. ' |   | 
 .-')     /  /   |  | |  | |  | | .-')       .-'-'  |  |  |  /  | |  |  |           .-'-'  |  |       |  |   |  |,   |  |  \ |    \|  | ) |    \|  | )  |  |      |  /  | | |   | 
(OO  \   /   \_) |  |\|  | |  |_|( OO )       \| |_.'  |  |  |_.' | (|  '--.         \| |_.'  |       |  |.'.|  |_)  |  |(_/ |  .     |/  |  .     |/  (|  '--.   |  |_.' | |  .' 
 |   /  /\_    \ |  | |  | |  | | `-' /        |  .-.  |  |  .  '.'  |  .--'          |  .-.  |       |         |   ,|  |_.' |  |\    |   |  |\    |    |  .--'   |  .  '.' `--'  
 `-./  /.__)    `'  '-'  '('  '-'(_.-'         |  | |  |  |  |\  \   |  `---.         |  | |  |       |   ,'.   |  (_|  |    |  | \   |   |  | \   |    |  `---.  |  |\  \  .--.  
   `--'           `-----'   `-----'            `--' `--'  `--' '--'  `------'         `--' `--'       '--'   '--'    `--'    `--'  `--'   `--'  `--'    `------'  `--' '--' '--'  
"""
        print(winner_msg)


    def play(self):
        """
        Runs the main game loop for a Battleship-style game. It handles setting up the fleets, alternating turns between the player and the machine, displaying the boards, and checking for win conditions.
        """

        # Welcome message
        self.welcome()

        # Set the fleet
        self.set_machine_ships()
        print("Time to set up our fleet. This is the template:")
        self.show_board('player', delay = 0.2)
        self.set_player_ships()

        # Clear console
        os.system('cls' if os.name == 'nt' else 'clear')

        # The game starts here
        while True:
            
            print("The enemy is attacking!")
            time.sleep(0.5)

            # Enemy's attack
            self.launch_attack('machine')

            # Show your fleet
            print("Your fleet:")
            time.sleep(0.5)
            self.show_board('player')

            # Check win condition
            if self.check_win('machine'):
                print("Machine wins this time!")
                self.message_for_loser()
                break

            # Player launch attack
            self.launch_attack('player')

            # Show enemy's fleet
            print("Enemy's fleet:")
            time.sleep(0.5)
            self.show_board('machine')

            # Check win condition
            if self.check_win('player'):
                print("Player wins this time!")
                self.message_for_winner
                break

        # Goodbye message
        time.sleep(1)
        print("Thank you for playing!")