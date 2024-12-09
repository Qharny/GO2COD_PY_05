import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, word_list=None, max_attempts=6):
        """
        Initialize the Hangman game
        
        :param word_list: List of words to choose from. If None, uses a default list.
        :param max_attempts: Maximum number of incorrect guesses allowed
        """
        # Default word list if none provided
        if word_list is None:
            word_list = [
                "python", "programming", "computer", "game", 
                "hangman", "challenge", "coding", "learning"
            ]
        
        # Select a random word
        self.word = random.choice(word_list).lower()
        
        # Track game state
        self.guessed_letters = set()
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts
        
        # Create initial word display with underscores
        self.word_display = ['_' for _ in self.word]
    
    def guess_letter(self, letter):
        """
        Process a letter guess
        
        :param letter: The letter guessed by the player
        :return: Tuple (is_correct_guess, is_game_over, game_result)
        """
        # Normalize the guess
        letter = letter.lower()
        
        # Check if letter was already guessed
        if letter in self.guessed_letters:
            return False, False, None
        
        # Add to guessed letters
        self.guessed_letters.add(letter)
        
        # Check if letter is in the word
        if letter in self.word:
            # Update word display
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_display[i] = letter
            
            # Check if word is completely guessed
            if '_' not in self.word_display:
                return True, True, "win"
            
            return True, False, None
        
        # Incorrect guess
        self.remaining_attempts -= 1
        
        # Check if out of attempts
        if self.remaining_attempts == 0:
            return False, True, "lose"
        
        return False, False, None
    
    def get_current_state(self):
        """
        Get the current state of the game
        
        :return: A tuple containing current word display and remaining attempts
        """
        return ''.join(self.word_display), self.remaining_attempts

class HangmanGUI:
    def __init__(self, master):
        """
        Initialize the Hangman GUI
        
        :param master: The root Tkinter window
        """
        self.master = master
        master.title("Hangman Game")
        master.geometry("400x500")
        
        # Initialize game
        self.game = HangmanGame()
        
        # Word display
        self.word_label = tk.Label(
            master, 
            text=self.format_word_display(), 
            font=("Courier", 24)
        )
        self.word_label.pack(pady=20)
        
        # Attempts left
        self.attempts_label = tk.Label(
            master, 
            text=f"Attempts left: {self.game.remaining_attempts}", 
            font=("Arial", 16)
        )
        self.attempts_label.pack(pady=10)
        
        # Guessed letters
        self.guessed_label = tk.Label(
            master, 
            text="Guessed letters: ", 
            font=("Arial", 12)
        )
        self.guessed_label.pack(pady=10)
        
        # Letter entry
        self.entry = tk.Entry(master, font=("Arial", 16), width=5)
        self.entry.pack(pady=10)
        
        # Guess button
        self.guess_button = tk.Button(
            master, 
            text="Guess", 
            command=self.process_guess
        )
        self.guess_button.pack(pady=10)
        
        # New game button
        self.new_game_button = tk.Button(
            master, 
            text="New Game", 
            command=self.start_new_game
        )
        self.new_game_button.pack(pady=10)
    
    def format_word_display(self):
        """
        Format the word display with spaces between letters
        
        :return: Formatted word display string
        """
        return ' '.join(self.game.word_display)
    
    def process_guess(self):
        """
        Process the player's letter guess
        """
        # Get and validate guess
        guess = self.entry.get().strip().lower()
        self.entry.delete(0, tk.END)
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        
        # Process the guess
        is_correct, is_game_over, result = self.game.guess_letter(guess)
        
        # Update display
        self.word_label.config(text=self.format_word_display())
        self.attempts_label.config(
            text=f"Attempts left: {self.game.remaining_attempts}"
        )
        
        # Update guessed letters
        guessed_letters = ' '.join(sorted(self.game.guessed_letters))
        self.guessed_label.config(text=f"Guessed letters: {guessed_letters}")
        
        # Check game status
        if is_game_over:
            if result == "win":
                messagebox.showinfo("Congratulations!", f"You won! The word was {self.game.word}.")
            else:
                messagebox.showinfo("Game Over", f"You lost. The word was {self.game.word}.")
            
            # Disable guess button
            self.guess_button.config(state=tk.DISABLED)
    
    def start_new_game(self):
        """
        Start a new Hangman game
        """
        # Reset game
        self.game = HangmanGame()
        
        # Reset display
        self.word_label.config(text=self.format_word_display())
        self.attempts_label.config(
            text=f"Attempts left: {self.game.remaining_attempts}"
        )
        self.guessed_label.config(text="Guessed letters: ")
        
        # Re-enable guess button
        self.guess_button.config(state=tk.NORMAL)

def main():
    """
    Main function to run the Hangman GUI
    """
    root = tk.Tk()
    hangman_gui = HangmanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()