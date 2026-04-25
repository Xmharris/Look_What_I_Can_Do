import hashlib
import random
import string

def hash_pw(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_pw(length=8):
    chars = string.ascii_letters + string.digits + "!@#$*"
    return ''.join(random.choice(chars) for _ in range(length))

def create_password():
    print("1. Create your own password")
    print("2. Generate a password")
    choice = input("Choose: ")

    if choice == "1":
        return input("Enter your password: ")

    if choice == "2":
        try:
            length = int(input("Password length (default 8): "))
        except:
            length = 8
        pw = generate_pw(length)
        print("Generated password:", pw)
        return pw

    print("Invalid choice.")
    return create_password()

def password_system():
    print("\n--- Password System ---")
    stored = hash_pw(create_password())

    attempt = input("Enter your password: ")
    if hash_pw(attempt) == stored:
        print("Access Granted")
    else:
        print("Access Denied")
