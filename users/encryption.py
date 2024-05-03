from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64decode, b64encode

encryption_key = get_random_bytes(16)

def encrypt_user_id(id, key=encryption_key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(str(id).encode('utf-8'))
    return b64encode(cipher.nonce + tag + ciphertext)

def decrypt_user_id(encrypted_id, key=encryption_key):
    encrypted_id = b64decode(encrypted_id)
    nonce = encrypted_id[:16]
    tag = encrypted_id[16:32]
    ciphertext = encrypted_id[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    return int(cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8'))