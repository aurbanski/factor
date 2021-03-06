# HW 8
# Alex Urbanski and Mengchen Gong
# The code below is commented but a more in depth explanation is in the writeup

############################################################
#                   HOW TO RUN THE CODE                    #
############################################################
# In the terminal just run:                                #
# $ python pollard.py number                               #
# where number is replaced with the number you want to     #
# test. The code will pass that in as a command line       #
# argument and then display the factors and the time taken.#
############################################################


import sys
import math
import random
import time

# euclidean algorithm
def euclid (arg1, arg2):

    # Just put the bigger number as the number to be divided and the other
    # number as the divider
    if arg1 >= arg2:
        number = arg1
        divider = arg2
    else:
        number = arg2
        divider = arg1

    # Use a while loop so that each iterationn until the remainder is zero
    # runs with the number becoming the divisor and the divisor becoming the
    # remainder
    while divider != 0:
        new_number = divider
        divider = number % divider
        number = new_number

    return number

# Check to see what case the result of the euclidean algorithm matches
def checkValue (remainder, modder):
    # If remainder is 1, we can run through code again
    if remainder == 1:
        return 0
    # If remainder is modder, we have redeclare starting values
    elif remainder == modder:
        return 1
    # Else we found one of the prime factors
    else:
        return 2


def pollard (modder):

    # Declare the initial values. The first is a random value in
    # the range of 2 to the square root of modder. Second is Just
    # a copy of first. Adder is a random value. And remainder is just
    # initialized to 0
    first = random.randrange(2, int(math.sqrt(modder)))
    second = first
    adder = random.randrange(1, modder)
    remainder = 0

    # Set flag to the defaut value so that we can enter the loop
    flag = 0

    # A while loop to run as long as the first condition in checkValue
    # is met.
    while flag == 0:

        # Use the equation (x^2 + y) % n to randomize the values first and
        # second
        first = (first ** 2 + adder) % modder
        second = (((second ** 2 + adder) % modder) ** 2 + adder) % modder

        # Set the remainder equal to result of the call to euclid so that
        # it can be returned if it needs to be
        remainder = euclid(abs(first - second), modder)

        # Send the value of remainder to be checked by checkValue
        flag = checkValue(remainder, modder)

    # If the first condition in checkValue isn't met, break out of the
    # loop. If the value is 1, we need to call the function again because
    # there wasn't a solution for the starting values
    if flag == 1:
        pollard(modder)

    # The only other option is that we found a prime factor so return
    # that factor and the second prime factor
    returnArr = [remainder, int(modder / remainder)]
    return returnArr


print('=================================================')
print('For the number ' + sys.argv[1])
print('=================================================')
start = time.time()
print("The two factors are: ")
print(pollard(int(sys.argv[1])))
end = time.time()
print('Time taken in seconds: ')
print(str(end - start))
