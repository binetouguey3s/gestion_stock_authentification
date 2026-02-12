Stock Flash - Systeme de gestion de stock

- Application Python avec MySQL pour gérer l'inventaire d'une boutique.


1.  Configuration de la base de données

    Démarrer MySQL
    Exécuter le script SQL : mysql -u root -p 
    Creer le base de donnéés qui sera stockée dans stock_final.sql

2. Créer le fichier stock

python main.py

Fonctionnalités

    - Ajouter produit (id, designation, categorie, quantite, prix_unitaire)

    - Voir inventaire : Liste complète des produits

    - Modifier stock : Changer la quantité

    - Rechercher : Trouver un produit par nom

    - Supprimer : Enlever un produit 

    - Dashboard : Visualisation  du stock

    Quitter : Fermer l'application

 Configuration MySQL

L'application utilise :

    host : localhost

    Utilisateur : crud_user

    Mot de passe : Crud@1234!

    Base de données : stock_final 
 

3. Fonctionnalité ajoutée :


SYSTÈME D'AUTHENTIFICATION SÉCURISÉ:

Cette fonctionnalité permet de contrôler l'accès à l'application via une inscription et une connexion.

Table MySQL créée :

    inscription : stocke les utilisateurs avec id, prénom, nom, email (unique) et mot de passe haché

Sécurité :

    Mots de passe hachés 

    Requêtes préparées contre les injections SQL

    Email unique pour éviter les doublons

Fonctions :

    inscription_utilisateur() : crée un nouveau compte

    connexion_utilisateur() : vérifie email + mot de passe

    choix_inscription_connexion() : menu interactif

Parcours utilisateur :

    Lancement du script → choix inscription ou connexion

    Saisie des informations

    Vérification/création en base

    Accès au menu principal uniquement si authentifié

