import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0

    while True:
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the guess
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    number_guessing_game()
