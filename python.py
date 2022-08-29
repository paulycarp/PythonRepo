#My python class starts
from myfile import M, N, O
from myfile import title
import myfile
import sys              #Load a library Module
import random           #Imports Random Lib.
print(sys.platform)
print(2**5)             #Raise 2 to power 5

X = "Spam!"
print(X*8)              #String repetition
print(X + 'NI!')
print(X.__add__('NI!'))

is_published = True
is_published = False       #booleans 

msg = """aaaaaaaabbb'''bbbbbbbb""bbbbbbbb'bbbccccccc"""
print(msg)
msg = '\naaaaaaa\nbbb\'\'\'bbbbbbb""bbbbbb\'bbbb\ncccccc\n'
print(msg)

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
Python_Tutoria = "I want to learn this python, God Please help me"
print(Python_Tutoria[0])                             #This helps us to get the index of a character starting from the begining
print(Python_Tutoria[-1])                            #This helps us to get the index of a character starting from the end
print(Python_Tutoria[0:3])                           #This helps us to get the index of a character starting from index 0 to index 2 omitting index 3
print(Python_Tutoria[0:])                            #This helps us to get the index of a character starting from the begining to the end
print(Python_Tutoria[1:])                            #This helps us to get the index of a character starting from the second later to the end
print(Python_Tutoria[:7])                            #This helps us to get the index of a character starting from index 0 to index 6 omitting index 7

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
course = "Learning a new programming language call Python"
print(len(course))
power = len(str(2**1000000))       #To set the lenght of returned value
print(power)
print(course.lower())              #To set the characters to lower case
print(course.upper())              #TO SET THE CHARACTERS TO UPPER CASE
print(course.find('call'))         #This helps us to find the word call gives the INDEX of the first letter in 'call'
print(course[36:-7])
print(course.replace('call', 'named'))   #Finds 'call' in the string assigned to course and replace it with 'named'

#There are times you want to check the existence of a Character or a squence of characters in your string, in those situaltion you use 'in operator'
print('programming language' in course) #This is called boolian statement. This line of code will search for "programing language" in the values asigned to "course". It returns true if found else return False
                                            #Note that the different between 'in' and 'find' is that 'in' returns boolian value while 'find' returns the 'index' of the character
Food = bytearray(b'Fish')
Food.extend(b'roll')
print(Food)
print(Food.decode())

Fruit = "shrubbery"
L = list(Fruit)             #Helps to list the string assigned to fruit letter by letter
L[1] = 'c'                  #Replaces h with c
#''.join(L)

Line = 'mymymy,yesyes,nono,youyouyou,ususus'
print(Line.split(','))        #Split the values asigned to Line
print(Line.rstrip())
print(Line.rstrip().split(','))

Life = 'mistery'
print(Life.isalpha())        #Content test: isalpha
print(Life.isnumeric())      #Content test: isnumeric
print(Life.isdigit())

print(7)
print(random.choice(['cassava', 'cocoyam', 'corn', 'potatoes', 'plantain', 'yam', 'igbagwu', 'okpa', 'beans', 'rice']))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(L)
#print(''.join(L))              

a = 3
b = 5
print(a+b)
print(len(Days))        #Prints the lenght of the content of Days

M = "Death"
N = "Or"
O = "Life"
print(M, N, O)

print(20 - 10/5*3**2)

print((20-10)/5*3**2)

print("spam!"*8)         #prints spam! in multiple of 8 

for x in 'spam!':
    print(x)

print(myfile.title)
print(title)
print(M, N, O)
print(M, N)
print(myfile)