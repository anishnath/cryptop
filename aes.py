from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

backend = default_backend()

# This AES key is 256 but long
mykey="mysecretkeyisverystrongofbitlong".encode("hex")
message="Hello 8gwifi.org"

#AES-256 ECB Mode Encyption

cipher = Cipher(algorithms.AES(mykey.decode('hex')), modes.ECB(), backend=backend)
e = cipher.encryptor()
ct = e.update(message) + e.finalize()

#AES-256 ECB Mode Decryption
#Using same Cipher Object
d = cipher.decryptor()

clear = d.update(ct) + d.finalize()

assert  clear,message


#AES-256 CBC Mode Encyption

iv = os.urandom(16)
cipher = Cipher(algorithms.AES(mykey.decode('hex')), modes.CBC(iv), backend=backend)
e = cipher.encryptor()
ct = e.update(message) + e.finalize()

#AES-256 CBC Mode Decryption
#Using same Cipher Object
d = cipher.decryptor()
clear = d.update(ct) + d.finalize()
assert  clear,message

#AES-256 CTR Mode Encyption

iv = os.urandom(16)
cipher = Cipher(algorithms.AES(mykey.decode('hex')), modes.CTR(iv), backend=backend)
e = cipher.encryptor()
ct = e.update(message) + e.finalize()

#AES-256 CTR Mode Decryption
#Using same Cipher Object
d = cipher.decryptor()
clear = d.update(ct) + d.finalize()
assert  clear,message


