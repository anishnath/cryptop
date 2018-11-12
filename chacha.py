from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

backend = default_backend()

nonce = os.urandom(12)

# This AES key is 256 but long
message="Hello 8gwifi.org"
aaed="Not Secret "


key = ChaCha20Poly1305.generate_key()
chacha = ChaCha20Poly1305(key)

ct = chacha.encrypt(nonce, message, aaed)

assert message, chacha.decrypt(nonce, ct, aaed)

