import mysql.connector # Importation du module mysql.connector pour connecter à la BD MySQL
import hashlib # Importation du module hashlib pour le hashage des mots de passe

conn = None  # Variable globale pour la connexion à la base de données
cursor = None # Variable globale pour le curseur de la base de données
def get_connection(): # Fonction établir une connexion à la BD MySQL
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="crud_user",
            password="Crud@1234!",
            database="stock_final"
        )
        print("Connexion MySQL réussie")
        return conn
    except mysql.connector.Error as e:
        print("Erreur de connexion MySQL :", e)
        return None

conn = get_connection() 

#Gestion des utilisateurs
#inscription d'un nouvel utilisateur avec hashage du mot de passe
def inscription_utilisateur(nom_utilisateur, prenom_utilisateur, email, mot_de_passe):
    global conn
    global cursor
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO inscription (prenom_utilisateur, nom_utilisateur, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
            mot_de_passe_hash = hashlib.sha256(mot_de_passe.encode()).hexdigest() # Hashage du mot de passe
            cursor.execute(sql, (prenom_utilisateur, nom_utilisateur, email, mot_de_passe_hash)) 
            conn.commit()
            print("Inscription réussie!")
        except Exception as e:
            print('Erreur inscription utilisateur :', e)

#Verification du hash du mot de passe lors de la connexion
def connexion_utilisateur(email, mot_de_passe):
    global conn
    global cursor
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT mot_de_passe FROM inscription WHERE email = %s" # Recuperation du mot de passe hashé correspondant à l'email saisi 
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            if result:
                mot_de_passe_hash_db = result[0] # Récupération du mot de passe hashé depuis la base de données 
                mot_de_passe_hash_input = hashlib.sha256(mot_de_passe.encode()).hexdigest() # Hashage du mot de passe saisi pour comparaison
                if mot_de_passe_hash_input == mot_de_passe_hash_db: # Comparaison des hash des mots de passe
                    print("Connexion réussie!") 
                    menu() 
                else:
                    print("Mot de passe incorrect")
            else:
                print("Email non trouvé")
        except Exception as e:
            print('Erreur connexion utilisateur :', e)
            conn.rollback()
            return False

def choix_inscription_connexion():
    print("Bienvenue dans la gestion de stock")
    print("1. Inscription")
    print("2. Connexion")
    choix = input("Votre choix : ").strip()
    if choix == "1":
        nom_utilisateur = input("Nom : ").strip()
        prenom_utilisateur = input("Prénom : ").strip()
        email = input("Email : ").strip()
        mot_de_passe = input("Mot de passe : ").strip()
        inscription_utilisateur(nom_utilisateur, prenom_utilisateur, email, mot_de_passe)
        choix_inscription_connexion() # Retour au choix pour se connecter
    elif choix == "2":
        email = input("Email : ").strip()
        mot_de_passe = input("Mot de passe : ").strip()
        connexion_utilisateur(email, mot_de_passe) 
    else:
        print("Choix invalide. Veuillez réessayer.")
        choix_inscription_connexion() # Retour au  choix 

# gerer la recherche d'id si on met un id qui n'existe pas lors d une recherche ou d une suppression ou d une mise à jour du stock
def id_existe(id): #id est en entier
    global conn
    global cursor
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT COUNT(*) FROM produits WHERE id = %s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            conn.commit()
            # Retourne True si l'ID existe, sinon False
            if result and result[0] > 0: # Si le résultat existe et que le compte est supérieur à 0, l'ID existe
                return True
            else:                
                return False
        except Exception as e:
            print('Erreur vérification ID :', e)
            conn.rollback()
            return False



# Ajouter un produit à l'inventaire        
def ajouter_produit(id, designation, categorie, quantite, prix_unitaire):
    global  conn 
    global cursor
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO produits (id, designation, categorie, quantite, prix_unitaire) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (id, designation, categorie, quantite, prix_unitaire))
            conn.commit()
            print("Produit ajouté avec succès")
        except Exception as e:
            print('Erreur ajout produit :', e)
            conn.rollback()

