import random

MAX_GUESSES = 4
MIN_NUMBER = 1
MAX_NUMBER = 10

def number_guessing_game():
    answer = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_guesses = 0

    while num_guesses < MAX_GUESSES:
        try:
            user_guess = int(input(f"Enter an integer to guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if not MIN_NUMBER <= user_guess <= MAX_NUMBER:
            print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
            continue

        if user_guess == answer:
            print(f"Congrats that you guessed the number correctly")
            break
        elif user_guess < answer:
            print("Try a higher number.")
        elif user_guess > answer:
            print("Try a lower number.")

        num_guesses += 1
        remaining_guesses = MAX_GUESSES - num_guesses
        if remaining_guesses > 0:
            print(f"You have {remaining_guesses} {'guesses' if remaining_guesses > 1 else 'guess'} remaining.")
        else:
            print(f"You have {remaining_guesses} remainging.")

if __name__ == '__main__':
    number_guessing_game()
