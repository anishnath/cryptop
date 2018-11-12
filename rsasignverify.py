# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key

encryptedpass = "myverystrongpassword"
plaintextMessage = "Hello 8gwifi.org"



alicePrivKey = load_pem_private_key(open('/tmp/alice.pem', 'rb').read(),encryptedpass,default_backend())

sig = alicePrivKey.sign(
    plaintextMessage,
    padding.PSS(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256()
)


alicePubKey = load_pem_public_key(open('/tmp/alicepub.pem', 'rb').read(),default_backend())

ciphertext = alicePubKey.verify(
    sig,
    plaintextMessage,
    padding.PSS(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256()
)