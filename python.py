#My python class starts
from myfile import M, N, O
from myfile import title
import myfile
import myfile
import sys              #Load a library Module
import random           #Imports Random Lib.
print(sys.platform)
print(2**5)             #Raise 2 to power 5

X = "Spam!"
print(X*8)              #String repetition
print(X + 'NI!')
print(X.__add__('NI!'))

msg = """aaaaaaaabbb'''bbbbbbbb""bbbbbbbb'bbbccccccc"""
print(msg)
msg = '\naaaaaaa\nbbb\'\'\'bbbbbbb""bbbbbb\'bbbb\ncccccc\n'
print(msg)

Days = "Today is Thursday"
print(Days)

power = len(str(2**1000000))       #To set the lenght of returned value

Name = input("Enter your Name: ")

Food = bytearray(b'Fish')
Food.extend(b'roll')
print(Food)
print(Food.decode())

Age = input("Enter your Age: ")

newAge = int(Age) + float(25)

greating = input("Write a greating: ")

Fruit = "shrubbery"
L = list(Fruit)             #Helps to list the string assigned to fruit letter by letter
L[1] = 'c'                  #Replaces h with c
#''.join(L)

Line = 'mymymy,yesyes,nono,youyouyou,ususus'
print(Line.split(','))        #Split the values asigned to Line
print(Line.rstrip())
print(Line.rstrip().split(','))

Life = 'mistery'
print(Life.upper())          #Upper and Lowercase conversion
print(Life.isalpha())        #Content test: isalpha
print(Life.isnumeric())      #Content test: isnumeric
print(Life.isdigit())


print(greating)
print(newAge)
print(7)
print(power)
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

Code = 'Codemore'
print(Code.find('s'))                 #Searches for s in the string assigned to codemore if true it returns 1 else it returns -1
print(Code.replace('more', 'rforever'))   #Finds 'more' in the string assigned to code and replace it with 'rforever'
print(Code)

print(myfile.title)
print(title)
print(M, N, O)
print(M, N)
#print(myfile)