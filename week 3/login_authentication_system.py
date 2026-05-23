import sqlite3
import hashlib
import os

DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            salt BLOB NOT NULL,
            password_hash BLOB NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(32)
    # Using PBKDF2 for stronger security
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt, key

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    
    salt, pwd_hash = hash_password(password)
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, salt, password_hash) VALUES (?, ?, ?)", 
                       (username, salt, pwd_hash))
        conn.commit()
        print("[+] Registration successful!")
    except sqlite3.IntegrityError:
        print("[-] Username already exists.")
    finally:
        conn.close()

def login():
    username = input("Username: ")
    password = input("Password: ")
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT salt, password_hash FROM users WHERE username=?", (username,))
    record = cursor.fetchone()
    conn.close()
    
    if record is None:
        print("[-] Login failed: User not found.")
        return
        
    stored_salt, stored_hash = record
    _, attempt_hash = hash_password(password, stored_salt)
    
    if attempt_hash == stored_hash:
        print("[+] Login successful! Welcome,", username)
    else:
        print("[-] Login failed: Incorrect password.")

if __name__ == "__main__":
    init_db()
    while True:
        print("\n--- Authentication System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")
