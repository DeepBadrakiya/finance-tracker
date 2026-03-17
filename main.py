#!/usr/bin/env python3
"""A simple number guessing game."""

import random


def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.\n")

    secret = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a number.\n")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"\nYou got it in {attempts} attempt(s)! The number was {secret}.")
            return

        if attempts < max_attempts:
            print(f"Attempts left: {max_attempts - attempts}\n")

    print(f"\nOut of attempts. The number was {secret}. Better luck next time!")


if __name__ == "__main__":
    main()
