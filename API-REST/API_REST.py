
from flask import Flask, jsonify, request
# créer l'application Flask
app = Flask(__name__)

#une liste d'etudiant
students = [
    {"id":1, "name": "Youcef", "age":21},
    {"id":2, "name": "Mohamed", "age":22},
    {"id":3, "name": "Melousta", "age":25},
    {"id":4, "name": "Issa", "age":23},

]
#Racine de l'API pour tester si le serveur fonctionne
@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des étudiants"
#Activer mode debug pour voir les erruers et recharger automatiquement le serveur
# Mettre à la fin 
#if __name__ == '__main__':
 #   app.run(debug=True)


##Endpoint pourlister tous les étudiants
@app.route('/students', methods=['GET'])
#Méthode HTTP Get qui permet de retouner la lister des étudiants
def get_etudiants():
    "jsonif transforme la liste students en json"
    return jsonify(students)

# Ajouter un étudiant (POST)
@app.route('/students', methods=['POST'])
def add_student():
    new_student=request.get_json()
#Pour récuperer les données envoyé par le client
    new_student['id']=len(students)+1
# Attribuer un numero de manière incrementable
    students.append(new_student)
    return jsonify(new_student), 201
#Le code 201 est pour confirmer que la creation s'est bien passée 



#Afficher un étudiant sachant son identifiant ....

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id']==id), None)
    if student:
        return jsonify(student)
    return jsonify({"erreur":"L'étudiant n'existe pas"}), 404

#   Mettre à jour un étudiant

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s['id']==id), None)
    if not student:
        return jsonify({"message":"Etudiant non trouvé"}), 404  


    data=request.get_json()
    student.update(data) #Mis a jour des données
    return jsonify(student)

# Suppriler un étudiant
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return jsonify({"message": "Etudiant supprimé"})


#Activer mode debug pour voir les erruers et recharger automatiquement le serveur 
if __name__ == '__main__':
    app.run(debug=True)

