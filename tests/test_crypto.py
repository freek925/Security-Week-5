from crypto import decrypt_text, encrypt_text


def test_encrypt_decrypt_returns_correct_text():
    message = "Hello World"
    password = "Goodbye World"

    encrypted = encrypt_text(message, password)

    assert encrypted != message
    assert decrypt_text(encrypted, password) == message
