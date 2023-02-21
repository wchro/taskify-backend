import sqlite3

DB_FILE = "database/database.db"

def create_database():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password BLOB)")
    c.execute("CREATE TABLE IF NOT EXISTS invalid_tokens (token BLOB, date_added TEXT)")
    conn.commit()
    conn.close()

def check_if_exists(table, column, data):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(f"SELECT 1 FROM {table} WHERE {column}=?", (data,))
    result = c.fetchone()
    conn.close()
    return result is not None

def get_data(table, column, data):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table} WHERE {column}=?", (data,))
    result = c.fetchone()
    conn.close()
    return result

def insert(sql, values):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(sql, values)
    conn.commit()
    conn.close()

create_database()