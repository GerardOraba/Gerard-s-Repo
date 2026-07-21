import sqlite3
from student import Student

DB_FILE = "student.db"


def create_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            year_level TEXT NOT NULL,
            gender TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def save_student(student):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (student_id, name, course, year_level, gender, email)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', student.to_tuple())
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False  # Duplicate student_id


def search_student(student_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Student(*row)
    return None


def update_student(student):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students
        SET name = ?, course = ?, year_level = ?, gender = ?, email = ?
        WHERE student_id = ?
    ''', (student.name, student.course, student.year_level,
          student.gender, student.get_email(), student.student_id))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected > 0


def delete_student(student_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected > 0


def get_next_student_id():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT student_id FROM students ORDER BY student_id DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()
    if row:
        return str(int(row[0]) + 1)
    return "5000"  # Starting ID


def fetch_all_students():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students ORDER BY student_id')
    rows = cursor.fetchall()
    conn.close()
    return [Student(*row) for row in rows]