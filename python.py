                                            
                                            #My python class starts
import sys              #Load a library Module
import random           #Imports Random Lib.
import math             #This imports Math Module
from myfile import M, N, O
from myfile import title
import myfile
print(sys.platform)
print(2**5)             #Raise 2 to power 5

X = "Spam!"
print(X*8)              #String repetition
print(X + 'NI!')
print(X.__add__('NI!'))

is_published = True
is_published = False       #boolean

split = """aaaaaaaabbb'''bbbbbbbb""bbbbbbbb'bbbccccccc"""
print(split)
split = '\naaaaaaa\nbbb\'\'\'bbbbbbb""bbbbbb\'bbbb\ncccccc\n'
print(split)

Days = "Today is Thursday"
print(Days)

#CONCATINATION
Name = input("Enter your Name: ")
Age = input("Enter your Age: ")
newAge = int(Age) + 15
greating = input("Write a greating: ")
print('Your New age is ' + str(newAge))
print(greating)


Full_Name = input('What is your Full Name? ')
Your_Color = input('what is your best color? ')
print(Full_Name + " likes " + Your_Color)

Full_Name = 'John Michael'
Age = '20'
is_new = True
print(Full_Name + ' is ' + Age)

birth_year = input('what is your birth year? ')
age = 2022 - int(birth_year)
print(age)

weight_in_pounds = input('what is your weight in pounds? ')
weight_in_kg = int(weight_in_pounds) * float(0.45)                  #concatinating string and float
print(weight_in_kg)

#FETCHING THE INDEX OF A CHARACTER IN A STRING
python_tutorial = "I want to learn this python, God Please help me"
print(python_tutorial[0])                             #This helps us to get the index of a character starting from the begining
print(python_tutorial[-1])                            #This helps us to get the index of a character starting from the end
print(python_tutorial[0:3])                           #This helps us to get the index of a character starting from index 0 to index 2 omitting index 3
print(python_tutorial[0:])                            #This helps us to get the index of a character starting from the begining to the end
print(python_tutorial[1:])                            #This helps us to get the index of a character starting from the second later to the end
print(python_tutorial[:7])                            #This helps us to get the index of a character starting from index 0 to index 6 omitting index 7

name = "Michael"
print(name[1:-1])                                    #This helps us to get the index of a character starting from index 1(I) to index second to the last omitting last index

#Formatted Strings
#FOrmatted strings are particularly useful where we want to dynamically generate some text from our variable.

First_Name ='John'
Last_Name ='Okechi'
Massage = First_Name + ' ['+ Last_Name +'] is Dead' #Concatination worked but it will be difficult if we have more lines of code
print(Massage)
#Now let's use formatted string. Note that the syntax is "f'{}'" {} is called place holder
msg = f'{First_Name} [{Last_Name}] is Dead'
print(msg)

#Using 3 quotation marks
introduction ='''
My name is Mr. D
I am a native of banyi
i wish to learn Python to change my status of life
Please God give me the grace to make it a habbit
'''
print(introduction)                                             #We use 3 quotation when we have multiple lines data.

#STRING METHODS
#To print the number of character in a string
course = "    learning a new programming language call python"
print(len(course))
power = len(str(2**1000000))       #To set the lenght of returned value
print(power)
print(course.lower())              #To set the characters to lower case
print(course.upper())              #TO SET THE CHARACTERS TO UPPER CASE
print(course.find('call'))         #This helps us to find the word call gives the INDEX of the first letter in 'call'
print(course[36:-7])
print(course.replace('call', 'named'))   #Finds 'call' in the string assigned to course and replace it with 'named'
print(course.isalpha())                   #Content test: isalpha returns boolian value "TRUE" if true else false
print(course.isnumeric())                       #Content test: isnumeric
print(course.isdigit())
print(course.title())               #This makes all the first letter capital
print(course.strip())               #This helps to clear all the spaces
Line = 'mymymy,yesyes,nono,youyouyou,ususus'
print(Line.split(','))        #Split the values asigned to Line
print(Line.rstrip())
print(Line.rstrip().split(','))

#There are times you want to check the existence of a Character or
# a squence of characters in your string, in those situaltion you use 'in operator'
print("programming language" in course) #This is called boolian statement. This line of code will search for "programing language" in the values asigned to "course". It returns true if found else return False                                          #Note that the different between 'in' and 'find' is that 'in' returns boolian value while 'find' returns the 'index' of the character
#ARITHIMETIC OPRERATIONS
# In python we have two type of number
# *Integer (int) whole numbers and Float (Value with decimal places)
print(3 + 4)          #ADDITON
print(10 - 4)           #SUBTRACTION
print(3 * 4)                #MULTIPLICATION
print(15 / 3)                   #DIVISION
print(5 // 4)                       #INTEGER DIVITION
print(4 % 3)         #THIS RETURNS THE REMENDER OF THE DIVITION VALUE
print(10 ** 3)                              #THIS IS EXPONENCIAL
X = 10
X = X + 10
X += 10          #AUGUMENTED ASSIGNMENT OPERATOR (Adding 10 to X as in line above).
X -= 5           #AUGUMENTED ASSIGNMENT OPERATOR (Subtractin 5 from X).
print(X)

#OPPERATOR PRECEDENCE
print(20 - 10/5*3**2)   #Python calculates the values in parantecis first,
                        #then exponential is in (BODMAS)
print((20-10)/5*3**2)
#THE ORDER IS AS FOLLOWS
#Bracket ()
#Exponential (3**2)
#Multiplication or Division
#Addition or Subtraction

#MATH FUNCTION
#ROUND FUNCTION: THIS IS USED TO ROUND A FLOAT TO INT
X = 2.9
print(round(X))

#ABSOLUTE FUNCTION (abs): THHIS RETURN THE POSITIVE REPRESENTATIVE OF VALUE EVEN IF IT IS A NEGETVE VALUE
X = -30
print(abs(X))

#MATH MODULE (for you to use Math Module, You need to import the module)

Food = bytearray(b'Fish')
Food.extend(b'roll')
print(Food)
print(Food.decode())

Fruit = "shrubbery"
L = list(Fruit)             #Helps to list the string assigned to fruit letter by letter
L[1] = 'c'                  #Replaces h with c
#''.join(L)

print(7)
print(random.choice(['cassava', 'cocoyam', 'corn', 'potatoes', 'plantain', 'yam', 'igbagwu', 'okpa', 'beans', 'rice']))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(L)
#print(''.join(L))

print(len(Days))        #Prints the lenght of the content of Days

M = "Death"
N = "Or"
O = "Life"
print(M, N, O)

print("spam!"*8)         #prints spam! in multiple of 8

for x in 'spam!':
    print(x)

Man = 4 > 9
print (Man)

print(myfile.title)
print(title)
print(M, N, O)
print(M, N)
print(myfile)
#Axis = u'x' + b'y'
#print (Axis)
