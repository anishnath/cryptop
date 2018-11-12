# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

from cryptography.fernet import Fernet, MultiFernet
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
key3 = Fernet(Fernet.generate_key())
plaintext="Hello 8gwifi.org"
f = MultiFernet([key1, key2, key3])
token = f.encrypt(plaintext)
d= f.decrypt(token)

assert  d,plaintext