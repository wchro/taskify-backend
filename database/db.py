import sqlite3

def create_database():
    conn = sqlite3.connect("database/database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password BLOB)")
    conn.commit()
    conn.close()

def signup(username: str, password: bytes):
    conn = sqlite3.connect("database/database.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

create_database()