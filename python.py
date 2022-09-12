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
print(X * 8)              #String repetition
print(X + 'NI!')

IS_PUBLISHED = True
IS_PUBLISHED = False       #boolean

SPLIT = """aaaaaaaabbb'''bbbbbbbb""bbbbbbbb'bbbccccccc"""
print(SPLIT)
SPLIT = '\naaaaaaa\nbbb\'\'\'bbbbbbb""bbbbbb\'bbbb\ncccccc\n'
print(SPLIT)

DAYS = "Today is Thursday"
print(DAYS)
print(len(DAYS))        #Prints the lenght of the content of Days

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

FULL_NAME = 'John Michael'
AGE = '20'
IS_NEW = True
print(FULL_NAME + ' is ' + AGE)

FIRST = "PAULINUS"
LAST = "OKECHI"
FULLNAME = FIRST + " " + LAST
print(FULLNAME.title())

BIRTH_YEAR = input('what is your birth year? ')
AGE = 2022 - int(BIRTH_YEAR)
print(AGE)

weight_in_pounds = input('what is your weight in pounds? ')
weight_in_kg = int(weight_in_pounds) * float(0.45)                  #concatinating string and float
print(weight_in_kg)

#FETCHING THE INDEX OF A CHARACTER IN A STRING
#LIST
NAME = "Michael"
print(NAME[1:-1])   #The block parentaces helps us to get the index of a character starting from the second letter through to second to the last

MINE = [123, 'Mmine', 1.23]
print (MINE[0])
print (MINE + [1, 2, 3,])
print (MINE * 3)
print (MINE.append('Yours'))        #This line adds Yours to the list.
print (MINE.pop(2))                 #This line will delete the second item


PYTHON_TUTORIAL = "I want to learn this python, God Please help me"
print(PYTHON_TUTORIAL[0])  #This helps us to get the index of a character starting from the begining
print(PYTHON_TUTORIAL[-1])      #This helps us to get the index of a character starting from the end
print(PYTHON_TUTORIAL[0:3])                           #This helps us to get the index of a character starting from index 0 to index 2 omitting index 3
print(PYTHON_TUTORIAL[0:])                            #This helps us to get the index of a character starting from the begining to the end
print(PYTHON_TUTORIAL[1:])                            #This helps us to get the index of a character starting from the second later to the end
print(PYTHON_TUTORIAL[:7])                            #This helps us to get the index of a character starting from index 0 to index 6 omitting index 7

#Formatted Strings
#Formatted strings are useful where we want to dynamically generate some text from our variable.

FIRST_NAME ='John'
LAST_NAME ='Okechi'
MASSAGE = FIRST_NAME + ' ['+ LAST_NAME +'] is Dead' #Concatination worked but it will be difficult if we have more lines of code
print(MASSAGE)
#Now let's use formatted string. Note that the syntax is "f'{}'" {} is called place holder
MSG = f'{FIRST_NAME} [{LAST_NAME}] is Dead'
print(MSG)

#Using 3 quotation marks
INTRODUCTION ='''
My name is Mr. D
I am a native of banyi
i wish to learn Python to change my status of life
Please God give me the grace to make it a habbit
'''
print(INTRODUCTION)                #We use 3 quotation when we have multiple lines data.

#STRING METHODS
#To print the number of character in a string
COURSE = "    learning a new programming language call python   "
print(len(COURSE))
POWER = len(str(2**1000000))       #To set the lenght of returned value
print(POWER)
print(COURSE.lower())              #To set the characters to lower case
print(COURSE.upper())              #TO SET THE CHARACTERS TO UPPER CASE
print(COURSE.find('call'))         #This helps us to find the word call gives the INDEX of the first letter in 'call'
print(COURSE[36:-7])
print(COURSE.replace('call', 'named'))   #Finds 'call' in the string assigned to course and replace it with 'named'
print(COURSE.isalpha())       #Content test: isalpha returns boolian value "TRUE" if true else false
print(COURSE.isnumeric())                       #Content test: isnumeric
print(COURSE.isdigit())
print(COURSE.title())               #This makes all the first letter capital
print(COURSE.strip())               #This helps to clear all the spaces
print(COURSE.rstrip())               #This helps to clear spaces on the right
print(COURSE.lstrip())               #This helps to clear spaces on the left

#SORTING
HELLO = ['Bb', 'Aa', 'Cc', 'Dd']
print (HELLO.sort())
print (HELLO.reverse())

#NESTINIG/LIST COMPREHENSION
MATRIX = [[1, 2, 3],                    #3 x 3 matrix, as Nested list
          [5, 7, 9],                    #Code can span line if bracketed
          [6, 8, 4]]
print(MATRIX)
print(MATRIX[1])                                         #Get Row 2
print(MATRIX[1][2])                                      #Get Row 2 and Item 3

#LIST COMPREHENSION
COL2 = [row[1] for row in MATRIX]                       #Get the items in second column
MATRI = [row[1] + 1 for row in MATRIX]                  #Adds 1 to all the items in second column
MATR = [row[1] for row in MATRIX if row[1] % 2 == 0]    #This line filter out odd item
DIAG =  [MATRIX[i][i] for i in [0, 1, 2]]               #Collect a diagonal from matrix
DOUBLE = [b * 3 for b in 'spam']                        #Multiply the string item
GENERATOR = (sum(row) for row in MATRIX)               #This creates a generator of row sum
print(COL2)
print(MATRI)
print(MATR)
print(DIAG)
print(DOUBLE)
print(next(GENERATOR))
print(next(GENERATOR))
print(next(GENERATOR))

