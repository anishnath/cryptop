from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives.asymmetric import ec  
from cryptography.hazmat.primitives import serialization  
  

# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath
  
encryptedpass = "myverystrongpassword"  
  
# Generate an RSA Keys  
private_key = ec.generate_private_key(  
        ec.SECP256K1,  
        backend=default_backend()  
    )  
  
public_key = private_key.public_key()  
  
# Save the RSA key in PEM format  
with open("/tmp/eckey.pem", "wb") as f:  
    f.write(private_key.private_bytes(  
        encoding=serialization.Encoding.PEM,  
        format=serialization.PrivateFormat.TraditionalOpenSSL,  
        encryption_algorithm=serialization.BestAvailableEncryption(encryptedpass),  
    )  
    )  
  
# Save the Public key in PEM format  
with open("/tmp/ecpub.pem", "wb") as f:  
    f.write(public_key.public_bytes(  
        encoding=serialization.Encoding.PEM,  
        format=serialization.PublicFormat.SubjectPublicKeyInfo,  
    )  
)