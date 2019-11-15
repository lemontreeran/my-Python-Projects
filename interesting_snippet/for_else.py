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
    """This function will test primality of a number using trial and error method."""
    logger.info("Testing weather {} is primality or not!".format(number))
    for i in range(2, number - 1):
        if number % i == 0:
            logger.info("{} is not a primality! It can be divided by {}.".format(number, i))
            break
    else:
        logger.info("{} is a primality!".format(number))

def main():
    input_number = int(input("Please input any number :\n"))
    logger.info("Your input is: {}".format(input_number))
    check_primality(input_number)

if __name__ == "__main__":
    main()
