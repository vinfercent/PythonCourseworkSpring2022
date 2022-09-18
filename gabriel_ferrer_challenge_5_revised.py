# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:33:20 2022

@author: gabri
"""

# this program calculates the distance an object has traveled in free fall per second
# GRAVITY is a global constant that represents gravity
GRAVITY = 9.8

def main():
    #print the greeting message & detail what the program does
    print('Hello! This program determines the distance per second an')
    print('object in free fall has fallen after a given amount')
    print('of seconds is provided by the user.')
    print()
    #ask the user to enter the amount of time the object will be falling
    time_of_fall = int(input('How many seconds do you want the object to fall for: '))
    
    #call the fallingDistance function passing time_of_fall as an argument
    fallingDistance(time_of_fall)

def fallingDistance(time):
    #calculate the distance traveled at EACH moment in time
   for i in range(1, time + 1):
       distance_traveled_per_second = (0.5 * GRAVITY * i**2)
       print(f'{distance_traveled_per_second} m')
    
#call the main function
main()