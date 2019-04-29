# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:03:12 2019

@author: Sajitha

The question : https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

"""

import datetime

name= input("Please enter your name : ")
age = input("Please enter your age : ")
 
hundradyear = int(datetime.date.today().year) + (100 - int(age))

print("your name is " + name + " and you will be 100 on year " + str(hundradyear))

copycount = int(input("Please enter the number of copies need : "))

while copycount != 0:
    print("your name is " + name + " and you will be 100 on year " + str(hundradyear) + '\n')
    copycount -= 1
    
print ("End of program")    
    

