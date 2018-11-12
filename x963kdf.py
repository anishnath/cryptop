# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath


import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.x963kdf import X963KDF
from cryptography.hazmat.backends import default_backend

sharedinfo = b"ANSI X9.63 Example"
backend = default_backend()

kdf = X963KDF(
    algorithm=hashes.SHA256(),
    length=32,
    sharedinfo=sharedinfo,
    backend=backend
)

# ANSI X9.63  Kdf Function

key = kdf.derive(b"input key")
base64.b64encode(key)

# ANSI X9.63  verify Function

kdf = X963KDF(
    algorithm=hashes.SHA256(),
    length=32,
    sharedinfo=sharedinfo,
    backend=backend
)

kdf.verify(b"input key", key)