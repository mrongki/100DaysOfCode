from art import logo
import os, random


def deal_card():
    '''Returns a random card'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calc_score(hand):
    '''Input: List of cards. Returns 0 for Blackjack, returns score otherwise'''
    if len(hand) == 2 and sum(hand) == 21:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare(user_score, comp_score):
    if comp_score == 0:
        return 'Lose, Dealer has Blackjack 😱'
    elif user_score == 0:
        return 'Win with a Blackjack 😎'
    elif user_score == comp_score:
        return 'Draw 🙃'
    elif user_score > 21:
        return 'You went over. you lose 😭'
    elif comp_score > 21:
        return 'Opponent went over. you win 😁'
    elif user_score > comp_score:
        return 'You win 😃'
    else:
        return 'You lose 😤'

def play_blackjack():
    # Initial deal
    print(logo)
    user_cards = []
    user_is_done = False
    comp_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    # User's turn to play
    while not user_is_done:
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)
        print(f'\tYour cards: {user_cards} Your current score: {user_score}')
        print(f'\tComputer cards: [{comp_cards[0]}, *]')

        # If anyone gets a Blackjack, the game is over.
        # If user goes over 21 he/she loses.
        if user_score > 21 or user_score == 0 or comp_score == 0:
            user_is_done = True
        elif input('Would you like to draw another card? "y" or "n": ').lower() == 'y':
            user_cards.append(deal_card())
        else:
            user_is_done = True

    # Computer's turn to play
    while comp_score < 17 and comp_score !=0 and user_score <= 21 and user_score != 0:
        # Deal another card to computer and update computer's score
        comp_cards.append(deal_card())
        comp_score = calc_score(comp_cards)

    print(f'Your final cards: {user_cards}\nFinal score: {user_score}')
    print(f'Computer\'s final cards: {comp_cards}\nFinal score: {comp_score}')
    print(compare(user_score, comp_score))

while input("Do you want to play Blackjack? ('y' or 'n'): ").lower() == 'y':
    os.system('cls')
    play_blackjack()
