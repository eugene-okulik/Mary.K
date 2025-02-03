import csv
import dotenv
import os
import mysql.connector as mysql

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

base_path = os.path.dirname(__file__)
hw_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(hw_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")

cursor = db.cursor(dictionary=True)

query = '''
SELECT st.name, st.second_name, g.title AS group_title,
b.title AS book, subj.title AS subject,
l.title AS lesson, m.value AS mark
FROM students st
INNER JOIN books b
ON st.id=b.taken_by_student_id
INNER JOIN `groups` g
ON st.group_id = g.id
INNER JOIN marks m
ON st.id = m.student_id
INNER JOIN lessons l
ON m.lesson_id = l.id
INNER JOIN subjets subj
ON l.subject_id = subj.id
WHERE st.name = %s AND st.second_name = %s
AND g.title = %s AND b.title = %s
AND subj.title = %s AND l.title = %s AND m.value = %s
'''

with open(file_path, newline='') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        values = (row['name'], row['second_name'], row['group_title'],
                  row['book_title'], row['subject_title'],
                  row['lesson_title'], row['mark_value'])
        cursor.execute(query, values)
        if cursor.fetchone() is None:
            print(row)

db.close()
