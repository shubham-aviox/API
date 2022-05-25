import sqlite3

conn = sqlite3.connect('test.db')
print('open database successfully')

# conn.execute('''CREATE TABLE COMPANY
# (ID INT  PRIMARY KEY NOT NULL,
#  NAME          TEXT  NOT NULL,
#  AGE            INT   NOT NULL,
#  ADDRESS        CHAR(50),
#  SALARY         REAL);''')
# print('table has created')

# insert operation

# conn.execute('INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY) VALUES (1, "Shubham", 27, "Saharanpur", 11000.23);')
# conn.execute('INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY) VALUES (2, "Vishal", 27, "Himachal", 50000.23);')
# conn.execute('INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY) VALUES (3, "Rajat", 27, "Mohali", 20000.23);')
# conn.commit()
# print('inserted data')

conn.close()

# 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