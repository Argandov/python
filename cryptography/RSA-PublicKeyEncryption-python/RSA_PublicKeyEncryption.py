from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

# Using an existing RSA key:
with open("rsa_mykey.pem","rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(),password=None,backend=default_backend())
public_key = private_key.public_key()

message = b"Secret message"

#The hashing algorithm can be different, as long as the pairs used to auth are the same:
ciphertext = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA512()),algorithm=hashes.SHA256(),label=None))
print(ciphertext)
decrypted_message = private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA512()),algorithm=hashes.SHA256(),label=None)).decode()

print(decrypted_message)
