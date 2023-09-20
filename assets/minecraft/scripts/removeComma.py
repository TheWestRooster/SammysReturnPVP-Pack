def enlever_derniere_virgule(fichier):
    # Lire le contenu du fichier
    contenu = fichier.read()
    
    # Vérifier si le contenu est vide ou ne contient pas de virgule
    if not contenu or ',' not in contenu:
        print("Le fichier est vide ou ne contient pas de virgule.")
        return
    
    # Trouver l'index de la dernière virgule
    dernier_index_virgule = contenu.rfind(',')
    
    # Supprimer la dernière virgule
    contenu_modifie = contenu[:dernier_index_virgule] + contenu[dernier_index_virgule+1:]
    
    # Réécrire le contenu modifié dans le fichier
    fichier.seek(0)
    fichier.write(contenu_modifie)
    fichier.truncate()
    print("Dernière virgule supprimée avec succès.")

# Exemple d'utilisation
try:
    # Ouvrir le fichier en mode lecture/écriture
    with open('sounds.json', 'r+') as fichier:
        enlever_derniere_virgule(fichier)
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé.")
except PermissionError:
    print("Vous n'avez pas les permissions nécessaires pour accéder au fichier.")
except Exception as e:
    print(f"Une erreur s'est produite : {str(e)}")