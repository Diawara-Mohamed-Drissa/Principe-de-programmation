# README - Introduction à Docker

##  Qu'est-ce que Docker ?

Docker est une plateforme de **conteneurisation** qui permet d’exécuter des applications dans des environnements isolés appelés **conteneurs**.

Un conteneur contient :

- l’application
- ses dépendances
- ses bibliothèques
- sa configuration

Cela garantit que l’application fonctionnera de la même manière sur n’importe quelle machine.

---

#  Pourquoi utiliser Docker ?

##  Avantages principaux

###  Portabilité

Une application Docker fonctionne sur :

- Windows
- Linux
- macOS
- Serveurs Cloud

###  Isolation

Chaque conteneur possède :

- ses propres processus
- son système de fichiers
- son réseau
- ses ressources

###  Démarrage rapide

Un conteneur démarre beaucoup plus vite qu’une machine virtuelle.

###  Léger

Docker consomme moins de ressources qu’une VM.

###  Automatisation

Docker est idéal pour :

- CI/CD
- tests automatiques
- déploiement rapide

---

# Concepts essentiels

## Image Docker

Une **image** est un modèle prêt à l’emploi permettant de créer un conteneur.

Exemples :

- nginx
- mysql
- postgres
- alpine

## Conteneur Docker

Un **conteneur** est une instance lancée d’une image.

## Volume Docker

Permet de conserver les données même après suppression du conteneur.

## Réseau Docker

Permet la communication entre conteneurs.

---

# Commandes Docker essentielles

## Lancer un conteneur

```bash
docker run -it alpine:latest /bin/sh
```

### Explication :

- `run` : crée et lance un conteneur
- `-i` : mode interactif
- `-t` : terminal
- `alpine` : image Linux légère
- `/bin/sh` : shell Linux

---

## Voir les conteneurs

```bash
docker ps
```

Conteneurs actifs.

```bash
docker ps -a
```

Tous les conteneurs.

---

## Supprimer

```bash
docker rm nom_conteneur
docker rmi nom_image
```

---

# Exemple avec NGINX

```bash
docker run -d -p 8080:80 --name web nginx
```

### Explication :

- `-d` : arrière-plan
- `-p 8080:80` : port machine → port conteneur
- `--name web` : nom du conteneur

Puis ouvrir :

```text
http://localhost:8080
```

---

## Entrer dans un conteneur

```bash
docker exec -it web bash
```

---

# Volumes Docker

## Créer un volume

```bash
docker volume create monvolume
```

## Utiliser un volume

```bash
docker run -v monvolume:/data alpine
```

## Voir les volumes

```bash
docker volume ls
```

## Inspecter un volume

```bash
docker volume inspect monvolume
```

## Supprimer un volume

```bash
docker volume rm monvolume
```

---

# 🛢 Exemple MySQL avec persistance

```bash
docker run -d \
--name mysql \
-e MYSQL_ROOT_PASSWORD=pass \
-v mysql_data:/var/lib/mysql \
-p 3306:3306 \
mysql:8
```

### Ce que fait cette commande :

- lance MySQL
- crée un utilisateur root avec mot de passe
- stocke les données dans le volume `mysql_data`

---

# 🐘 Exemple PostgreSQL

```bash
docker run -d \
--name postgres \
-e POSTGRES_PASSWORD=pass \
-v pg_data:/var/lib/postgresql/data \
-p 5432:5432 \
postgres
```

---

#  Réseau Docker

## Types de réseaux

### bridge

Réseau par défaut Docker.

### host

Le conteneur partage le réseau de la machine hôte.

### none

Aucun réseau.

```bash
docker run --network none -it alpine sh
```

---

## Créer un réseau personnalisé

```bash
docker network create monreseau
```

## Connecter des conteneurs

```bash
docker run -d --name site --network monreseau nginx
docker run -d --name client --network monreseau alpine sleep 1000
```

Tester :

```bash
docker exec -it client sh
ping site
```

Les conteneurs communiquent via leur nom.

---

#  Dockerfile

Un **Dockerfile** permet de créer sa propre image Docker.

## Exemple :

```dockerfile
FROM node:20

WORKDIR /app

COPY . .

RUN npm install

CMD ["npm", "start"]
```

## Construire l’image

```bash
docker build -t monapp .
```

## Lancer l’image

```bash
docker run -p 3000:3000 monapp
```

---

#  Docker Compose

Permet de lancer plusieurs services facilement.

## Exemple :

```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"

  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: pass
```

## Lancer :

```bash
docker compose up -d
```

---

#  Bonnes pratiques

- utiliser des images légères (`alpine`, `slim`)
- nommer ses conteneurs
- utiliser des volumes pour les bases de données
- supprimer les ressources inutiles

```bash
docker system prune
```

---

#  Docker vs Machine Virtuelle

| Docker | Machine Virtuelle |
|--------|-------------------|
| Léger | Plus lourd |
| Rapide | Plus lent |
| Portable | Plus complexe |
| Partage le noyau OS | OS complet |

---

#  Commandes utiles récapitulatif

```bash
docker ps
docker ps -a
docker images
docker run image
docker exec -it conteneur bash
docker stop conteneur
docker rm conteneur
docker rmi image
docker volume ls
docker network ls
docker compose up -d
```

---

# Conclusion

Docker permet :

- d’uniformiser les environnements  
- de lancer rapidement des services  
- de simplifier les déploiements  
- de mieux travailler en équipe  
- de gérer facilement les bases de données  

Docker est aujourd’hui une compétence essentielle pour tout développeur et DevOps.
