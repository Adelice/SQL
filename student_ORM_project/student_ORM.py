import sqlite3

connection=sqlite3.connect("students.db")
cursor=connection.cursor()

class Student:
	def __init__(self,name,major,age,id=None):
		self.id=id
		self.name=name
		self.major=major
		self.age=age

	@classmethod
	def create(cls,cursor,connection):
		cursor.execute("""
				CREATE TABLE IF NOT EXISTS students(
				 id INTEGER PRIMARY KEY,
				 name TEXT,
				 major TEXT,
				 age INTEGER)
				 """)
	
		connection.commit()
		print("Table Created Sucessfully")

	def save(self,cursor, connection):
		cursor.execute('''
			   INSERT INTO students (name,age,major)
			   VALUES (?,?,?)
''', (self.name,self.major,self.age))
		
		connection.commit()
		print(f"Student {self.name} added successfully")
	
	@classmethod
	def show_all(cls,cursor):
		cursor.execute('SELECT * FROM students')
		for row in cursor.fetchall():
			print(row)



Student.create(cursor,connection)
alice= Student("Alice","Math",20)
bob=Student("Bob","Science",23)
alice.save(cursor,connection)
bob.save(cursor,connection)

Student.show_all(cursor)

		
