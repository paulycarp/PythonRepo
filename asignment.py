SCORE = 40
if SCORE <= 39:
    print("You failed")
if SCORE <= 49:
    print("poor")
            #OR
if SCORE <= 59:
    print("Passed")
if SCORE <= 69:
    print("Good")
if SCORE <= 79:
    print("Very Good")
if SCORE <= 89:
    print("Excellent")
if SCORE <= 69:
    print("God Like")
    #print(MESSAGE)
        #OR BEST
#MESSAGE = "Eligible" if AGE >= 18 else "Not Eligible"
#print(MESSAGE)
NUMBERS = list(range(20))
print(NUMBERS)

def multi(*numbs):
    total = 1
    for numb in numbs:
        total += numb
    return total#Note that the indentation for this line must be inline with for loop

ASCORE = 0 
BSCORE = 0

print(multi(10, 9, 8, 7))