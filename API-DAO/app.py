from flask import Flask, jsonify, request
import repersitory

# Créer l'application
app = Flask(__name__)

# Définir les routes
@app.route('/')
def home():
    return "C'est cool REST !"

@app.route('/students', methods=['GET'])
def get_students():
    students = repersitory.get_all_students()
    return jsonify(students)

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = repository.get_student_by_id(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student)

# Lancer le serveur
# Force Flask à écouter sur toutes les interfaces (IPv4 + IPv6)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)