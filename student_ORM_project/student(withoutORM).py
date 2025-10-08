import sqlite3

# create and connect the database 
connection=sqlite3.connect("students.db")
cursor=connection.cursor()

# clean the database
cursor.execute("DROP TABLE IF EXISTS students")

# create the table 
cursor.execute("""
CREATE TABLE students(
			   id INTEGER PRIMARY KEY,
			   name TEXT,
			   age INTEGER,
			   major TEXT
			   )
""")

# insert values

cursor.execute("""INSERT INTO students (name,age,major)
			   VALUES ("Alice",20,'Computer Science')""")

cursor.execute("""INSERT INTO students (name,age,major)
			   VALUES ("Bob",20,'Mathematics')""")

cursor.execute("""INSERT INTO students (name,age,major)
			   VALUES ("Alex",19,'Physics')""")

connection.commit()# save the values 
# reAD VALUES 

cursor.execute("SELECT * FROM students")
rows= cursor.fetchall()
for row in rows:
	print(row)

connection.commit()
connection.close()