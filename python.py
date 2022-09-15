#My python class starts
from os import cpu_count
import sys              #Load a library Module
import random           #Imports Random Lib.
import math             #This imports Math Module
import decimal          #This improts Decimal:Fixed precision
from fractions import Fraction  #This imports: Numerator+Denominator
from myfile import M, N, O
from myfile import title
import myfile
print(sys.platform)
print(2**5)             #Raise 2 to power 5

X = "Spam! "
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
print(NAME[1:-1])   #The block parentaces helps us to get the index of a character,
                    #starting from the second letter through to second to the last.

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
MASSAGE = FIRST_NAME + ' ['+ LAST_NAME +'] is Dead'  #Concatination worked but it will be difficult,
print(MASSAGE)                                       #if we have more lines of code
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
print(COURSE.find('call'))         #This helps us to find the word call gives the
                                   #INDEX of the first letter in 'call'
print(COURSE[36:-7])
print(COURSE.replace('call', 'named'))          #Finds 'call' in the string assigned to course
                                                #and replace it with 'named'
print(COURSE.isalpha())       #Content test: isalpha returns boolian value "TRUE" if true else false
print(COURSE.isnumeric())                       #Content test: isnumeric
print(COURSE.isdigit())
print(COURSE.title())               #This makes all the first letter capital
print(COURSE.strip())               #This helps to clear all the spaces
print(COURSE.rstrip())               #This helps to clear spaces on the right
print(COURSE.lstrip())               #This helps to clear spaces on the left

#SORTING
HELLO = ['Bb', 'Aa', 'Cc', 'Dd']
HELLO.sort()
print(HELLO)
HELLO.reverse()
print(HELLO)

#IF STATEMNET
#SAMPLING
SAMPLE = {'A': 3, 'B': 9, 'D': 81}
print(SAMPLE)
SAMPLE['E'] = 6561                      #ASSIGNING NEW KEY GROWS DICTIONARY
print(SAMPLE)
if 'F' not in SAMPLE:
    print('missing')

TEMPERATURE = 50
if TEMPERATURE < 40:
    print("I failed")
elif TEMPERATURE >= 51:                 #NOTE: YOU CAN USE AS MANY AS "ELIF' YOU WANT
    print("ebuka abiakwa")
    print("it is warm")
    print("Drink water")
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

ALSO = {'A': 2, 'B': 4, 'C': 6,}
SOLUTION = ALSO.get('E', 'Mission')
print(SOLUTION)
SOLUTION = ALSO['A'] if 'A' in ALSO else 'Missing'
print(SOLUTION)

#LOGICAL OPERATOR
#WE HAVE 3 LOGICAL OPERATORS (AND, OR & NOT)
#ASSUMING YOU ARE BUILDING APP FOR LOAN PROCESSING
#WE NEED SOME VARIABLE
HIGH_INCOME = True
GOOD_CREDIT = True
if HIGH_INCOME and GOOD_CREDIT:           #IF ANY OF THE VARIABLE IS FALSE, WE WILL NOT GET ELIGIBLE
    print("You are Eligible") #In and operator once the two condition is ture the result is true
else:
    print("You are not Eligible")

HIGH_INCOME = False
GOOD_CREDIT = True
if HIGH_INCOME and GOOD_CREDIT:           #IF ANY OF THE VARIABLE IS FALSE, WE WILL NOT GET ELIGIBLE
    print("You are Eligible") #In and operator once the two condition is ture the result is true
else:
    print("You are not Eligible")

HIGHINCOME = True
GOODCREDIT = False
if HIGHINCOME or GOODCREDIT:           #IF ANY OF THE VARIABLE IS FALSE, WE WILL NOT GET ELIGIBLE
    print("You are Eligible") #In OR operator if any the two condition is ture the result is true
else:
    print("You are not Eligible")

HIGHCOME = True
GOODREDIT = True
STUDENT = True
if (HIGHCOME or GOODREDIT) and not STUDENT:
    print("You are Eligible")
else:
    print("You are not Eligible")

HIGHCOME = True
GOODREDIT = True
STUDENT = True
if (HIGHCOME and GOODREDIT) or not STUDENT:
    print("You are Eligible")
else:
    print("You are not Eligible")

#CHAINING COMPARISON OPERATORS
#ASSUMING WE WANT TO IMPLEMENT A ROW THAT SAYS AGE SHOULD BE BETWEEN 18 AND 65
AGE = 19
if AGE >= 18 and AGE <= 65:
    print("Dear you are Eligible")
if 18<= AGE <= 65:
    print("Age Comfirmation Successful")

#LOOP
#LOOPING IS USED TO CREATE REPETITION
for number in range(6):
    print("CODEMORE", number)           #Prints "CODEMORE" 6 times and number them 0-6
    print('CODEMORE', number + 1)       #ADDS ONE TO THE INDEX AND MAKE IT START FROM 1 INSTED OF 0
    print("CODEMORE", number + 1, (number + 1) * "*")
    print("CODEMORE", number + 1, (number) * "*")
for count in range(1, 20, 2):
    print("MORECODES", count, )
    print("MORECODES", count, count * '.',)
SUCESSFUL = True
for count in range(6):
    print('Attempt')
    if SUCESSFUL:
        print("You made it")
        break
else:
    print("failed after 6  attempt")
SUCESSFUL = False
for count in range(6):
    print('Attempt')
    if SUCESSFUL:
        print("You made it")
        break
else:
    print("failed after 6  attempt")

