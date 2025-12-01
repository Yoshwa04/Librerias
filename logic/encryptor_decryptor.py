from cryptography.fernet import Fernet
import os

def create_key(path):   
    if not os.path.exists(path):
        with open(path, "wb") as key_file:
            key = Fernet.generate_key()
            key_file.write(key)
        
        
def __load_key(path):
    with open(path, "rb") as key_file:
        return key_file.read()
    
    
def encrypt_password(password, path):
    key = __load_key(path)
    fernet = Fernet(key)
    
    return fernet.encrypt(password.encode())


def decrypyt_password(encrypted_password, path):
    key = __load_key(path)
    fernet = Fernet(key)
    
    return fernet.decrypt(encrypted_password.decode())