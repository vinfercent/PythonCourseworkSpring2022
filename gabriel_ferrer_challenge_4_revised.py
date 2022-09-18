# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 19:48:46 2022

@author: gabri
"""

GRAND_PRIZE = 'a RTX 3090' # the grand prize for guessing the correct number
SMALL_PRIZE = 'a Free Steam Card' #the minor prize for guess within 5 digits of the correct number
CORRECT_GUESS = 25 # the correct guess

# ask the user if they want to play a game
decision = input('Do you want to play a game? ')
if decision.lower() == 'yes':
   choice = 'yes' 
else:
    choice = 'no'
    print("What a shame. You're missing out on some good prizes. Goodbye.", '\n')

# assign accumulators for total number of guesses
total = 0 # total number of guesses
incorrect_total = 0 # total number of incorrect guesses

#allow the user to have unlimited attempts to play the game 
while choice == 'yes':
    guess = int(input('Guess a number between 1-50: '))
    while guess < 1 or guess > 50:
        print('ERROR: Only numbers between 1-50 are permitted.')
        guess = int(input('Guess a number between 1-50: '))
        total += 1
    if (guess >= 20 and guess <= 24) or (guess >= 26 and guess <= 30):
        print(f'You were so close to the grand prize, take {SMALL_PRIZE}.')
        choice = input('Do you want to guess again? please type yes or no: ')
        incorrect_total += 1
        total += 1
    elif (guess >= 1 and guess <= 19) or (guess >= 31 and guess <= 50):
        print('Your guess did not qualify for a prize.')
        choice = input('Would you like to guess again? please type yes or no: ')
        incorrect_total += 1
        total += 1
    elif guess == CORRECT_GUESS:
        print(f'You have won the grand prize, {GRAND_PRIZE}.')
        choice = input("Please type 'end' to end the game: ")
        total += 1
        
        
print(f'You attempted this game {total} times.', '\n')
print(f'You guessed incorrectly {incorrect_total} times', '\n')