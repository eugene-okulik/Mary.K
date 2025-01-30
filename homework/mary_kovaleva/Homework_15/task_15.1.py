import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name) VALUES ('Will', 'Graham')")
student_id = cursor.lastrowid
cursor.execute("SELECT * FROM students WHERE name = 'Will' AND second_name = 'Graham'")
print(cursor.fetchone())

insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('How to tame a stray dog', student_id),
        ('How to solve murder cases', student_id)
    ]
)
cursor.execute(f'SELECT * FROM books WHERE taken_by_student_id = {student_id}')
print(cursor.fetchall())

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Group B', 'sep 2025', 'jun 2025')")
group_id = cursor.lastrowid
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")
cursor.execute(f"SELECT * FROM `groups` WHERE id = {group_id}")
print(cursor.fetchall())

cursor.execute("INSERT INTO subjets (title) VALUES ('Veterinary sciences')")
subj1_id = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) VALUES ('Forensics')")
subj2_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM subjets WHERE id IN ({subj1_id}, {subj2_id})")
print(cursor.fetchall())

cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Methology of veterinary science', {subj1_id})")
les1_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('How to investigate a murder scene', {subj2_id})")
les2_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM lessons WHERE id IN ({les1_id}, {les2_id})")
print(cursor.fetchall())

cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('A', {les1_id}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('A+', {les2_id}, {student_id})")
cursor.execute(f"SELECT * FROM marks WHERE student_id = {student_id}")
print(cursor.fetchall())

query = cursor.execute('''
SELECT students.name, students.second_name, b.title AS books, g.title AS group_name, 
s.title AS subjects, l.title AS lessons, m.value AS marks
FROM students
INNER JOIN books b
ON students.id=b.taken_by_student_id
INNER JOIN `groups` g
ON students.group_id = g.id
INNER JOIN marks m
ON students.id = m.student_id 
INNER JOIN lessons l
ON m.lesson_id = l.id
INNER JOIN subjets s
ON l.subject_id = s.id
WHERE students.name = 'Will' AND second_name = 'Graham'
''')
print(cursor.fetchall())

db.commit()
cursor.close()
db.close()
