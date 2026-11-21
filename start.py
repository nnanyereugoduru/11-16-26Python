import sqlite3

db_path = 'C:\\Projects\\P_DEVELOPMENT\\11-16-26Python\\database.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Brandon", "brandon@example.com"))
print(cursor.lastrowid)   # the id SQLite just assigned
conn.commit()
conn.close()
