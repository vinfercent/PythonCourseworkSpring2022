# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 09:10:30 2022

@author: gabri
"""

def Database(name, location, value):    
    
    saved_database = []    #WE ARE CREATING AN EMPTY LIST HERE
    
    inFile = open(r'C:\Users\gabri\OneDrive\Desktop\StudentGradeBook.txt', 'r')     #HERE WE ARE OPENING A FILE IN READ MODE
    
    for lines in inFile:    #WE ARE GOING TO LOOP THROUGH EVERY LINE IN THE FILE
        
        saved_database.extend(lines.split('\t'))    #WE ARE SAVING EACH ITEM SEPARATED WITH A TAB TO A LOCATION IN THE LIST
        
    print(saved_database)
    
    print('\n------------------------------')
    inFile.close()
    
# COMPLETE THIS SECTION USING A DECISION STRUCTURE TO SEE IF THE NAME IS CONTAINED IN THE DATABASE.
#IF IT IS, THEN YOU MUST FIND THE INDEX VALUE AND #REPLACE THE APPROPRIATE GRADE.  
#IF THE NAME IS NOT IN THE DATABASE, TELL THE USER IT WAS NOT FOUND IN THE GRADEBOOK. 
    
    name = input('What student are you looking for? ')
                
    if name in saved_database:
        value = input('What grade do you want to replace for them? ')
        if value in saved_database:
            #code finding the index value and replacing the appropriate grade
            location = saved_database.index(value)
            print(location)
    else:
        print('That student was not found.')
    
        
    with open(r'C:\Users\gabri\OneDrive\Desktop\StudentGradeBook.txt', 'w') as f:       #OPEN THE FILE IN WRITE MODE
         
         for elements in saved_database:   #ITERATE THROUGH EVERY ELEMENT IN THE DATABASE
             
             f.write('%s\t' % elements)   #WRITE EACH VALUE TO THE DATABASE BACK INTO DELIMITED FORM.  
             
             
    f.close()
    
    #new grade = input('Enter the students new grade: ')
    
    
def ChangingGrades():
    
    #This function will let the user access the working_database and change any 
    #grade contained in the function
    new grade = Database(student, index, past_grade)
    
    

#YOU MUST COMPLETE THIS SECTION OF THE CODE ON YOUR OWN.
#DO NOT USE THE SAME NAME FOR THE VARIABLES IN THE PARAMATER FIELD OF THE  DATBASE() #FUNCTION.
#REMEMBER YOU MUST CALL THE DATABASE FUNCTION AND PASS THE SAME NUMBER OF ARGUMENT, IN THIS CASE 3.  
#ONE FOR THE STUDENTS NAME, #ONE FOR THE GRADE NUMBER YOU ARE CHANGING, AND ONE FOR THE NEW GRADE VALUE.      
    pass  #YOU CAN REMOVE THIS ONCE THE FUNCTION IS COMPLETE
if __name__ == '__main__':
    ChangingGrades()