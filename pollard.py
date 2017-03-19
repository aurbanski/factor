import math
import random
import time

# My code for a euclidean algorithm
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

def checkValue (remainder, modder):
    if remainder == 1:
        return 0
    elif remainder == modder:
        return 1
    else:
        return 2


def pollard (modder):

    first = random.randrange(2, int(math.sqrt(modder)))
    second = first
    adder = random.randrange(1, modder)
    remainder = 1

    flag = 0

    while flag == 0:
        first = (first ** 2 + adder) % modder
        second = (((second ** 2 + adder) % modder) ** 2 + adder) % modder

        remainder = euclid(abs(first - second), modder)

        flag = checkValue(remainder, modder)

    if flag == 1:
        pollard(modder)

    returnArr = [remainder, long(modder / remainder)]
    return returnArr

start = time.time()
print(pollard(13845251856075533713))
end = time.time()
print(str(end - start))
