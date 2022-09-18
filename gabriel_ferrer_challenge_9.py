# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:23:48 2022

@author: gabri
"""

def menu(choice):
    #choice = input('Would you like to add a new student to the gradebook or access the grades of a current student? (y/n): ')
    
    if choice.lower() == 'y':
        AddStudent()
    else:
        print('Goodbye')
    

def AddStudent():
    student_name = input("Enter the student's name: ")
    
    grade_list = [] #creates an empty list for the student's grades 
    
    StudentGradeBook(student_name, grade_list) #pass student_name and grade_list as arguments to the StudentGradeBook function
    

def StudentGradeBook(name, grade_value):
    grade_book = {'Gina': [100, 90, 10], 'Tina': [45, 50, 48], 'Rob': [78, 84, 82]}
    
    #display the grades of the student if they are already in the dictionary
    if name in grade_book:
        print(f'These are the grades of {name}', grade_book[name] )
        
        decision = input('Would you like to change any of their grades? (y/n): ') #ask the user if they want to change a grade
        if decision.lower() == 'y': 
            
            grade_change = int(input("Which grade do you want to change? "))
            grade_change = grade_change - 1 # places the grade to be changed within the proper index of the grade list
            new_value = int(input("Enter the new grade: "))
        
            for key in grade_book:
                grade_book[name][grade_change] = new_value
        
            print(grade_book)
        
        else: #runs if decision is anything other than 'y'
            print('Goodbye')
    
    #adds the new student to the grade_book dict.    
    if name not in grade_book: 
        
        choice = 'y' #set a variable and accumulator to initiate/control the while loop
        total = 0
        while choice == 'y' and total < 3: #this while loop allows the user to enter 3 grades into the grade_list
            grade = int(input('Enter a grade: '))
            grade_value.append(grade)
            total += 1
        grade_book[name] = grade_value
        
    print(grade_book)
        
    
    

if __name__ == '__main__':
    choice = input('Would you like to add a new student to the gradebook or access the grades of a current student? (y/n): ')
    menu(choice)