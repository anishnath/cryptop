from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

backend = default_backend()

iv = os.urandom(12)

# This AES key is 256 but long
mykey="mysecretkeyisverystrongofbitlong".encode("hex")
message="Hello 8gwifi.org"
aaed="Not Secret "


#AES-256 GCM Mode Encyption

cipher = Cipher(algorithms.AES(mykey.decode('hex')), modes.GCM(iv), backend=backend)
e = cipher.encryptor()
e.authenticate_additional_data(aaed)
ct = e.update(message) + e.finalize()

tag = e.tag

#AES-256 GCM Mode Decryption
# GCM tag used for authenticating the message.
cipher = Cipher(algorithms.AES(mykey.decode('hex')), modes.GCM(iv,tag), backend=backend)
d = cipher.decryptor()
d.authenticate_additional_data(aaed)
clear = d.update(ct) + d.finalize()

assert  clear,message


