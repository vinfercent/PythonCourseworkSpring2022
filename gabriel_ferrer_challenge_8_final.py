# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:41:08 2022

@author: gabri
"""

def main():
    getUserPass()
    
    
def getUserPass():
    #obtain user input for a username and password
    user_name = str(input('Please enter a username: '))
    user_pass = str(input('Please enter a password: '))
    passwordDatabase = ['123456', '123456789', '12345', 'qwerty', 'password',
                        '12345678', '111111', '123123', '1234567890', '1234567', 
                        'qwerty123', '000000', '1q2w3e', 'aa12345678', 'abc123', 
                        'password1', '1234', 'qwertyuiop', '123321', 'password123', 
                        '1q2w3e4r5t', 'iloveyou', '654321', '666666', '987654321', 
                        '123', '123456a', 'qwe123', '1q2w3e4r', '7777777',
                        '1qaz2wsx', '123qwe', 'zxcvbnm', '121212', 'asdasd', 
                        'a123456', '555555', 'dragon', '112233', '123123123', 
                        'monkey', '11111111', 'qazwsx', '159753', 'asdfghjkl',
                        '222222', '1234qwer', 'qwerty1', '123654', '123abc']
    
    #pass user_pass as an argument to valid_password(password)
    password = valid_password(user_pass)
    
    print(password)
    
    #pass user_pass as an argument to StoredPasswords(checkPass)
    result = StoredPasswords(user_pass, passwordDatabase)
    
    print(result)
    
    #show the user's password was appended to the list
    base = insert_password(user_pass, passwordDatabase)
    print(base)
    
#the valid_password function accepts user_pass as an argument and returns true or false
# to indicate whether the password is valid.

#a valid password is at least 8 characters in length, contains one uppercase letter and,
#one lowercase letter, one digit, and one special character from the valid_char list.
#invalid_char is a list of invalid characters 

def valid_password(password):
    
    valid_char = ['!', '@', '%', '^', '&', '*', '(', ')']
    invalid_char = ['#', '$', '_', '-', '+', '=']
    
    #set the boolean variables to false
    #has_invalid_char is set to True 
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_valid_char = False
    has_invalid_char = True
    
    #begin the validation process by testing the password's length
    if len(password) >= 8:
        correct_length = True
        
        #test each character and set the appropriate flag when a
        #required character is found.
        for char in password:
            if char.isupper():
                has_uppercase =  True
            if char.islower():
                has_lowercase = True
            if char.isdigit():
                has_digit = True
            if char in valid_char:
                has_valid_char = True
            if char in invalid_char:
               has_invalid_char = False
    
    #determine if all the requirements are True. If so, return the appropriate message.
    if correct_length and has_uppercase and has_lowercase and \
        has_digit and has_valid_char and has_invalid_char:
        is_valid = 'Your password is valid.'
        return is_valid
    else:
        not_valid = 'Your password is invalid.'
        return not_valid
    

# the StoredPasswords(checkPass) function checks to see if user_pass is in the passwordDatabase list  
def StoredPasswords(checkPass, passwordDatabase):
   
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

def insert_password(user_pass, passwordDatabase):
    
    #append user_pass to passwordDatabase
    passwordDatabase.append(user_pass)
    return passwordDatabase
    

if __name__ == '__main__':
    main()