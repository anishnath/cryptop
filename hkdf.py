import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

backend = default_backend()

salt = os.urandom(16)
info = b"hkdf-example"
hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    info=info,
    backend=backend
)

key = hkdf.derive(b"input key")
base64.b64encode(key)

# Recreate the HKDF Instace to Verify the 

hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    info=info,
    backend=backend
)

hkdf.verify(b"input key", key)