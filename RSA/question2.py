import os
import sys
import logging
import random

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def check_primality(number):
    """ Question 2
     This method improves the efficiency of the check_primality function in two ways:
	 * only check potential factors up to the square root of the number
	 * only check potential factors that are themselves prime
	 * This method is based on the Miller Rabin algorithm.
    The following number form Lucas primes can be used for testing:
    2, 3, 7, 11, 29, 47, 199, 521, 2207, 3571, 9349, 3010349, 54018521, 370248451, 6643838879, 119218851371, 5600748293801, 688846502588399, 32361122672259149
    """

    logger.info("Testing weather {} is primality or not!".format(number))

    ## if a number is even its composite
    if number <= 1:
        logger.info("{} is a not primality!".format(number))
    elif number == 2:
        logger.info("{} is a primality!".format(number))
    elif number % 2 == 0:
        logger.info("{} is a not primality!".format(number))
    elif miller_rabin(number):
        logger.info("{} is a primality!".format(number))
    elif not miller_rabin(number):
        logger.info("{} is not a primality!".format(number))

def miller_rabin(n) :
    """This method implements the Miller Rabin algorithm.  Returns False if n is
    definitely a composite.  Returns True if n might be a prime number.
    Fermat's Little Theorem: a^(n-1) ≡ 1(mod n)
    Quadratic Probing: if n is prime, and 0<x<n, for x^2%n=1: then x=1 or x=n-1
    Keyword arguments:
    n - the number to test for primality.
    """

    r = 0
    x = n-1
    runner = False
    a = random.randint(1, n-1)

    # continuously extract the factor 2 in the index n-1 in the Fermat's Little Theorem,
    # so n-1 = d*2^r (d is an odd number)
    # According to Quadratic Probing:
    # a^(d * 2^(r-1)) = 1 or = n -1
    # if a^(d * 2^(r-1)) = 1, we can reiterate on a^(d * 2^(r-2)).
    # in the end:
    # either we get a^(d * 2^0), the Fermat's Little Theorem becomes a^d mod n=1
    # or there is a number j, a^(d*2^j) mod n=n-1 ( 0<=j<r ) 
    while(runner == False):
        x = x >> 1
        r = r+1
        if(x & 1):
            runner = True
    d = (n-1) >> r

    # check a^d mod n = 1
    value = pow(a, d, n)
    if value == 1:
        return True

    # check a^(d*^j) mod n = n-1 ( 0<=j<r )
    for j in range(0, k):
        if pow(a,(pow(2, j)*d), n) == n-1:
            return True
    return False

def main():
    input_number = int(input("Question 2 - Please input any number to check primality :\n"))
    logger.info("Your input is: {}".format(input_number))
    check_primality(input_number)

if __name__ == "__main__":
    main()
