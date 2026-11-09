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
    ciphertext = aes.encrypt(nonce, text.encode("utf-8"), None)

    result = salt + nonce + ciphertext

    return base64.urlsafe_b64encode(result).decode("ascii")