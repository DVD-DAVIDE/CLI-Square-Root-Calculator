import sys, math, random, time
def squareroot(n, x = 1):
    xPrev = 0
    #If obtain same value as before stop, otherwise go on another iter
    while xPrev != x:
        xPrev = x
        x = (x+n/x)/2
    return x
#Initiate random and variables
random.seed(time.time())
good = 0
bad = 0
#Use first arg if possible, otherwise use default (100)
try:
    total = int(sys.argv[1])
except IndexError:
    total = 100
#For [total] times, try computing two different square root functions
#If different, print the two numbers
for i in range(total):
    number = random.randrange(0, 2147483647)
    #By default, the first function is [math.sqrt()]. That can be changed
    a = math.sqrt(number)
    #The second function is the custom one, defined in this file
    b = squareroot(number)
    if a == b:
        print(str(number) + ': OK')
        good = good + 1
    else:
        print(str(number) + ': ERROR\nMath module solution:\t\t' + str(a) + '\nCustom function solution:\t' + str(b))
        bad = bad + 1
#Print count of both good (equal with both functions) and bad (different) answers
print('Good answers: ' + str(good) + '\nBad answers:  ' + str(bad) + '\nTotal: ' + str(good+bad))
input('Press ENTER to exit. ')