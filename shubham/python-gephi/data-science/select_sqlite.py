import sqlite3

conn = sqlite3.connect('test.db')
data = conn.execute("select * from COMPANY")

for row in data:
	print('id=', row[0])
	print('name=', row[1])
	print('age=', row[2])