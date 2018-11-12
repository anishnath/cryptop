# The sample code is extracted from the book Python Cryptography
# The book can be downloaded from https://leanpub.com/cryptop
# Online Crypto Playgroud https://8gwifi.org
# Author Anish Nath


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
import datetime

#Generate Key (RSA,DSA,EC)

encryptedpass = "myverystrongpassword "
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
with open("/tmp/rsakey.pem", "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(encryptedpass),
    ))

# In Self Signed Certificate Issuer and Signer are Same

subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"CA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Python Cryptography"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"8gwifi.org"),
])

cert = x509.CertificateBuilder().subject_name(
    subject
    ).issuer_name(
    issuer
    ).public_key(
    key.public_key()
    ).serial_number(
    x509.random_serial_number()
    ).not_valid_before(
    datetime.datetime.utcnow()
    ).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=10)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
        critical=False,
).sign(key, hashes.SHA256(), default_backend())

with open("/tmp/certificate.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))