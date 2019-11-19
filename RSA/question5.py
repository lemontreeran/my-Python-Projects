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
    """ Question 5
    * According to Extended Euclid’s algorithm: a*x + b*y = hcf(a,b)
    * It is the same as : a*x ≡ hcf(a,b)(mod b).
    * For the linear congruence: ax= 1(mod b)
    * We only need to calculate the x in the Extended Euclid’s algorithm when hcf(a, b)=1
    """
    input_number1 = 342952340
    input_number2 = 4230493243
    logger.info("Your input is: {} , {}".format(input_number1, input_number2))
    ans = euclicid(input_number1, input_number2)
    logger.info("The HCF for {} and {} is : {}".format(input_number1, input_number2, ans[0]))
    logger.info("The linear congruence 342952340x=1 mod4230493243 is : {}".format(ans[1]))

def euclid(a, b):
    """ Euclid Algorithm, returns hcf, and x, y in d = hcf(a, b) = ax + by """
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
        [dn, xn, yn] = euclid(b, a % b)
        [d, x, y] = [dn, yn, xn - (a // b) * yn]
        return [d, x, y]

if __name__ == "__main__":
    main()
