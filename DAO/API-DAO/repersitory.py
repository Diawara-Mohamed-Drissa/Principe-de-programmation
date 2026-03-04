from db import get_connection


def get_all_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students


def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return student


def create_student(prenom, age):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (prenom, age) VALUES (%s, %s)",
        (prenom, age)
    )
    conn.commit()

    cursor.close()
    conn.close()


def update_student(student_id, prenom, age):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "UPDATE students SET prenom=%s, age=%s WHERE id=%s",
        (prenom, age, student_id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return None

    # récupérer l'étudiant mis à jour
    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
    student = cursor.fetchone()

    cursor.close()
    conn.close()
    return student


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()

    deleted = cursor.rowcount  # nombre de lignes supprimées

    cursor.close()
    conn.close()

    return deleted > 0