def afficher_inventaire():
    global conn
    global cursor
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM produits ORDER BY id"
            cursor.execute(sql)
            produits = cursor.fetchall()
            conn.commit()

            #Affichage des produits
            for produit in produits:
                # Accès par position 
                id_prod = produit[0] 
                designation = produit[1]
                categorie = produit[2]
                
                # Gérer les valeurs None
                quantite = produit[3] if produit[3] is not None else 0 # Valeur par défaut pour la quantité
                prix = produit[4] if produit[4] is not None else 0.0 # Valeur par défaut pour le prix unitaire
                conn.commit()
                # Calcul 
                try:
                    total = float(quantite) * float(prix) # Calcul du total en gérant les erreurs de conversion
                except (TypeError, ValueError):
                    total = 0.0
                print(f"ID: {id_prod}, Désignation: {designation}, Catégorie: {categorie}, Quantité: {quantite}, Prix unitaire: {prix} FCFA, Total: {total} FCFA")
                conn.commit()
        except Exception as e:
            print('Erreur affichage inventaire :', e)
            conn.rollback()

def mettre_a_jour_stock(id, nouvelle_quantite):
    global conn
    global cursor
    if conn:
        if not id_existe(id):
            print(f"Erreur : Aucun produit trouvé avec l'ID {id}. Mise à jour annulée.")
            return
        try:
            cursor = conn.cursor()
            sql = "UPDATE produits SET quantite = %s WHERE id = %s"
            cursor.execute(sql, (nouvelle_quantite, id))
            conn.commit()
            print("Stock mis à jour avec succès")
            afficher_inventaire()
        except Exception as e:
            print('Erreur mise à jour stock :', e)
            conn.rollback()

def rechercher_produit(designation):
    global conn
    global cursor
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM produits WHERE designation LIKE %s"  
            cursor.execute(sql, ('%' + designation + '%',))
            produit = cursor.fetchone()
            conn.commit()

            mon_produit = produit[1] if produit and produit[1] is not None else "Produit non trouvé" # Gérer les valeurs nulles et les produits non trouvés
            print(f"Produit trouvé : {str(mon_produit).strip()}") # Affichage du produit trouvé en gérant les valeurs nulles et les espaces
            if produit:
                print(produit)
        except Exception as e:
            print('Erreur dans la recherche de produit :', e)
            conn.rollback()
 
def supprimer_produit(id):
    global conn
    global cursor
    afficher_inventaire()
    if conn:
        # Vérifier d'abord si l'ID existe
        if not id_existe(id):
            print(f"Erreur : Aucun produit trouvé avec l'ID {id}. Suppression annulée.")
            return
            
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM produits WHERE id = %s"
            cursor.execute(sql, (id,))
            conn.commit()
            print(f"Produit avec l'ID {id} supprimé avec succès")
            afficher_inventaire()
        except Exception as e:
            print("Erreur suppression produit :", e)
            conn.rollback()


def dashboard():
    while True:       
        print("\n Dashboard")
        print("1. Produit le plus cher")
        print("2. Valeur totale du stock")
        print("3. Quantité de produits par catégorie")
        print("4. Nombre de produits par catégorie")
        print("5. Retour au menu principal")

        choix = input("Votre choix : ").strip()
        if choix == "1":
            produit_plus_cher()
        elif choix == "2":
            valeur_totale_stock()
        elif choix == "3":      
            quantite_par_categorie()
        elif choix == "4":
            nombre_produits_par_categorie()
        elif choix == "5":
            break
        else:
            print("Choix invalide")
            continue


# Le produit le plus cher
def produit_plus_cher():    
    global conn
    global cursor
    if conn:
        try:
            cursor = conn.cursor()
            # Produit le plus cher
            sql = "SELECT designation FROM produits ORDER BY prix_unitaire DESC LIMIT 1"
            cursor.execute(sql)
            produit_cher = cursor.fetchone()
            cher_produit = produit_cher[0] if produit_cher[0] is not None else 0.0 # gerer les valeurs nulles
            print(f"Produit le plus cher : {str(cher_produit).strip()}") # Affichage du produit le plus cher en gérant les valeurs nulles et les espaces 
        except Exception as e:
            print("Erreur du produit plus cher")
            conn.rollback()
 
