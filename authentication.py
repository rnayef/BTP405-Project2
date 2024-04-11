
import sys
sys.path.insert(1, './database')

users_db = {}

def registerUser(user, pwd):
    """
    Registers user to the database
    """
    if user in users_db:
        print("User already exists!")
        return False
    else:
        users_db[user] = pwd
        print("User registered successfully!")
        return True

def authenticateUser(user, pwd):
    """
    Checks if user exists in the database and verifies password
    """
    if user in users_db and users_db[user] == pwd:
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed. Invalid username or password.")
        return False
