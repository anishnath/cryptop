from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives import hashes  
from cryptography.hazmat.primitives.asymmetric import dh  
from cryptography.hazmat.primitives.kdf.hkdf import HKDF  
from binascii import hexlify, unhexlify  
from cryptography.hazmat.primitives import serialization  
from cryptography.hazmat.primitives.serialization import load_pem_public_key  
import os  

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath
  
# DH generator must be 2 or 5  
# Minumun DH key size is 512  
parameters = dh.generate_parameters(generator=2, key_size=512,backend=default_backend())  
  
#You must generate a new private key using generate_private_key() for each exchange() when performing an DHE key exchange  
private_key = parameters.generate_private_key()  
  
#peer_public_key = parameters.generate_private_key().public_key()  
  
#Public Key Extracted  
peer_public_key = load_pem_public_key(open('/tmp/shpub.pem', 'rb').read(),default_backend())  
  
shared_key = private_key.exchange(peer_public_key)  
  
print "Shared Key " + hexlify(shared_key)  
  
# Perform key derivation.  
derived_key = HKDF(  
    algorithm=hashes.SHA256(),  
    length=32,  
    salt=os.urandom(13),  
    info=b'Some Data ',  
    backend=default_backend()  
).derive(shared_key)  
  
  
print "Derive Key " +  hexlify(derived_key)