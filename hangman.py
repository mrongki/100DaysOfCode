import random, os
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
is_gameover = False
chosen_word = random.choice(word_list)
lives = 6

print('for debugging: ' + chosen_word)

display = []
for _ in range(len(chosen_word)):
    display.append('_')


while not is_gameover:
    
    guess = input('Guess a letter: ').lower()
    os.system('cls')
    print(logo)
    while not len(guess) == 1 or not guess.isalpha():
        print(stages[lives])
        print(' '.join(display))
        guess = input('Invalid input, enter one letter only: ')
        os.system('cls')
    
    # If guess is not in chosen_word, minus one life
    if guess not in chosen_word:
        print(f'You guessed "{guess}", that\'s not in the word. You lose a life.')
        lives -= 1
        # if you ran out of lives, you lose the game
        if lives == 0:
            is_gameover = True
            print('You lose.' + 'The word is ' + chosen_word)
    elif guess in display:
        print(f'You\'ve already guessed "{guess}".')   
    # Update display to show current game state
    for i in range(len(chosen_word)):
        # Compare each letter of chosen_word to guess letter
        if chosen_word[i] == guess:
            # Assign guess letter to corresponding index of display
            display[i] = guess
    
    # If all underlines have been replaced by letters you win the game
    if '_' not in display:
        is_gameover = True
        print('You win.')
    # Print display
    print(' '.join(display))
    # Print ASCII art of stages
    print(stages[lives])
    
