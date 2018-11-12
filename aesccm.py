from cryptography.hazmat.primitives.ciphers.aead import AESCCM
from cryptography.hazmat.backends import default_backend
import os

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

backend = default_backend()

nonce = os.urandom(13)
message="Hello 8gwifi.org"
aaed="Not Secret"

# This AES key is 128 but long
key = AESCCM.generate_key(256)
aesccm = AESCCM(key)


#AES-256 GCM Mode Encyption
ct = aesccm.encrypt(nonce, message, aaed)

print ct

assert  message,aesccm.decrypt(nonce, ct, aaed)