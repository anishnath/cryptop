from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
import os

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

backend = default_backend()

nonce = os.urandom(12)
message="Hello 8gwifi.org"
aaed="Not Secret "

# This AES key is 256 but long
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

#AES-256 GCM Mode Encyption
ct = aesgcm.encrypt(nonce, message, aaed)

assert  message,aesgcm.decrypt(nonce, ct, aaed)