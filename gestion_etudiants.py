# --- SYSTÈME DE GESTION DES NOTES (AVEC SAUVEGARDE) ---

def sauvegarder_donnees(nom, moyenne):
    # 'a' signifie 'append' : ajouter à la fin du fichier sans effacer
    with open("notes_bts.txt", "a", encoding="utf-8") as fichier:
        fichier.write(f"Étudiant: {nom} | Moyenne: {moyenne:.2f}/20\n")
    print("✅ Données sauvegardées dans notes_bts.txt")

def calculer_moyenne(notes):
    return sum(notes) / len(notes) if notes else 0

# Programme Principal
print("--- BIENVENUE DANS LE GESTIONNAIRE BTS ---")

nom_etudiant = input("Nom de l'étudiant : ")
notes = []

while True:
    saisie = input(f"Entrez une note pour {nom_etudiant} (ou 'stop') : ")
    if saisie.lower() == 'stop':
        break
    try:
        n = float(saisie)
        if 0 <= n <= 20:
            notes.append(n)
        else:
            print("❌ La note doit être entre 0 et 20.")
    except ValueError:
        print("❌ Veuillez entrer un nombre valide.")

if notes:
    moy_generale = calculer_moyenne(notes)
    print(f"\nRésultat pour {nom_etudiant}:")
    print(f"Moyenne : {moy_generale:.2f}/20")
    
    # Appel de la fonction de sauvegarde
    sauvegarder_donnees(nom_etudiant, moy_generale)
else:
    print("Aucune note enregistrée.")