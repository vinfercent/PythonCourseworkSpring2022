# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:28:22 2022

@author: gabri
"""

# creating an RPG with the PlayerCharacter class

class PlayerCharacter:
    
    #intialize the attributes of the class
    
    def __init__(self, health, armor_rating, attack_power):
        self.__health = health
        self.__armor_rating = armor_rating
        self.__attack_power = attack_power
    
    def set_health(self, health):
        self.__health = health
    
    def set_armor_rating(self, armor_rating):
        self.__armor_rating = armor_rating
    
    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power
    
    #this block of methods returns the value of each respective attribute when called.
    def get_health(self):
        return self.__health
    def get_armor_rating(self):
        return self.__armor_rating
    def get_attack_power(self):
        return self.__attack_power

def main():
    # print a small greeting to the user
    print('Welcome to the Wizard 101 Create a Character Menu!')
    
    # each attribute has a block of code that asks for user input and validates the correct range
    # with a while loop.
    hp = int(input('Enter the amount of health: '))
    while hp < 1 or hp > 100:
        print('Health can be only be from 1-100, please try again.')
        hp = int(input('Enter the amount of health: '))

    armor = int(input('Enter the armor rating: '))
    while armor < 1 or armor > 20:
        print('Armor Rating can be only be from 1-20, please try again.')
        armor = int(input('Enter the amount of armor: '))

    attack = int(input('Enter the attack power: '))
    while attack < 1 or attack > 20:
        print('Attack Power can be only be from 1-20, please try again.')
        attack = int(input('Enter the amount of attack power: '))
    
    
    #create an object from the PlayerCharacter class
    Wizard = PlayerCharacter(hp, armor, attack)
    
    #display the attributes of the Wizard
    print('Your wizard has the following build:')
    print()
    print(f'Health: {Wizard.get_health()}')
    print(f'Armor Rating: {Wizard.get_armor_rating()}')
    print(f'Attack Power: {Wizard.get_attack_power()}')

if __name__ == '__main__':
    main()
    
    
        
        
        
        
        