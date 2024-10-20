import random
import tkinter as tk
from tkinter import messagebox

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")

        # Random number between 1 and 100
        self.number = random.randint(1, 100)
        self.attempts = 7

        # GUI Elements
        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.attempts_label = tk.Label(root, text=f"Attempts left: {self.attempts}")
        self.attempts_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return

        if guess < 1 or guess > 100:
            messagebox.showwarning("Out of Range", "Please enter a number between 1 and 100.")
        elif guess > self.number:
            messagebox.showinfo("Hint", "Too high!")
        elif guess < self.number:
            messagebox.showinfo("Hint", "Too low!")
        else:
            messagebox.showinfo("Congratulations!", f"You've guessed the number {self.number} correctly!")
            self.root.destroy()
            return

        self.attempts -= 1
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")
        if self.attempts == 0:
            messagebox.showinfo("Game Over", f"Out of attempts! The correct number was {self.number}.")
            self.root.destroy()

# Main execution for GUI
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
