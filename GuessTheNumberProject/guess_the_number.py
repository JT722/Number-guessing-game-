import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    # Set the range and the number of attempts
    number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 7  # Max number of attempts

    for i in range(attempts):
        try:
            guess = int(input(f"Attempt {i + 1}/{attempts} - Guess the number (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess < 1 or guess > 100:
            print("Your guess is out of range. Please guess a number between 1 and 100.")
        elif guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print(f"Congratulations! You've guessed the number {number} correctly in {i + 1} attempts!")
            break
    else:
        print(f"Sorry, you've used all {attempts} attempts. The correct number was {number}.")

# Main execution
if __name__ == "__main__":
    guess_the_number()
