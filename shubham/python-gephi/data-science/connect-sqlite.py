import sqlite3

try:
	conn = sqlite3.connect('test1.db')
	print('Database created and Successfully Connected to SQLite')

	create_table = '''CREATE TABLE Studens(
					id INT PRIMARY KEY NOT NULL,
					name TEXT NOT NULL,
					roll_number INT NOT NULL,
					email TEXT NOT NULL UNIQUE,
					image BLOB NOT NULL);'''
	stu_id = int(input('enter the id: '))
	name = input('enter the name: ')
	email = input('enter the email: ')
	roll_number = input('enter the roll_number: ')
	image = input('enter the image: ')

	insert_data = '''INSERT INTO Studens(
					id,name,roll_number,email,image)
					VALUES (?,?,?,?,?);'''

	data = (stu_id,name,email,roll_number,image)
	cursor = conn.cursor()
	try:
		cursor.execute(create_table)
	except sqlite3.Error as error:
		print("table already exists", error)

	cursor.execute(insert_data, data)
	print('yes')

	conn.commit()
	cursor.close()

except sqlite3.Error as error:
	print("Error while connecting to sqlite", error)
finally:
	if conn:
		conn.close()
		print('connetion is closed')