from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import ec

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath

encryptedpass = "myverystrongpassword"
plaintextMessage = "Hello 8gwifi.org"


# EC DSA Generate Signature
privateKey = load_pem_private_key(open('/tmp/eckey.pem', 'rb').read(),encryptedpass,default_backend())

sig = privateKey.sign(
    plaintextMessage,
    ec.ECDSA(hashes.SHA256())
)

publicKey = load_pem_public_key(open('/tmp/ecpub.pem', 'rb').read(),default_backend())

# EC DSA Verify Signature
ciphertext = publicKey.verify(
    sig,
    plaintextMessage,
    ec.ECDSA(hashes.SHA256())
)