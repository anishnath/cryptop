# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
kdf = PBKDF2HMAC(hashes.SHA1(), 20, b"salt", 10, default_backend())
key=kdf.derive(b"password")
base64.b64encode(key)
# 'rj/l9XB+B/PnwRf7iFzQUqb813o='


# Verify Operation

kdf = PBKDF2HMAC(hashes.SHA1(), 20, b"salt", 10, default_backend())
kdf.verify(b"password", key)

