import sqlite3

DB_FILE = "database/database.db"

def create_database():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password BLOB)")
    c.execute("CREATE TABLE IF NOT EXISTS invalid_tokens (token BLOB, date_added TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, date INTEGER, completed BOOLEAN CHECK (completed IN (0, 1)), user_id INTEGER)")
    conn.commit()
    conn.close()

def check_if_exists(table, column, data):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(f"SELECT 1 FROM {table} WHERE {column}=?", (data,))
    result = c.fetchone()
    conn.close()
    return result is not None

def get_data(table, column, data, all = False):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table} WHERE {column}=?", (data,))
    result = c.fetchall() if all else c.fetchone()
    conn.close()
    return result

def insert(sql, values):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(sql, values)
    conn.commit()
    conn.close()

def execute(sql):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()


create_database()
