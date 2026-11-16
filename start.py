import sqlite3

db_path = 'C:\\Projects\\P_DEVELOPMENT\\11-16-26Python\\database.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
print(cursor.lastrowid)   # the id SQLite just assigned
conn.commit()
conn.close()
