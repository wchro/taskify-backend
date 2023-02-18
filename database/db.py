import sqlite3

DB_FILE = "database/database.db"

def create_database():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password BLOB)")
    conn.commit()
    conn.close()

def check_if_exists(table, column, data):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(f"SELECT 1 FROM {table} WHERE {column}=?", (data,))
    result = c.fetchone()
    conn.close()
    return result is not None

def signup(username: str, password: bytes):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

create_database()