import sqlite3

conn = sqlite3.connect('persons.db')
cursor = conn.cursor()
cursor.execute('select * from persons')
gente = cursor.fetchall()


print(gente)
