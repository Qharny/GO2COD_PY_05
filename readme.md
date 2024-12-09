# 🎮 Tkinter Hangman Game

A graphical Hangman game implemented in Python using Tkinter, offering an interactive and fun word-guessing experience.

## 📝 Overview

This Hangman game provides a graphical user interface where players can guess letters to uncover a hidden word. The game features:
- Random word selection
- Graphical interface with real-time updates
- Attempt tracking
- Win/lose notifications

## 🚀 Features

- 🔤 Guess letters to reveal the hidden word
- 📊 Track remaining attempts
- 📋 Display guessed letters
- 🔄 Start a new game at any time
- 🎲 Random word selection from a predefined list

## 🛠️ Prerequisites

- Python 3.7+
- Tkinter (typically included with Python standard library)

## 💾 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/qharny/GO2COD_PY_05.git
   cd GO2COD_PY_05
   ```

2. No additional dependencies required!

## 🎯 How to Play

1. Run the script:
   ```bash
   python main.py
   ```

2. Game Rules:
   - A random word is selected
   - Enter one letter at a time in the text field
   - Click "Guess" to submit your letter
   - You have 6 attempts to guess the entire word
   - Correctly guessed letters are revealed
   - Incorrect guesses reduce your remaining attempts

3. Game Buttons:
   - **Guess**: Submit a letter
   - **New Game**: Start a new game at any time

## 🔧 Customization

### Word List
Modify the `word_list` in the `HangmanGame` class to add or change words:

```python
word_list = [
    "python", "programming", "computer", 
    "game", "hangman", "challenge", 
    "coding", "learning"
]
```

### Attempts
Change the `max_attempts` parameter to adjust difficulty:
```python
game = HangmanGame(max_attempts=5)  
```


## 🎈 Acknowledgments

- Inspired by the classic Hangman word-guessing game
- Built with Python and Tkinter
- Thanks for GO2COD for the internship oppoturnity

## 📞 Contact

Your Name - kabuteymanasseh5@gmail.com

Project Link: [https://github.com/qharny/GO2COD_PY_05](https://github.com/qharny/GO2COD_PY_05)