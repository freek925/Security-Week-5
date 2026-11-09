import os
import base64

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = Scrypt(salt=salt, length=32, n=2 ** 15, r=8, p=1)

    return kdf.derive(password.encode("utf-8"))


def encrypt_text(text: str, password: str) -> str:
    """
    Takes a string `text` and a string `password`, returns an encrypted version of the text.
    """
    salt = os.urandom(16)
    nonce = os.urandom(12)

    key = derive_key(password, salt)

    aes = AESGCM(key)
    ciphertext = aes.encrypt(nonce, text.encode(), None)

    result = salt + nonce + ciphertext

    return base64.urlsafe_b64encode(result).decode("ascii")


def decrypt_text(encrypted_text: str, password: str) -> str:
    """
    Takes a string `encrypted_test` and a string `password`, returns the decrypted text.
    """
    data = base64.b64decode(encrypted_text, altchars=b"-_", validate=True)

    if len(data) < 44:
        raise ValueError("Invalid encrypted data")

    salt = data[:16]
    nonce = data[16:28]
    ciphertext = data[28:]

    key = derive_key(password, salt)

    aes = AESGCM(key)
    plaintext = aes.decrypt(nonce, ciphertext, None)

    return plaintext.decode()