MAP = list(map(sum, MATRIX))                    #MAP SUM OVER ITEMS IN MATRIX
SUM = {sum(row) for row in MATRIX}              #CREATE A SET OF SUMS
SUMM ={i : sum(MATRIX[i]) for i in range(3)}    #CREATES KEY/VALUE TABLE OF ROWS SUMS
RANGE = list(range(4))
RANG = list(range(-6, 9, 2))
AN = [[c ** 2, c ** 3] for c in range(4)]                   #Multiple values "if" filters
RAN = [[x, x/2, x*3,] for x in range(-6, 9, 2) if x > 0]
VAN = [ord(x) for x in 'spam']                              #LIST OF CHARACTER ORDINALS
BUS = {ord(x) for x in 'spam'}                              #SETS REMOVES DUPLICATES
CAR = {x: ord(x) for x in 'spam'}                           #DICTIONARY KEYS ARE UNIQUE
print(MAP)
print(SUM)
print(SUMM)
print(RANGE)
print(RANG)
print(AN)
print(RAN)
print(VAN)
print(BUS)
print(CAR)

LINE = '     mymymy,yesyes,nono,youyouyou,ususus   '
print(LINE.split(','))        #Split the values asigned to Line
print(LINE.strip().split(','))

#DICTIONARY
#MAPPING OPERATIONS
MENU = {'meal': 'food', 'quantity': 3, 'color': 'orange'}
print(MENU['meal'])                 #Fetch value of key 'meal'
MENU['quantity' ] += 1               #Add 1 to 'quantity' value
print(MENU['color'])
print(MENU)

DATA = {}
DATA['name'] = 'Bob'
DATA['job'] = 'dev'
DATA['age'] = 34
print(DATA)
print(DATA['job'])

TIME = dict(Name='Paul', Job='Dev', Age=45)                     #KEYWORDS
TIME2 = dict(zip(['Name', 'Job', 'Age'], ['Bob', 'Dev', 49 ])) #Zipping
print(TIME)
print(TIME2)
print(list(TIME2.keys()))           #Unordered keys list
#print(TIME.sort())
for key in TIME2:                   #Iterate though sorted keys
    print(key, "=>", TIME2[key])

#NESTING REVISITED
REC = {'Name': {'First': 'Michael', 'Last': 'Smath'},
        'Jobs': ['Dev', 'Mgr'],
        'Age': 34.4}
print(REC['Name'])                      #'name' is a nested dictionary
print(REC['Name']['Last'])              #Index the nested dictionary
print(REC['Jobs'])                      #'Jobs' is a nested list
print(REC['Jobs'][-1])                  #Index the nested list
REC['Jobs'].append('Janitor')           #Expand Bob's Job description in place
print(REC)

#SAMPLING
SAMPLE = {'A': 3, 'B': 9, 'D': 81}
print(SAMPLE)
SAMPLE['E'] = 6561                      #ASSIGNING NEW KEY GROWS DICTIONARY
print(SAMPLE)
if 'F' not in SAMPLE:
    print('missing')

#There are times you want to check the existence of a Character or
# a squence of characters in your string, in those situaltion you use 'in operator'
print("programming language" in COURSE) #This is called boolian statement.
                                  #It is used to check for the existecne of character in a stringr.
            # #Note that the different between 'in' and 'find' is that 'in' returns boolian value.
                                        # while 'find' returns the 'index' of the character
print("Flash Back" not in COURSE)
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
print(bool(X))

#ABSOLUTE FUNCTION (abs):
#THHIS RETURN THE POSITIVE REPRESENTATIVE OF VALUE EVEN IF IT IS A NEGETVE VALUE
X = -30
print(abs(X))

#MATH MODULE (for you to use Math Module, You need to import the module)
print(math.ceil(2.2)) #THIS PRINTS THE APPROXIMATE USING MATHS MODULE
M = input("M = ")
N = int(M) + 1
print(f"M: {M}, N: {N}")

Food = bytearray(b'Fish')
Food.extend(b'roll')
print(Food)
print(Food.decode())

FRUIT = "shrubbery"
L = list(FRUIT)             #Helps to list the string assigned to fruit letter by letter
L[1] = 'c'                  #Replaces h with c
#''.join(L)
print(L)
#print(''.join(L))

print(random.choice(['cassava', 'cocoyam', 'corn', 'potatoes', 'plantain', 'yam', 'igbagwu', 'okpa', 'beans', 'rice']))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

M = "Death"
N = "Or"
O = "Life"
print(M, N, O)

print("spam!"*8)         #prints spam! in multiple of 8

for x in 'spam!':
    print(x)

MAN = 4 > 9
print (MAN)

print(myfile.title)
print(title)
print(M, N, O)
print(M, N)
print(myfile)
#Axis = u'x' + b'y'
#print (Axis)
#To get the numerical representation of any character, do the following
B = "Z"
ZE = "z"
print(ord(ZE))
print(ord(B))

#COMPARIZINE OPERATORS (<, <=, >, >=, ==, !=)
IN =  "bag" < "Bag"
print(IN)

#IF STATEMNET
TEMPERATURE = 50
ALSO = {'A': 2, 'B': 4, 'C': 6,}
if TEMPERATURE < 40:
    print("I failed")
elif TEMPERATURE >= 51:
    print("ebuka abiakwa")
else:
    print("we passed")

AGE = 34
if AGE >= 30:
    print("Eligible")
else:
    print("Not Eligible")
            #OR
if AGE >= 30:
    MESSAGE = "Eligible"
else:
    MESSAGE = "Not Eligible"
    print(MESSAGE)
        #OR BEST
MESSAGE = "Eligible" if AGE >= 18 else "Not Eligible"
print(MESSAGE)

SOLUTION = ALSO.get('E', 'Mission')
print(SOLUTION)
SOLUTION = ALSO['A'] if 'A' in ALSO else 'Missing'
print(SOLUTION)
