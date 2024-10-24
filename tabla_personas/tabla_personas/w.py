import sqlite3

conn = sqlite3.connect('persons.db')
cursor = conn.cursor()
cursor.execute('select * from persons')
gente = cursor.fetchall()
gente: list[list] = [[str(p[0]), p[1], str(p[2])] for p in gente]

print(gente)
