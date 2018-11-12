from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

backend = default_backend()

iv = os.urandom(16)

# This AES key very short performing PKCS Padding
mykey="myshortkey"
message="Hello 8gwifi.org"

padder = padding.ANSIX923(128).padder()
padded_data = padder.update(mykey)

padded_data += padder.finalize()

#AES-128 CBC Mode Encyption
cipher = Cipher(algorithms.AES(padded_data), modes.CBC(iv), backend=backend)
e = cipher.encryptor()
ct = e.update(message) + e.finalize()


#AES-128 CBC Mode Decryption
# GCM tag used for authenticating the message.
cipher = Cipher(algorithms.AES(padded_data), modes.CBC(iv), backend=backend)
d = cipher.decryptor()

clear = d.update(ct) + d.finalize()

assert  clear,message

