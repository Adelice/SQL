Lesson: SQL Joins
1. What is a JOIN?
 A JOIN is used when we want to combine rows from two (or more) tables based on a related column.

Think of it like this:
We have a students table with student info.
We have a scores table with test results.
The student_id column connects them.

A JOIN is like saying:
“Show me the data from both tables where the student IDs match.”a students table with student info.

General Syntax of a JOIN

SELECT columns
FROM table1
JOIN_TYPE table2
ON table1.column = table2.column;

SELECT columns → choose which columns you want to display (can be from both tables).

FROM table1 → the first (left) table.

JOIN_TYPE table2 → the second (right) table and which type of join (INNER, LEFT, etc.).

ON table1.column = table2.column → the condition that connects the two tables (matching columns).

The ON clause is the “bridge” between tables — it tells SQL how to connect them.

Types of Joins
1) INNER JOIN → Only Matching Rows

Definition:
Shows rows where there’s a match in both tables.

SELECT students.name, scores.subject, scores.score
FROM students
INNER JOIN scores
  ON students.student_id = scores.student_id;

FROM students → start with the students table.

INNER JOIN scores → join with the scores table.

ON students.student_id = scores.student_id → only keep rows where the student ID matches in both tables.

SELECT students.name, scores.subject, scores.score → pick columns to display.

Result: Only students who have scores appear.


2) LEFT JOIN → Keep All From Left Table
Definition:
Shows all rows from the left table (students), even if there’s no match in the right table (scores).
SELECT students.name, scores.subject, scores.score
FROM students
LEFT JOIN scores
  ON students.student_id = scores.student_id;

LEFT JOIN → keeps all students (left table).

If a student has no scores, the subject/score will be NULL.

Result: Students without scores still appear, with blanks for score info.

4. RIGHT JOIN Syntax
SQLite doesn’t support RIGHT JOIN, but in general SQL the syntax is:

SELECT columns
FROM table1
RIGHT JOIN table2
  ON table1.column = table2.column;

This shows all rows from the right table, even if there’s no match in the left table.
In SQLite, you can simulate it by swapping the order of tables in a LEFT JOIN.

5. FULL OUTER JOIN Syntax

SQLite doesn’t support this directly either, but in general SQL:

SELECT columns
FROM table1
FULL JOIN table2
  ON table1.column = table2.column;

This shows all rows from both tables, with NULL where there’s no match.

6. Adding Conditions With WHERE

You can filter results after the join using WHERE.

Example: Show only math scores.

SELECT students.name, scores.subject, scores.score
FROM students
INNER JOIN scores
  ON students.student_id = scores.student_id
WHERE scores.subject = "Math";

7. Using Aliases (Shortcuts)

To make queries shorter, give tables nicknames using AS:

SELECT s.name, sc.subject, sc.score
FROM students AS s
INNER JOIN scores AS sc
  ON s.student_id = sc.student_id;

s = students, sc = scores.
Now you don’t need to type full table names every time.