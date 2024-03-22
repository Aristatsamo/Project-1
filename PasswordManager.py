from cryptography.fernet import Fernet
import json
import os
import string
import random

class PasswordManager:
    def __init__(self, key_file):
        self.key_file = key_file
        self.load_or_generate_key()

    def load_or_generate_key(self):
        if not os.path.exists(self.key_file):
            self.key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(self.key)
        else:
            with open(self.key_file, 'rb') as key_file:
                self.key = key_file.read()

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def encrypt_password(self, password):
        cipher_suite = Fernet(self.key)
        return cipher_suite.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        cipher_suite = Fernet(self.key)
        return cipher_suite.decrypt(encrypted_password.encode()).decode()

    def save_passwords(self, passwords, filename):
        with open(filename, 'w') as f:
            json.dump(passwords, f)

    def load_passwords(self, filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

if __name__ == "__main__":
    key_file = 'key.key'
    password_manager = PasswordManager(key_file)

    # Example usage
    new_password = password_manager.generate_password()
    print("Generated Password:", new_password)

    encrypted_password = password_manager.encrypt_password(new_password)
    print("Encrypted Password:", encrypted_password)

    decrypted_password = password_manager.decrypt_password(encrypted_password)
    print("Decrypted Password:", decrypted_password)

    # Saving passwords to a file
    passwords = {'email': encrypted_password}
    password_manager.save_passwords(passwords, 'passwords.json')

    # Loading passwords from a file
    loaded_passwords = password_manager.load_passwords('passwords.json')
    print("Loaded Passwords:", loaded_passwords)
