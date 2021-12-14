import sys
#Square root function
def squareroot(n, x = 1):
    xPrev = 0
    #If obtain same value as before stop, otherwise go on another iter
    while xPrev != x:
        xPrev = x
        x = (x+n/x)/2
        #Print single results (comment if not needed)
        print('Result: ' + str(x))
    return x
#Use first arg if possible, otherwise ask for number
try:
    number = int(sys.argv[1])
except IndexError:
    number = int(input('What number do you want the square root of? '))
#Print result
print('The square root of ' + str(number) + ' is ' + str(squareroot(n = number, x = number/2)))
input('Press ENTER to exit. ')