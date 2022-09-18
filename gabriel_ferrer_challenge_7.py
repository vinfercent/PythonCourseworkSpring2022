# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:27:45 2022

@author: gabri
"""

def main():
    getUserPass()
    
def getUserPass():
    #obtain user input for a username and password
    user_name = str(input('Please enter a username: '))
    user_pass = str(input('Please enter a password: '))
    
    #pass user_pass as an argument to StoredPasswords(checkPass)
    result = StoredPasswords(user_pass)
    
    print(result)

def StoredPasswords(checkPass):
    #create a tuple that stores the 50 most common passwords
    passwordDatabase = ('123456', '123456789', '12345', 'qwerty', 'password',
                        '12345678', '111111', '123123', '1234567890', '1234567', 
                        'qwerty123', '000000', '1q2w3e', 'aa12345678', 'abc123', 
                        'password1', '1234', 'qwertyuiop', '123321', 'password123', 
                        '1q2w3e4r5t', 'iloveyou', '654321', '666666', '987654321', 
                        '123', '123456a', 'qwe123', '1q2w3e4r', '7777777',
                        '1qaz2wsx', '123qwe', 'zxcvbnm', '121212', 'asdasd', 
                        'a123456', '555555', 'dragon', '112233', '123123123', 
                        'monkey', '11111111', 'qazwsx', '159753', 'asdfghjkl',
                        '222222', '1234qwer', 'qwerty1', '123654', '123abc')
    
    #check if user_pass is in passowordDatabase
    #if found, print the location of where the password is in the database
    if checkPass in passwordDatabase:
        checkPassIndex = passwordDatabase.index(checkPass)
        print(f'{checkPass} was found in the tuple at index {checkPassIndex}.')
        found = 'Your password is too common. Please consider changing it.'
        return found
    else:
        notFound = 'You have a strong password.'
        return notFound

if __name__ == '__main__':
    main()