from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import binascii
import base64

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

password="mysecretpassword"
val="hello 8gwifi.org"

def gen_key(password):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password)
    return base64.urlsafe_b64encode(digest.finalize())
if (len(password)>1):
	key = gen_key(password)
else:
	key = Fernet.generate_key()

print "Key: "+binascii.hexlify(bytearray(key))
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(val)
print "Cipher: "+binascii.hexlify(bytearray(cipher_text))
plain_text = cipher_suite.decrypt(cipher_text)
print "Plain text: "+plain_text