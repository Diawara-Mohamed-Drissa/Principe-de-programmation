# PRINCIPE DE PROGRAMMATION  
## Étude Approfondie de l’Architecture MVC et de la Consommation d’une API REST en PHP

---

# Résumé

Ce projet s’inscrit dans le cadre du module *Principe de Programmation*.  
Il a pour objectif l’étude et la mise en œuvre d’une architecture logicielle structurée basée sur le modèle **MVC (Model – View – Controller)**, combinée à la consommation d’une **API REST** développée en Python (Flask).

À travers la réalisation d’un système CRUD de gestion d’étudiants, ce travail met en évidence les principes de séparation des responsabilités, d’interopérabilité entre systèmes, de modularité logicielle et d’organisation professionnelle du code.

---

# 1. Introduction

Le développement d’applications web modernes nécessite une structuration rigoureuse du code afin de garantir :

- Maintenabilité
- Lisibilité
- Évolutivité
- Réutilisabilité
- Travail collaboratif

Dans les premiers stades d’apprentissage, les applications sont souvent conçues de manière monolithique. Cette approche montre rapidement ses limites lorsque la complexité augmente.

Ce projet répond donc à la question suivante :

**Comment structurer une application web afin de séparer clairement les responsabilités et faciliter son évolution ?**

La réponse étudiée repose sur l’adoption du modèle architectural MVC.

---

# 2. Problématique et Justification

## 2.1 Approche non structurée

Exemple simplifié d’une application non organisée :

```php
$data = file_get_contents("http://127.0.0.1:5000/students");
$students = json_decode($data, true);

foreach ($students as $student) {
    echo $student['name'];
}
```

Problèmes identifiés :

- Mélange de logique métier et d’affichage
- Difficulté de modification
- Faible réutilisabilité
- Absence de modularité
- Complexité croissante

Une architecture formelle devient donc nécessaire.

---

# 3. Cadre Théorique

## 3.1 Architecture MVC

MVC signifie **Model – View – Controller**.

Il s’agit d’un modèle architectural qui divise une application en trois couches distinctes.

### 3.1.1 Model

Le Model encapsule :

- La logique métier
- Les données
- Les interactions avec les sources externes

Dans ce projet :

```
interop/services/StudentService.php
```

Exemple :

```php
public static function getAllStudents()
{
    return self::request('GET', '/students');
}
```

Le modèle est responsable de la communication avec l’API.

---

### 3.1.2 View

La View gère exclusivement l’affichage.

Exemple :

```php
<?php foreach ($students as $student): ?>
    <p><?= $student['name'] ?> (<?= $student['age'] ?> ans)</p>
<?php endforeach; ?>
```

Elle ne contient aucune logique métier.

---

### 3.1.3 Controller

Le Controller coordonne l’application.

```php
public static function index()
{
    $students = StudentService::getAllStudents();
    require __DIR__ . '/../views/students.php';
}
```

Il :

- Reçoit la requête
- Interroge le modèle
- Transmet les données à la vue

---

# 4. Diagramme Conceptuel MVC

![Architecture MVC](images/MVC.png)

Flux logique :

1. Requête utilisateur
2. Front Controller
3. Controller
4. Model
5. View
6. Réponse HTTP

---

---

## 4.1 Séparation des Responsabilités (Separation of Concerns)

La séparation des responsabilités est un principe fondamental selon lequel chaque composant d’un système doit avoir une fonction clairement définie et indépendante.

Dans une architecture non structurée :

- L’affichage
- La logique métier
- Les requêtes réseau

sont souvent mélangés.

Exemple non recommandé :

```php
$data = file_get_contents("http://127.0.0.1:5000/students");
$students = json_decode($data, true);

foreach ($students as $student) {
    echo "<p>" . $student['name'] . "</p>";
}
```

Dans cet exemple :

- L’accès aux données
- Le traitement
- L’affichage

sont réunis dans un seul bloc.

Avec MVC :

- Le Model récupère les données
- Le Controller coordonne
- La View affiche

Cette séparation rend l’application plus claire et plus maintenable.

---

## 4.2 Principe de Responsabilité Unique (SRP)

Le principe de responsabilité unique (Single Responsibility Principle), issu des principes SOLID, stipule qu’une classe ne doit avoir qu’une seule raison de changer.

Dans ce projet :

- `StudentService` gère uniquement l’accès à l’API.
- `StudentController` gère uniquement la logique de contrôle.
- Les fichiers de vue gèrent uniquement l’affichage.

Exemple :

```php
public static function getAllStudents()
{
    return self::request('GET', '/students');
}
```

Cette méthode ne fait qu’une seule chose : récupérer les étudiants.

Si l’API change, seul le service devra être modifié.

---

## 4.3 Cohésion et Couplage

Deux notions fondamentales en architecture logicielle :

### Cohésion

La cohésion mesure à quel point les éléments d’un module sont liés entre eux.

Un module fortement cohésif remplit une fonction bien précise.

