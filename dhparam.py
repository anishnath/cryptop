from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from binascii import hexlify, unhexlify
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import os

# DH generator must be 2 or 5
# Minumun DH key size is 512

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

p=175628339748224396140181355652569699881813470248510623740591206685224250268384255240141948567354436537469491258220480057343568322574414086924865612809502228925716250748136611976100895526530988783989918151666049795173173954826715147064072440336587386179441044551636048835596196013590766513435349750248369932891
g=107176209836536718962801284808131605075363838277339744565850617301534676770726222742912610436798059249618678970839324288089303827822543766150505159246951497945379339255850622488608863364657965634629341847037411606765436699180972115636657444687917156956960679037643921673927062603550324334473749946110139377151

pn = dh.DHParameterNumbers(p,g)
parameters = pn.parameters(default_backend())
#You must generate a new private key using generate_private_key() for each exchange() when performing an DHE key exchange
private_key = parameters.generate_private_key()

#peer_public_key = parameters.generate_private_key().public_key()

#Public Key Extracted
peer_public_key = load_pem_public_key(open('/tmp/shpub.pem', 'rb').read(),default_backend())

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