#NESTED LOOPS (i.e: one loop inside another loop)
for O in range(7):
    for P in range(5):
        print(f"({O}, {P})")


#NESTINIG/LIST COMPREHENSION
MATRIX = [[1, 2, 3],                    #3 x 3 matrix, as Nested list
          [5, 7, 9],                    #Code can span line if bracketed
          [6, 8, 4]]
print(MATRIX)
print(MATRIX[1])                        #Get Row 2
print(MATRIX[1][2])                     #Get Row 2 and Item 3

#FOR LOOP
print("spam!"*8)                        #prints spam! in multiple of 8

for x in 'spam!':
    print(x)
    print(x.upper())

TIME = dict(Name='Paul', Job='Dev', Age=45)                     #KEYWORDS
TIME2 = dict(zip(['Name', 'Job', 'Age'], ['Bob', 'Dev', 49 ])) #Zipping
print(TIME)
print(TIME2)
print(list(TIME2.keys()))                                     #Unordered keys list
#print(TIME2.sort())
for key in TIME2:                                             #Iterate though sorted keys
    print(key, "=>", TIME2[key])
for key in sorted(TIME2):                                     #sorts the items in alphabetical order
    print(key, '=>', TIME[key])

#LIST COMPREHENSION
COL2 = [row[1] for row in MATRIX]                       #Get the items in second column
MATRI = [row[1] + 1 for row in MATRIX]                  #Adds 1 to all the items in second column
MATR = [row[1] for row in MATRIX if row[1] % 2 == 0]    #This line filter out odd item
DIAG =  [MATRIX[i][i] for i in [0, 1, 2]]               #Collect a diagonal from matrix
DOUBLE = [b * 3 for b in 'spam']                        #Multiply the string item
GENERATOR = (sum(row) for row in MATRIX)                #This creates a generator of row sum
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
RANGE = list(range(4))                          #NUMBER OF REPETITION
RANG = list(range(-6, 9, 2))
AN = [[c ** 2, c ** 3] for c in range(4)]                   #Multiple values "if" filters
RAN = [[x, x/2, x*3,] for x in range(-6, 9, 2) if x > 0]
VAN = [ord(x) for x in 'spam']                              #LIST OF CHARACTER ORDINALS
BUS = {ord(x) for x in 'spam'}                              #SETS REMOVES DUPLICATES
CAR = {x: ord(x) for x in 'spam'}                           #DICTIONARY KEYS ARE UNIQUE
DECIMAL = decimal.Decimal('3.141')
decimal.getcontext().prec = 2
DECI = decimal.Decimal('1.00') / decimal.Decimal('3.00')

print(DECIMAL + 1)
print(DECI)
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

#SQUARE OF A LIST OF NUMBER USING FOR LOOP
SQUARE = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(SQUARE)
SQURE = []
for x in [1, 2, 3, 4, 5]:           #This is what a list comprehension does
    SQURE.append(x ** 2)            #Both run the iteration protocal internally
    print(SQURE)

#WHILE LOOP
WHILE = 4
while WHILE > 0:
    print('DevMan ' * WHILE)      #MULTIPLIES THE DEVMAN ITEM TO THE NUMBER OF VALUE STORED IN WHILE
    WHILE -= 1                    #PRINTS THE ITEM IN WHILE IN REDUCTION OF 1
    print(WHILE)

#TUPLES
TUPLE = (1, 2, 3, 4)
print(len(TUPLE))               #PRINT OUT THE LENGHT
print(TUPLE + (5, 5, 5, 6, 7))  #CONCATENATING ANOTHER ITEMS TO TUPLE
print(TUPLE[0])                 #PRINT OUT THE ITEM IN INDEX 0
print(TUPLE.count(5))           #COUNTS HOW MANY 5 APPERED
print(TUPLE.index(2))           #PRINT OUT THE ITEM IN INDEX 2
TUPLE = (2,) + TUPLE[1:]
print(TUPLE)
TUPL = 'PAN', 9.0, [11, 22, 33]
print(TUPL[1])
print(TUPL[2][1])

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

#FILES
F = open('data.txt', 'w')                   #Makes a new file in output mode('w' is write)
F.write('Hello ')                           #Writes strings of characters to it
F.write('World\n')
F.write('Nigeria is not a place to be \n\t')
F.write('For the first time in my life I chose a part of career\n')
F.close()                                   #Close to flush output buffers to disk
F = open('data.txt')                        #'r'(read) is the default processing mode
text = F.read()                             #Read entire file into a string
print(text)                                 #Print interprets control characters
print(text.split())
for line in open('data.txt'): print(line)

#OTHER CORE TYPES
X = set('codemore')
Y = {'k', 'i', 'd', 'd', 'i', 'e'}
CODEMORE = 'C' in set('CODEMORE'), 'C' in 'CODEMORE', 'MORE' in ['man', 'CODEMORE', 'MORE']
CHECK = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(X, Y)                             #Filtering out duplicates (possibly reordered)
print(X & Y)
print(X | Y)
print(X - Y)                            #Finding differences in collections
print(X > Y)
print(X < Y)
#print(X = Y)
print(X <= Y)
print(X >= Y)
print(X == Y)
print(set('CHECK') == set('KECH'))
print(set('CHECK') - set('ECH'))
print(CODEMORE)

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

print(random.choice(['cassava', 'cocoyam', 'corn', 'potatoes', 'plantain', 'yam',
                    'igbagwu', 'okpa', 'beans', 'rice']))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

M = "Death"
N = "Or"
O = "Life"
print(M, N, O)

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
