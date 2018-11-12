from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives.keywrap import *
from os import urandom

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

#  Use a 128-bit KEK to wrap a 128-bit AES key.
# My wrapping Kek
kek = urandom(32)

# The padding will take care of making the key_to_wrap of multiple of 8 bytes
keyData = "8gwifi.org"
wk = aes_key_wrap_with_padding(kek, keyData, default_backend())
assert aes_key_unwrap_with_padding(kek, wk, default_backend()), kek