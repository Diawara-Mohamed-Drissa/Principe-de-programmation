# API-DAO – Exemple pédagogique d’API REST avec DAO (Flask + MySQL)

## Objectif pédagogique

Ce projet a été réalisé dans un cadre **pédagogique** pour illustrer plusieurs concepts fondamentaux du développement backend :

* création d’une **API REST**
* utilisation du **pattern DAO (Data Access Object)**
* séparation des responsabilités dans une application
* connexion à une **base de données MySQL**
* implémentation des opérations **CRUD**

Ce projet est volontairement simple afin de permettre aux étudiants de comprendre **les bases de l’architecture backend**.

---

# Architecture du projet

Structure simplifiée :

```
API-DAO/
│
├── app.py
├── db.py
├── repersitory.py
└── templates/
    └── students.html
```

| Fichier          | Rôle                               |
| ---------------- | ---------------------------------- |
| `app.py`         | API REST avec Flask                |
| `repersitory.py` | DAO contenant les requêtes SQL     |
| `db.py`          | gestion de la connexion MySQL      |
| `students.html`  | interface simple pour tester l’API |

---

# Principe général de fonctionnement

Architecture en couches :

```
Client (navigateur / interface)
        ↓
API REST (Flask)
        ↓
DAO / Repository
        ↓
Base de données MySQL
```

Chaque couche possède une responsabilité précise :

* **API** : reçoit les requêtes HTTP
* **DAO** : accède aux données
* **Base de données** : stocke les informations

Cette séparation rend le code **plus lisible et maintenable**.

---

# Qu’est-ce que le DAO ?

DAO signifie **Data Access Object**.

Le DAO est un **design pattern** dont le rôle est de **gérer l'accès aux données**.

Au lieu d’écrire les requêtes SQL dans toute l’application, on centralise ces accès dans une couche dédiée.

Cela permet :

* de séparer la logique applicative du SQL
* de rendre le code plus organisé
* de faciliter les modifications futures
* de changer la base de données plus facilement

---

## Mauvaise pratique

Mettre le SQL directement dans l’API :

```python
@app.route('/students')
def get_students():
    cursor.execute("SELECT * FROM students")
```

Ici l’API gère à la fois :

* la logique HTTP
* l’accès aux données

Ce n’est pas une bonne séparation.

---

## Bonne pratique avec DAO

L’API appelle simplement une méthode du repository :

```python
@app.route('/students')
def get_students():
    students = repersitory.get_all_students()
    return jsonify(students)
```

Le SQL est isolé dans le DAO.

---

# DAO / Repository

Le fichier `repersitory.py` contient toutes les opérations CRUD.

Exemple :

```python
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students
```

Cette fonction :

1. ouvre une connexion à la base
2. exécute une requête SQL
3. récupère les résultats
4. ferme la connexion
5. retourne les données à l’API

---

# Connexion à la base de données

La connexion MySQL est centralisée dans `db.py`.

Exemple :

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
    )
```

Toutes les fonctions du DAO utilisent cette connexion.

---

# Méthodes du repository

Le repository implémente les opérations CRUD.

## Lire tous les étudiants

```
GET /students
```

Méthode :

```
get_all_students()
```

---

## Lire un étudiant

```
GET /students/<id>
```

Méthode :

```
get_student_by_id(id)
```

---

## Ajouter un étudiant

```
POST /students
```

Méthode :

```
create_student(prenom, age)
```

---

## Modifier un étudiant

```
PUT /students/<id>
```

Méthode :

```
update_student(id, prenom, age)
```

---

## Supprimer un étudiant

```
DELETE /students/<id>
```

Méthode :

```
delete_student(id)
```

---

# Structure de la base de données

Table utilisée :

```
students
```

Création de la table :

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# Exemple de réponse JSON

Requête :

```
GET /students
```

Réponse :

```json
[
  {
    "id": 1,
    "prenom": "Alice",
    "age": 20
  },
  {
    "id": 2,
    "prenom": "Bob",
    "age": 22
  }
]
```

---

# Comment exécuter le projet

## 1. Installer Python

Installer Python depuis :

https://www.python.org/

Vérifier l'installation :

```
python --version
```

---

## 2. Installer les dépendances

Installer Flask et le connecteur MySQL :

```
pip install flask
pip install mysql-connector-python
```

---

## 3. Configurer la base de données

Créer la base de données dans MySQL :

```sql
CREATE DATABASE school;
```

Créer la table :

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 4. Configurer la connexion

Modifier si nécessaire le fichier :

```
db.py
```

Exemple :

```python
host="localhost"
user="root"
password=""
database="school"
```

---

## 5. Lancer l'application

Dans le dossier du projet :

```
python app.py
```

Le serveur démarre sur :

```
http://127.0.0.1:5001
```

---

## 6. Accéder à l’interface

Interface simple :

```
http://127.0.0.1:5001/ui
```

---

# Concepts pédagogiques illustrés

Ce projet permet de comprendre :

* API REST
* architecture backend
* DAO pattern
* CRUD
* JSON
* connexion MySQL
* interaction client / serveur

---

# Conclusion

Ce projet constitue une **base pédagogique pour comprendre la construction d’une API backend**.

Améliorations possibles :

* validation des données
* gestion d’erreurs avancée
* authentification
* ORM (SQLAlchemy)
* documentation API

---

Projet pédagogique – Principe de programmation

