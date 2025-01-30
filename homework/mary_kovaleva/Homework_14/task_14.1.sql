INSERT INTO students (name, second_name) VALUES ('Hannibal', 'Lecter')

INSERT INTO books (title, taken_by_student_id) VALUES ('How to cook humans', 3943)

INSERT INTO books (title, taken_by_student_id) VALUES ('Neurological disorders', 3943)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Group A1', 'sep 2025', 'jun 2025')

UPDATE students SET group_id = 2495 WHERE id = 3943

INSERT INTO subjets (title) VALUES ('Psychiatry 101')

INSERT INTO subjets (title) VALUES ('Cooking 101')

INSERT INTO lessons (title, subject_id) VALUES ('Introduction into psychiatry', 3813)

INSERT INTO lessons (title, subject_id) VALUES ('How to hold a knife', 3814)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('magnifique', 7408, 3943)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('extraordinary', 7409, 3943)



SELECT * FROM marks WHERE student_id = 3943

SELECT * FROM books WHERE taken_by_student_id = 3943

SELECT students.name, students.second_name, b.title AS books, g.title AS group_name, s.title AS subjects, l.title AS lessons, m.value AS marks
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
WHERE students.name = 'Hannibal'