# 🎮 Classic Games Development with Python
## 📖 Project Description

![main_image](https://github.com/user-attachments/assets/17c02f87-2699-4fd2-a3e6-a7bceff3b316)

This project involves the development of a series of classic games using **Python 3.12**. The objective of the project is to apply various programming concepts, such as loops, conditionals, exception handling, and classes, to create interactive and entertaining experiences.

The games developed include:
- **Trivia Crack** 🧠❓: Users answer questions from various categories and must answer 10 questions correctly in a row to win. One mistake and you are out.
- **Tic-Tac-Toe** ❌⭕: Two users play against each other on a 3x3 grid, aiming to place three pieces in a row (horizontally, vertically, or diagonally) before the oppoent does.
- **Hangman** 😵: The user guesses a random word selected from a predefined list, with each wrong guess revealing part of the hangman. The user wins if they guess the word before running out of attempts.
- **Rock-Paper-Scissors-Lizard-Spock** ✋🪨✂️🦎🖖: The user competes against the machine in this classic game. We’ve added the Rock-Paper-Scissors-Lizard-Spock variant for extra fun.
- **Battleship** 💥🚢: A strategic game where the user tries to locate and sink the machine's ships on a 10x10 grid before the machine sinks theirs.

## 🗂️ Project Structure

```bash
├── README.md              # Project description
├── main.py                # Main script to launch the menu
├── src/                   # Source code for the games
│   ├── trivia.py          # Trivia game logic
│   ├── tictactoe.py       # Tic-Tac-Toe game logic
│   ├── hangman.py         # Hangman game logic
│   ├── spockgame.py       # Rock-Paper-Scissors game logic
│   └── battleship.py      # Battleship game logic
│   └── menu.py            # Main menu for selecting games
├── notebook/              # Jupyter notebooks for the games
│   ├── trivia.ipynb       # Trivia game in notebook form
│   ├── tictactoe.ipynb    # Tic-Tac-Toe game in notebook form
│   ├── hangman.ipynb      # Hangman game in notebook form
│   ├── spockgame.ipynb    # Rock-Paper-Scissors in notebook form
│   └── battleship.ipynb   # Battleship game in notebook form
```

## 🛠️ Installation and Requirements

This project was developed using **Python 3.12** and does not require any external libraries beyond Python’s standard library. To run the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/SupernovaIa/Proyecto1-Juegos-Python.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Proyecto1-Juegos-Python
   ```

3. Run the main menu to select a game:
   ```bash
   python main.py
   ```

There are no additional dependencies, so no need to install any external libraries.

## 📊 Results and Conclusions

This project was developed over the course of two days to reach its current status. Below are the current features implemented and a quick coding review for each game:

- **Trivia Game**: This game asks questions taken from a JSON database, divided by categories. Possibly the simplest game to program on the list. To make it more interesting, the option to load custom questions in JSON format has been added.
- **Tic-Tac-Toe**: This is the classic two-player tic-tac-toe game. While the game is simple to program, it’s important to properly handle the victory checks.
- **Hangman**: This is the classic hangman game, where you have to guess a word from a list given its length. This game is also simple, but it requires properly managing the letters already used and how the result is displayed to the player.
- **Rock-Paper-Scissors (Lizard-Spock)**: This is the classic rock-paper-scissors game expanded with lizard and Spock. It’s also simple, though it requires a proper understanding of the victory-defeat relationships between the variables to function correctly.
- **Battleship**: The classic Battleship game on a 10 x 10 grid. Undoubtedly the most difficult of all, as it requires repeatedly checking the status of the ships, properly displaying both the player’s and the computer’s boards, managing shots, and handling victory conditions.

This project successfully demonstrates how Python can be used to create interactive, text-based games, leveraging basic programming concepts and logic.

## 🔄 Next Steps

- **Trivia Game**: Enhance the game by adding features like adjustable question count, manual category selection, and a lives or scoring system.
- **Tic-Tac-Toe**: Introduce an option to play against the computer. Implement a new game mode where the earliest placed icons disappear over time, preventing the possibility of a tie.
- **Hangman**: Add support for loading word sets from an external file.
- **Rock-Paper-Scissors (Lizard-Spock)**: Develop a more advanced scoring system.
- **Battleship**: Implement AI for the computer opponent, along with a "hard mode" where ships are not placed until halfway through the game, adding an element of cheating.

Consider developing a chess game as an additional project.

## 🤝 Contributions

Contributions are welcome! If you'd like to improve or extend the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request when you're ready.

Feel free to open an issue if you have any ideas or suggestions.

## ✒️ Authors

- **Javier Carreira** - Main Developer - [GitHub](https://github.com/SupernovaIa)

Special thanks to the team at Hack(io) for the opportunity to work on this project.