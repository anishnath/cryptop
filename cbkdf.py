import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.concatkdf import ConcatKDFHash
from cryptography.hazmat.backends import default_backend

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

backend = default_backend()
otherinfo = b"concatkdf-example"
ckdf = ConcatKDFHash(
    algorithm=hashes.SHA256(),
    length=32,
    otherinfo=otherinfo,
    backend=backend
)

# CKDF Derive key

key = ckdf.derive(b"input key")
base64.b64encode(key)

# CKDF Verify Key
ckdf = ConcatKDFHash(
    algorithm=hashes.SHA256(),
    length=32,
    otherinfo=otherinfo,
    backend=backend
)

ckdf.verify(b"input key", key)