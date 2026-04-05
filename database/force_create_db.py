import sqlite3
import os
from werkzeug.security import generate_password_hash

# 1. Get the folder where THIS script is located
current_folder = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_folder, "users.db")

print(f"📂 Target Database Path: {db_path}")

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
hashed_pw = generate_password_hash(password)

try:
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_pw))
    print(f"✅ SUCCESS: User '{username}' added.")
except sqlite3.IntegrityError:
    print(f"ℹ️  User '{username}' already exists.")

conn.commit()
conn.close()

print(f"🚀 Database successfully created at: {db_path}")