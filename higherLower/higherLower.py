from random import choice
from art import logo, vs
from game_data import data
import os


def format_data(person):
    """Format the person data and return a printable format."""
    name = person['name']
    description = person['description']
    country = person['country']
    return f"{name}, a {description}, from {country}"

def guessIsCorrect(a_person, b_person, guess):
    """Take user guess and both persons and returns if they got it right."""
    if a_person['follower_count'] > b_person['follower_count']:
        return guess == 'a'
    elif b_person['follower_count'] > a_person['follower_count']:
        return guess == 'b'
    else:
        return

def play_game():
    score = 0
    game_over = False 
    b_person = choice(data) 
    shown_list = []
    shown_list.append(b_person)
    print(logo)
    while not game_over:
        a_person = b_person
        while b_person in shown_list and a_person == b_person:
            b_person = choice(data)
            shown_list.append(b_person)
        # for entry in shown_list: #FOR DEBUGGING shown_list
        #     print(entry['name'])
        print(f"Compare A: {format_data(a_person)}")
        print(vs)
        print(f"Against B: {format_data(b_person)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        os.system('cls')
        print(logo)
        if guessIsCorrect(a_person,b_person,guess):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}.")
    play_again = input("Press enter to exit or type 'Y' to play again: ").lower()
    if play_again == 'y':
        os.system('cls')
        play_game()

os.system('cls')    
play_game()
