from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

encryptedpass = "myverystrongpassword"

# Generate an RSA Keys
private_key = dsa.generate_private_key(
        key_size=2048,
        backend=default_backend()
    )

public_key = private_key.public_key()

# Save the RSA key in PEM format
with open("/tmp/dsakey.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(encryptedpass),
    )
    )

# Save the Public key in PEM format
with open("/tmp/dsapub.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
)