Dans ce projet :

- Le service est fortement cohésif (il gère uniquement la communication API).

### Couplage

Le couplage mesure le niveau de dépendance entre modules.

Un faible couplage est souhaitable.

Dans MVC :

- La View ne connaît pas le fonctionnement interne du Model.
- Le Model ne connaît pas l’interface utilisateur.

Cette indépendance améliore la robustesse du système.

---

## 4.4 Abstraction

L’abstraction consiste à masquer la complexité interne d’un système.

Dans le projet :

```php
StudentService::getAllStudents();
```

Le contrôleur n’a pas besoin de savoir :

- Comment la requête HTTP est construite
- Comment le JSON est décodé

Ces détails sont abstraits dans le service.

---

## 4.5 Modularité

La modularité permet de diviser un système en composants indépendants.

Structure modulaire :

```
controllers/
services/
views/
config/
```

Chaque module peut être modifié indépendamment.

La modularité facilite :

- Les évolutions futures
- La maintenance
- Les tests
- Le travail collaboratif

---

## 4.6 Maintenabilité et Évolutivité

Une architecture bien conçue permet :

- D’ajouter de nouvelles fonctionnalités
- De modifier une partie du système sans impacter le reste
- D’améliorer progressivement l’application

Exemple :

Si l’API change d’URL, seule la configuration doit être modifiée :

```php
define('API_BASE_URL', 'http://nouvelle-api');
```

L’ensemble du système continue de fonctionner.

---

## 4.7 Testabilité

Une architecture modulaire facilite les tests unitaires.

Le service peut être testé indépendamment du contrôleur.  
La vue peut être vérifiée indépendamment de la logique métier.

Cela correspond aux bonnes pratiques modernes du développement logiciel.

---

## 4.8 Qualité Logicielle

Selon les critères classiques de qualité logicielle, une bonne architecture améliore :

- Lisibilité
- Maintenabilité
- Réutilisabilité
- Extensibilité
- Robustesse

L’adoption de MVC contribue directement à ces objectifs.

# 5. API REST

## 5.1 Définition

Une API (Application Programming Interface) permet à deux systèmes de communiquer.

REST (Representational State Transfer) repose sur :

- Le protocole HTTP
- Une architecture orientée ressources
- L’utilisation du format JSON

---

## 5.2 Méthodes HTTP

| Méthode | Rôle |
|----------|------|
| GET | Lecture |
| POST | Création |
| PUT | Mise à jour |
| DELETE | Suppression |

---

## 5.3 Format JSON

Exemple :

```json
{
  "id": 1,
  "name": "Ali",
  "age": 21
}
```

Conversion en PHP :

```php
$students = json_decode($response, true);
```

---

# 6. Méthodologie d’Implémentation

## 6.1 Front Controller

```php
$action = $_GET['action'] ?? 'list';

switch ($action) {
    case 'create':
        StudentController::create();
        break;
}
```

Centralisation des requêtes.

---

## 6.2 Communication HTTP

```php
$options = [
    'http' => [
        'method' => 'GET',
        'header' => "Content-Type: application/json\r\n"
    ]
];

$context = stream_context_create($options);
$response = file_get_contents($url, false, $context);
return json_decode($response, true);
```

Étapes :

1. Configuration
2. Envoi
3. Réception
4. Décodage

---

# 7. Cycle d’Exécution d’une Requête

Exemple : ajout d’un étudiant.

1. Soumission du formulaire.
2. Appel de :

```
index.php?action=create
```

3. Appel du contrôleur.
4. Transmission des données au service.
5. Envoi d’une requête POST.
6. Réception d’une réponse JSON.
7. Redirection vers la liste.
8. Affichage mis à jour.

---

# 8. Analyse Critique

## Avantages

- Séparation claire des responsabilités
- Architecture modulaire
- Code maintenable
- Facilité d’évolution
- Interopérabilité technologique

## Limites

- Complexité initiale plus élevée
- Nécessite rigueur organisationnelle

---

# 9. Comparaison Architecturale

| Approche Monolithique | Architecture MVC |
|-----------------------|------------------|
| Code mélangé | Code structuré |
| Maintenance difficile | Maintenance facilitée |
| Peu évolutif | Évolutif |
| Peu lisible | Lisible |

---

# 10. Perspectives d’Évolution

- Validation avancée
- Gestion d’exceptions
- Sécurisation des entrées
- Authentification
- Migration vers un framework (Laravel, Symfony)

---

# Conclusion Générale

Ce projet illustre l’application concrète des principes fondamentaux du développement structuré.

Il démontre que :

- L’architecture influence directement la qualité logicielle.
- La séparation des responsabilités est essentielle.
- REST permet l’interopérabilité entre technologies.
- MVC constitue une base solide pour des applications évolutives.

Ce travail constitue une étape fondamentale vers la maîtrise des architectures logicielles modernes et prépare efficacement à l’utilisation de frameworks professionnels.
