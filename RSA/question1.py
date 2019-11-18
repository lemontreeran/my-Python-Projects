import os
import sys
import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def check_primality(number):
    """ Question 1
    This function will test primality of a number using trial and error method.
    Note: negative numbers, 0, and 1 are not considered prime by definition.
    The following number form Lucas primes can be used for testing:
    2, 3, 7, 11, 29, 47, 199, 521, 2207, 3571, 9349, 3010349, 54018521, 370248451, 6643838879, 119218851371, 5600748293801, 688846502588399, 32361122672259149
    """
    logger.info("Testing weather {} is primality or not!".format(number))

    for i in range(2, number - 1):
        if number % i == 0:
            logger.info("{} is not a primality! It can be divided by {}.".format(number, i))
            break
    else:
        # negative numbers, 0, and 1 are not considered prime by definition
        if number <= 1:
            logger.info("{} is a not primality!".format(number))
        else:
            logger.info("{} is a primality!".format(number))

def main():
    input_number = int(input("Question 1 - Please input any number to check primality:\n"))
    logger.info("Your input is: {}".format(input_number))
    check_primality(input_number)

if __name__ == "__main__":
    main()
