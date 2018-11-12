# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath


import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

salt = os.urandom(16)

kdf = Scrypt(
    salt=salt,
    length = 32,
    n = 2**14,
    r=8,
    p=1,
    backend=default_backend()
)

#scrytp Derive key
key = kdf.derive(b"my password")
print base64.b64encode(key)

# ANSI X9.63  verify Function

kdf = Scrypt(
    salt=salt,
    length = 32,
    n = 2**14,
    r=8,
    p=1,
    backend=default_backend()
)

kdf.verify(b"my password", key)