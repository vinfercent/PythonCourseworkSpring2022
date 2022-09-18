# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 15:17:21 2022

@author: gabri
"""
GRAND_PRIZE = 'a RTX 3090' # the grand prize for guess the exact number
SMALL_PRIZE = 'a Free Steam Card' # the secondary prize
CORRECT_GUESS = 25

# Ask the user if they want to play a game
choice = input('Do you want to play a game? ')

if choice.lower() == 'yes':
    guess = int(input('Guess a number between 1-50: '))
    if (guess >= 20 and guess <= 24) or (guess >= 26 and guess <= 30):
        print(f'Valiant attempt, your efforts will be rewarded with {SMALL_PRIZE}.')
    elif guess == CORRECT_GUESS:
        print(f'You have won a highly coveted item, {GRAND_PRIZE}!')
    else:
        print('Sorry, wrong guess. Better luck next time. ')

else:
    print('Goodbye then.')
