from pyprimesieve import *
import math

def factor (number):
    #Create an array for the return values
    return_vals = [0] * 2

    #Generate a list of prime numbers
    prime_list = primes(int(math.floor(math.sqrt(number))))
    possible_numbers = primes(number)

    if not prime_list:
        prime_list.append(2)

    #For any value in the sieve
    for value in prime_list:
        #Check to see that it divides the number passed in and also that the
        #Other number that it would be multiplied by divides the number
        if (number % value) == 0 and (number % (number / value)) == 0:
            #Check to make sure that the other number is also prime
            if ((number / value) in possible_numbers) == True:
                #If it is pass the array back
                return_vals[0] = value
                return_vals[1] = number / value

    return return_vals

answer = factor()
print(answer)
