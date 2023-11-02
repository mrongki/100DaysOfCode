from random import randint
from art import logo
import os

HARD_DIFFICULTY = 5
EASY_DIFFICULTY = 10

def set_difficulty():
    """Returns the number of turns based on difficulty"""
    level = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
    if level == 'hard':
        return HARD_DIFFICULTY
    elif level== 'easy':
        return EASY_DIFFICULTY


def check_num(guess, answer, turns):
    """Returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it. The answer was {answer}")


def game():
    os.system('cls')
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Generate a random integer
    answer = randint(1,100)
    # print(answer) # Uncomment for debugging
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_num(guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses, you lose. The answer was {answer}.")
            return
        elif guess != answer:
            print("Guess again.")

game()
