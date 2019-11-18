import os
import sys
import logging
import random
from random import randint
import math
from math import gcd
import fractions

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def factorisation(number):
    """ Question 3
     This method factorize numbers based on:
	 * Use Miller Rabin algorithm to check prime number
	 * Use Pollard Rho algorithm for factorisation
    """
    # f = lambda x: (x * x + 1) % number
    # '''defining a quadratic function f(x) = (x^2 + 1) mod n for Pollard''s Rho Algorithm'''

    origin_number = number
    p = []
    while not miller_rabin(number) :
        # factor = pollard_rho(number, f)
        factor = pollard_rho(number)
        # print(factor),
        p.append(factor)
        number //= factor
    # print(number)
    p.append(number)
    p.sort()
    logger.info("The factorisaction for {} is : {}".format(origin_number, p))

# '''defining a quadratic function f(x) = (x^2 + c) mod n for Pollard''s Rho Algorithm'''
def f(x, c, n):
	return (x * x + c) % n

def miller_rabin(n) :
    """This method implements the Miller Rabin algorithm.  Returns False if n is
    definitely a composite.  Returns True if n might be a prime number.
    Fermat's Little Theorem: a^(n-1) ≡ 1(mod n)
    Quadratic Probing: if n is prime, and 0<x<n, for x^2%n=1: then x=1 or x=n-1
    Keyword arguments:
    n - the number to test for primality.
    """

    k = 0
    x = n-1
    runner = False
    a = random.randint(1, n-1)

    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    # continuously extract the factor 2 in the index n-1
    while(runner == False):
        x = x >> 1
        k = k+1
        if(x & 1):
            runner = True
    d = (n-1) >> k

    # check a^q mod n=1
    value = pow(a, d, n)
    if value == 1:
        return True

    # check a^(d*2^i) mod n=n-1 ( 0<=i<r )
    for j in range(0, k):
        if pow(a,(pow(2, j)*d), n) == n-1:
            return True
    return False

def pollard_rho(n):
    # logger.debug("This number to be checked: {}".format(n))

    # Collard''s Rho Algorithm
    if n % 2 == 0:
        return 2

    # Randomizing values for x0 and c for the polynomial f(x) = x^2 + c.
    tortoise = randint(2, n - 1)
    hare = tortoise
    c = randint(1, n - 1)
    g = 1

    while g == 1:
        tortoise = f(tortoise, c, n)
        hare = f(f(hare, c, n), c, n)
        g = gcd(abs(hare - tortoise), n)

    # Failed to find a divisor. Trying again.
    if g == n:
        return pollard_rho(n)

    # Found a divisor.
    return g

def main():
    input_number = int(input("Question 3 - Please input any number for factorisation :\n"))
    logger.info("Your input is: {}".format(input_number))
    factorisation(input_number)

if __name__ == "__main__":
    main()
