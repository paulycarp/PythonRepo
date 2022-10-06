'''CALLING EVEN NUMBERS THAT ARE BETWEEN 1 - 30'''
#from audioop import reverse


CALL = 0
for even_number in range(1, 30):
    if even_number % 2 == 0:
        CALL += 1
        print(even_number)
print(f"We have {CALL} even numbers")

NUMBERS = list(range(20))
print(NUMBERS)

#FIZZ_BUZZ ALGORITHM
#If you want to print FizzBuss do the following
def fiz_buzz(ouput):
    """Any dummy input."""
    if (ouput % 3 == 0) and (ouput % 5 == 0):
        return "FizzBuzz"
    if ouput % 3 == 0:
        return "Fizz"
    if ouput % 5 == 0:
        return "Buzz"
    return ouput

print(fiz_buzz(15))

def multi(*numbs):
    """Any dummy string."""
    total = 1
    for numb in numbs:
        total += numb
    return total#Note that the indentation for this line must be inline with for loop

COURSE = "    learning a new programming language call python   "
print(COURSE.upper())              #TO SET THE CHARACTERS TO UPPER CASE
print(COURSE.title())               #This makes all the first letter capital
print(len(COURSE))
HELLO = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee']
HELLO.reverse()
print(HELLO)
print(sorted(HELLO, reverse=True))

ASCORE = 0
BSCORE = 0

print(multi(10, 9, 8, 7))
