# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 15:10:09 2022

@author: gabri
"""

#999-999-9999
# index 0-2 should be digits 
#index 3 should be -
#index 4-6 should be digits
#index 7 should be -
#index 8-11 should be digits

#initialize Boolean variables
correct_length = False
has_digit = False
has_dash = False

phone_number = str(input('Enter a phone number in the following format, XXX-XXX-XXXX: '))


#checks the correct length of the password
if len(phone_number) == 12:
    correct_length = True
    #checks indexes of the string if they are digits
    if phone_number[0:3].isdigit() and phone_number[4:7].isdigit() and phone_number[8:12].isdigit():
        has_digit = True
    #checks if indexes 3 and 7 are "-" 
    if phone_number[3] and phone_number[7] == '-':
        has_dash = True


if correct_length and has_digit and has_dash:
    print('ruh ruh ringtone pick up the phone')
else: 
    print('invalid format')
