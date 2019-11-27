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

def main():
    """ Question 4
    * We calculate the highest common factor (aka the greatest common divisor) of two numbers
    * by successively calculating one number modulo the other number until the result is zero.
    * Each input number must be an integer greater than 0;
    * This method is based on the Euclid’s algorithm.
    """
    input_number1 = int(input("Question 4 - Please input first number to get hcf :\n"))
    input_number2 = int(input("Question 4 - Please input second number to get hcf :\n"))
    logger.info("Your input is: {} , {}".format(input_number1, input_number2))
    ans = euclicid(input_number1, input_number2)
    logger.info("The HCF for {} and {} is : {}".format(input_number1, input_number2, ans[0]))

def euclicid(a, b):
    """ Euclicid Algorithm, returns hcf, and x, y in d = hcf(a, b) = ax + by """
    if b == 0:
        return [a, 1, 0]
    else:
        # if aX +bY = hcf(a,b)
        # and bXn + (a mob b)Yn = hcf(b,(a mod b))
        # according to Euclid's algorithm:
        # hcf(a,b)=hcf(b,(a mode b))
        # then aX + bY = bXn + (a mod b)Yn
        # because a mod b = a - (a/b)b
        # so aX + bY = aYn + bXn - (a/b)bYn
        # so X = Yn, and Y = Yn - (a/b)Yn
        [dn, xn, yn] = euclicid(b, a % b)
        [d, x, y] = [dn, yn, xn - (a // b) * yn]
        return [d, x, y]

if __name__ == "__main__":
    main()
