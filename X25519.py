# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from binascii import hexlify, unhexlify
import os


# Generate a private key for use in the exchange.
private_key = X25519PrivateKey.generate()

peer_public_key = X25519PrivateKey.generate().public_key()
shared_key = private_key.exchange(peer_public_key)

print "Shared Key "  + hexlify(shared_key)

# Perform key derivation.
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=os.urandom(13),
    info=b'Some Data ',
    backend=default_backend()
).derive(shared_key)


print "Derive Key "  +  hexlify(derived_key)