# La valeur du stock
def valeur_totale_stock():
    global conn
    global cursor
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT SUM(quantite * prix_unitaire) FROM produits"
            cursor.execute(sql)
            resultat = cursor.fetchone()
            valeur_totale = resultat[0] if resultat[0] is not None else 0.0 
            print(f"Valeur totale du stock : {float(valeur_totale):.2f} FCFA ") # Affichage de la valeur totale du stock avec formatage en float et gestion des valeurs nulles
        except Exception as e:
            print('Erreur valeur totale stock :', e)
            conn.rollback()


def quantite_par_categorie():
    global conn
    global cursor
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT categorie, SUM(quantite) FROM produits GROUP BY categorie"
            cursor.execute(sql)
            quantite_par_categorie = cursor.fetchall()
            print("Quantité de produits par catégorie :")
            for categorie in quantite_par_categorie:
                nom_categorie = categorie[0] if categorie[0] is not None else "Inconnu" 
                quantite = categorie[1] if categorie[1] is not None else 0 # Gérer les valeurs nulles pour la quantité
                print(f"Catégorie: {nom_categorie}, Quantité: {quantite}")
        except Exception as e:
            print('Erreur quantité par catégorie :', e)
            conn.rollback()

def nombre_produits_par_categorie():
    global conn
    global cursor
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT categorie, COUNT(*) FROM produits GROUP BY categorie"
            cursor.execute(sql)
            nombre_par_categorie = cursor.fetchall()
            print("Nombre de produits par catégorie :")
            for categorie in nombre_par_categorie:
                nom_categorie = categorie[0] if categorie[0] is not None else "Inconnu"  #Gérer les valeurs nulles 
                nombre = categorie[1] if categorie[1] is not None else 0 # Gérer les valeurs nulles pour le nombre
                print(f"Categorie: {nom_categorie}, Nombre de produits: {nombre} ")
        except Exception as e:
            print('Erreur nombre de produits par catégorie :', e)
            conn.rollback() 


#Le menu de navigation
def menu():
    while True:
        print("\n Bienvenu dans la gestion de Stock")
        print("1. Ajouter un produit")
        print("2. Afficher l'inventaire")
        print("3. Mettre à jour le stock")
        print("4. Rechercher un produit")
        print("5. Supprimer un produit")
        print("6. Dashboard")
        print("7. Quitter")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            print("Ajouter un produit")
            
            try:
                id = int(input("ID : ").strip())
            except ValueError:
                print("Erreur : L'ID du produit doit être un nombre entier")
                continue
            designation = input("Désignation : ").strip()   
            categorie = input("Catégorie : ").strip()
            
            try:
                quantite = int(input("Quantité : ").strip())
            except ValueError:               
                print("Quantité doit être un nombre entier")
                continue

            try:
                prix_unitaire = float(input("Prix unitaire : "))
            except ValueError:                
                print("Erreur : Le prix unitaire doit être un nombre")
                continue

            ajouter_produit(id, designation, categorie, quantite, prix_unitaire)


        elif choix == "2":
            print("Inventaire des produits :")
            afficher_inventaire()

        elif choix == "3":
            print("Mettre à jour le stock")  
            id = input("ID du produit à mettre à jour : ")
            # Gestion des erreurs de saisie pour la nouvelle quantité
            try:
                nouvelle_quantite = int(input("Nouvelle quantité : "))
            except ValueError:
                print("Erreur : La nouvelle quantité doit être un nombre entier")
                continue # retourner au menu principal si la saisie est invalide

            mettre_a_jour_stock(id, nouvelle_quantite)

        elif choix == "4":  
            print("Rechercher un produit")
            designation = input("Désignation du produit à rechercher : ")
            rechercher_produit(designation)

        elif choix == "5":
            print("Supprimer un produit")
            id = input("ID du produit à supprimer : ")
            supprimer_produit(id)

        elif choix == "6":
            print("Dashboard")
            dashboard()

        elif choix == "7":
            print("Au revoir!")
            if conn and conn.is_connected():
                conn.close()
            break
        else:
            print("Choix invalide")
            continue

# fonction de fermeture de la connexion à la base de données            
def fermer_connexion():
    global conn
    if conn and conn.is_connected():
        conn.close()   

choix_inscription_connexion()
menu()
fermer_connexion()