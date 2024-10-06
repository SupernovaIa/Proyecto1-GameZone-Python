# 🎮 Classic Games Development with Python
## 📖 Project Description

This project involves the development of a series of classic games using Python 3.12. The objective of the project is to apply various programming concepts, such as loops, conditionals, exception handling, and classes, to create interactive and entertaining experiences.

The games developed include:
- **Trivia Crack**: Users answer questions from various categories and must answer 10 questions correctly in a row to win. One mistake and you are out.
- **Tic-Tac-Toe**: Two users play against each other on a 3x3 grid, aiming to place three pieces in a row (horizontally, vertically, or diagonally) before the oppoent does.
- **Hangman**: The user guesses a random word selected from a predefined list, with each wrong guess revealing part of the hangman. The user wins if they guess the word before running out of attempts.
- **Rock-Paper-Scissors-Lizard-Spock**: The user competes against the machine in this classic game. We’ve added the Rock-Paper-Scissors-Lizard-Spock variant for extra fun.
- **Battleship**: A strategic game where the user tries to locate and sink the machine's ships on a 10x10 grid before the machine sinks theirs.

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

- **Trivia Game**: Offers a variety of questions in different categories, challenging the user to answer 10 questions consecutively to win. A json file can be added for additional questions.
- **Tic-Tac-Toe**: Provides an enjoyable challenge where the user plays against a machine that follows basic strategies to win.
- **Hangman**: Engages users with a random word-guessing game and graphical representation of the hangman.
- **Rock-Paper-Scissors (Lizard-Spock)**: Adds a twist to the classic game with more options for players to enjoy, increasing strategic possibilities.
- **Battleship**: A fun, strategy-based game where the user tries to outmaneuver the machine in a 10x10 grid.

This project successfully demonstrates how Python can be used to create interactive, text-based games, leveraging basic programming concepts and logic.

## 🔄 Future Steps

- **
- **Improve AI strategies** for Tic-Tac-Toe and Battleship to provide a more challenging experience for users.
- **Add a graphical user interface (GUI)** to make the games visually appealing and more accessible.
- **Expand content** in Trivia Game and Hangman by adding more questions and words to increase replayability.
- Consider adding **online multiplayer functionality** for some of the games.

## 🤝 Contributions

Contributions are welcome! If you'd like to improve or extend the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request when you're ready.

Feel free to open an issue if you have any ideas or suggestions.

## ✒️ Authors

- **Javier Carreira** - Main Developer - [GitHub](https://github.com/SupernovaIa)

Special thanks to the team at Hack(io) for the opportunity to work on this project.