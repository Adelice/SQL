1. What is a Foreign Key?

 A foreign key is a column in one table that points to the primary key in another table.
It creates a relationship between two tables.

Students table: each student has a unique id (primary key).
Scores table: each score belongs to a student → it uses the student’s id as a foreign key.

SQLite supports foreign keys, but by default they are OFF.

You must run this command every time you open SQLite (it lasts for the current connection/session):

PRAGMA foreign_keys = ON;

PRAGMA is a special SQLite command that changes settings.

You can check if it’s on by running:
-PRAGMA foreign_keys;
-If it returns 1 → ON.
-If it returns 0 → OFF.

2. Why Use Foreign Keys?

To connect related data (students ↔ scores, customers ↔ orders).
To keep data consistent (no score without a valid student).
To avoid duplication (don’t repeat student details in every scores row).

3. Syntax (How to Declare a Foreign Key)
CREATE TABLE child_table (
    column_name DATA_TYPE,
    FOREIGN KEY (column_name) REFERENCES parent_table(parent_column)
);

4. Example: Students and Scores
Step 1 — Create the parent table (Students)
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
student_id is the primary key.
Each student is unique.

Step 2 — Create the child table (Scores)
CREATE TABLE scores (
    score_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT,
    score REAL,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
student_id here is a foreign key.
It must match a student_id in the students table.

Step 3 — Insert Data
-- Insert students
INSERT INTO students (name, age) VALUES ("Alice", 16);
INSERT INTO students (name, age) VALUES ("Bob", 15);

-- Insert scores
INSERT INTO scores (student_id, subject, score) VALUES (1, "Math", 88.5);
INSERT INTO scores (student_id, subject, score) VALUES (1, "English", 92.0);
INSERT INTO scores (student_id, subject, score) VALUES (2, "Math", 79.0);

Notice: student_id = 1 belongs to Alice, student_id = 2 belongs to Bob.
The scores table uses these IDs to “link” back to students.

Step 4 — What Happens If We Try Wrong Data?
INSERT INTO scores (student_id, subject, score) VALUES (3, "Science", 75.0);
 Error: No student with student_id = 3.
The foreign key stops invalid data.

