#My python class starts
from myfile import M, N, O
from myfile import title
import myfile
import myfile
import sys              #Load a library Module
import random
print(sys.platform)
print(2**5)             #Raise 2 to power 5

X = "Spam!"
print(X*8)              #String repetition

Days = "Today is Thursday"
print(Days)

power = len(str(2**1000000))       #To the lenght of returned value

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

print("spam!"*8)

for x in 'spam!':
    print(x)

print(myfile.title)
print(title)
print(M, N, O)
print(M, N)
#print(myfile)