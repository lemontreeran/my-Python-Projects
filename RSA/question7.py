import os
import sys
import logging
from rsa_key_helper import get_private_key

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def main():
    """ Question 7
    * Write a program to convert an encrypted number c = m^e (mod n)
    * into the original m = c^d (mod n), where 0 < m < n is some integer.
    """
    pk = (937513, 638471)
    key, n = pk
    private_key = get_private_key(key, n)
    logger.info("The private_key is : {}".format(private_key))

if __name__ == "__main__":
    main()
