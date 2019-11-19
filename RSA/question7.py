import os
import sys
import logging
from rsa_key_helper import get_private_key

LOGGING_LEVEL = logging.INFO
#logging_level = logging.debug
if None != os.getenv('LOGGING_LEVEL'):
    LOGGING_LEVEL = logging.getLevelName(os.getenv('LOGGING_LEVEL'))
logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

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
