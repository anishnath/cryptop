# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath


import uuid
from os import urandom

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.padding import (
    OAEP,
    MGF1,
)
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key
from cryptography.hazmat.primitives.hashes import SHA1


class RSAKeyWrapper:
    def __init__(self, kid):
        self.private_key = generate_private_key(public_exponent=65537,
                                                key_size=2048,
                                                backend=default_backend())
        self.public_key = self.private_key.public_key()
        self.kid = 'local:' + kid

    def wrap_key(self, key, algorithm='RSA'):
        if algorithm == 'RSA':
            return self.public_key.encrypt(key,
                                           OAEP(
                                               mgf=MGF1(algorithm=SHA1()),
                                               algorithm=SHA1(),
                                               label=None)
                                           )
        else:
            raise ValueError(_ERROR_UNKNOWN_KEY_WRAP_ALGORITHM)

    def unwrap_key(self, key, algorithm):
        if algorithm == 'RSA':
            return self.private_key.decrypt(key,
                                            OAEP(
                                                mgf=MGF1(algorithm=SHA1()),
                                                algorithm=SHA1(),
                                                label=None)
                                            )
        else:
            raise ValueError(_ERROR_UNKNOWN_KEY_WRAP_ALGORITHM)

    def get_key_wrap_algorithm(self):
        return 'RSA'

    def get_kid(self):
        return self.kid


#  Use a 128-bit KEK to wrap a 128-bit AES key.
# My wrapping Kek
kid = urandom(32)
key="This Key and it's Very Strong 8gwifi.org"

rsa = RSAKeyWrapper(kid)

assert rsa.wrap_key(key),  kid