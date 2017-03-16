# Import math, random, and time libraries
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


def pollard (number):

    # Get a random number between 2 and the square root of the number passed in
    first_guess = random.randrange(2, int(math.sqrt(number)))

    # Set a second value equal to that same number
    first_copy = first_guess

    # Get a number to add that is in the range of 1 to the number passed in
    random_adder = random.randrange(1, number)

    # Set d equal to 1 which is the condition for the while loop to run
    euclid_result = 1

    # If the result is 1, it means that the end value for the starting values
    # hasn't been found yet
    while euclid_result == 1:

        # Take one of the two values and square it and then add the random adding number
        # two times
        first_copy = (((first_copy ** 2 + random_adder) % number) ** 2 + random_adder) % number

        # For the other number, square it and add the random adding number
        first_guess = (first_guess ** 2 + random_adder) % number

        # Pass the difference of these two values into the euclidean algorithm
        # with the number itself
        euclid_result = euclid(abs(first_guess - first_copy), number)

        # If the result is equal to the original number, then call the function
        # again because the choice of starting numbers don't have a solution
        if euclid_result == number:
            return pollard(number)

    # When the program reaks out of the while loop, the euclid_result should
    # be one of the factors
    return euclid_result

start = time.time()
print(pollard(2605796209))
end = time.time()
print(str(end - start))
