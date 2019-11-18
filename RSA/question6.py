import os
import sys
import logging
# from common.rsa_key_helper import get_private_key
from rsa_key_helper import get_private_key
import rsa_key_helper

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def main():
    """ Question 6
    * Write a program to convert an encrypted number c = m^e (mod n) 
    * into the original m = c^d (mod n), where 0 < m < n is some integer. 
    """
    public_key = (937513, 638471)
    n, e = public_key
    private_key = get_private_key(n, e)

    input_plantext = input("Question 6 - Please input plaintext for encryption :\n")
    logger.info("Your input is: {}".format(input_plantext))
    ciphertext = encrypt(public_key, input_plantext)
    logger.info("The encrypted text is : {}".format(ciphertext))
    plantext = decrypt(private_key, ciphertext)
    logger.info("The decrypted text is : {}".format(plantext))

def encrypt(public_key, plaintext):
    #Unpack the key into it's components
    n, e = public_key
    #Convert each letter in the plaintext to numbers based on the character using m^e mod n
    cipher = [(ord(char) ** e) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(private_key, ciphertext):
    #Unpack the key into its components
    n, d = private_key
    #Generate the plaintext based on the ciphertext and key using c^d mod n
    plain = [chr((char ** d) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

if __name__ == "__main__":
    main()
