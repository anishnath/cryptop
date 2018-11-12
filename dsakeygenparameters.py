from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

encryptedpass = "myverystrongpassword"

parameters = dsa.generate_parameters(2048, default_backend())
skey = parameters.generate_private_key()
numbers = skey.private_numbers()
skey_parameters = numbers.public_numbers.parameter_numbers
pkey = skey.public_key()
parameters = pkey.parameters()
parameter_numbers = parameters.parameter_numbers()

print parameter_numbers.p
print parameter_numbers.q
print parameter_numbers.g

# Save the RSA key in PEM format
with open("/tmp/dsakey.pem", "wb") as f:
    f.write(skey.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(encryptedpass),
    )
    )

# Save the Public key in PEM format
with open("/tmp/dsapub.pem", "wb") as f:
    f.write(pkey.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
)