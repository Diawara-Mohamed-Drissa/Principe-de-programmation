import os
from flask import Flask, jsonify, request, render_template
import repersitory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

@app.route('/routes')
def routes():
    return "<br>".join(sorted(str(r) for r in app.url_map.iter_rules()))

@app.route('/')
def home():
    return "C'est cool REST !"

@app.route('/ui')
def ui():
    return render_template("students.html")

# READ ALL
@app.route('/students', methods=['GET'])
def get_students():
    students = repersitory.get_all_students()
    return jsonify(students)

# READ ONE
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = repersitory.get_student_by_id(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student)

# CREATE
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json(silent=True) or {}
    prenom = data.get("prenom")
    age = data.get("age")

    if prenom is None or age is None:
        return jsonify({"error": "Missing fields: prenom, age"}), 400

    try:
        age = int(age)
        if age < 0:
            return jsonify({"error": "age must be >= 0"}), 400
    except (TypeError, ValueError):
        return jsonify({"error": "age must be an integer"}), 400

    repersitory.create_student(prenom, age)
    return jsonify({"message": "Student created"}), 201

# UPDATE
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json(silent=True) or {}
    prenom = data.get("prenom")
    age = data.get("age")

    if prenom is None or age is None:
        return jsonify({"error": "Missing fields: prenom, age"}), 400

    try:
        age = int(age)
        if age < 0:
            return jsonify({"error": "age must be >= 0"}), 400
    except (TypeError, ValueError):
        return jsonify({"error": "age must be an integer"}), 400

    updated = repersitory.update_student(student_id, prenom, age)
    if updated is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(updated)

# DELETE
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    ok = repersitory.delete_student(student_id)
    if not ok:
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"message": "Student deleted"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)