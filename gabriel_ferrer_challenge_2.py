# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 19:42:12 2022

@author: gabri
"""

# Ask the user to enter their name
name = input('Hello, what is your name? ')

# Ask the user to enter their birth year
birth_year = int(input('In what year were you born? '))

# Use the user's birth year to determine their current age
age = 2022 - (birth_year)

# Print the user's name, birth year, and current age
print(f'Your name is {name}. ' +
      f'"You were born in {birth_year}. ' +
      f'That makes you approximately {age} years old."')
      