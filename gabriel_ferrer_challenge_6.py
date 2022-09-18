# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 18:52:13 2022

@author: gabri
"""

def main():
    FileControl()
    
def FileControl():
    #import the FunWithFiles.txt
    movie_file = open(r'C:\Users\gabri\OneDrive\Desktop\FunWithFiles.txt', 'r')
    
    #read each line from the FunWithFiles.txt and store them into a variable
    line1 = movie_file.readline()
    line2 = movie_file.readline()
    line3 = movie_file.readline()
    
    #close the FunWithFiles.txt
    movie_file.close()
    
    #print the contents of FunWithFiles.txt
    print('These are the contents of the FunWithFiles.txt file:', '\n')
    print(line1)
    print(line2)
    print(line3)
    
    #ask the user what their favorite movie is
    fav_movie = input('What is your favorite movie? ')
    
    #open the FunWithFiles.txt in append mode
    movie_file = open(r'C:\Users\gabri\OneDrive\Desktop\FunWithFiles.txt', 'a')
    
    #append the user's favorite movie into the FunWithFiles.txt
    movie_file.write(fav_movie + '\n')
    
    #close FunWithFiles.txt
    movie_file.close()
    
    #tell the user that their favorite movie has been added to the FunWithFiles.txt file
    print('Your favorite movie was added to the FunWithFiles.txt file!')

#call the main function
if __name__ == '__main__':
    main()
