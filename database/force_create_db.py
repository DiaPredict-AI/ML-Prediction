import sqlite3
import os
import hashlib
import hmac
import secrets


def hash_password(password):
    """
    Hashes a password using PBKDF2-SHA256 via Python's built-in hashlib.
    Format: pbkdf2_sha256$iterations$salt$hash
    """
    iterations = 260000
    salt = secrets.token_hex(16)
    hash_value = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        iterations
    ).hex()
    return f"pbkdf2_sha256${iterations}${salt}${hash_value}"

# 1. Get the folder where THIS script is located
current_folder = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_folder, "users.db")

print(f"[INFO] Target Database Path: {db_path}")

# 2. Connect to the database at that specific path
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 3. Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
''')

# 4. Add Admin User
username = "admin"
password = "pass"
hashed_pw = hash_password(password)

try:
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_pw))
    print(f"[SUCCESS] User '{username}' added.")
except sqlite3.IntegrityError:
    print(f"[INFO] User '{username}' already exists.")

conn.commit()
conn.close()

print(f"[DONE] Database successfully created at: {db_path}")