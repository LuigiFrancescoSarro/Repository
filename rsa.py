from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding

# Genera le chiavi pubbliche e private per Bob
private_key_bob = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key_bob = private_key_bob.public_key()

# Serializza le chiavi pubbliche e private di Bob
private_pem_bob = private_key_bob.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem_bob = public_key_bob.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Salva le chiavi pubbliche e private di Bob su file
with open("private_bob.pem", "wb") as private_file:
    private_file.write(private_pem_bob)

with open("public_bob.pem", "wb") as public_file:
    public_file.write(public_pem_bob)

# Leggi la chiave pubblica di Bob generata da Lisa (presumibilmente dalla sua chiave pubblica salvata su un file)
with open("public_bob.pem", "rb") as public_file:
    public_key_bob_from_lisa = serialization.load_pem_public_key(public_file.read(), backend=default_backend())

# Messaggio da cifrare
message = b"Hello, Bob! This message is encrypted using your public key."

# Cifra il messaggio utilizzando la chiave pubblica di Bob generata da Lisa
ciphertext = public_key_bob_from_lisa.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Il ciphertext può essere inviato a Bob che lo decifrerà utilizzando la sua chiave privata
print("Messaggio cifrato:", ciphertext)
