import random


def guess(x):
    """This function generates a random number between 1 and x for the user"""
    random_number = random.randint(1, x)
    guess = 0  # initialize our variable
    # We want to loop as long as the guess is false and break when the guess is right
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        # We want the program to give us a clue
        if guess < random_number:
            print("Sorry! Guess again, too low.")
        elif guess > random_number:
            print("Sorry! Guess again, too high.")
    print(
        f"Yay!! Congrats. You have guessed the random number {random_number} correctly.")


guess(10)
