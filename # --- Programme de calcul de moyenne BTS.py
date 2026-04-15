# --- Programme de calcul de moyenne BTS ---

def calculer_moyenne(notes):
    return sum(notes) / len(notes)

print("--- GESTION DES NOTES ---")

notes_liste = []
while True:
    saisie = input("Entrez une note (أو اكتب 'fin' باش تحسب): ")
    
    if saisie.lower() == 'fin':
        break
    
    try:
        note = float(saisie)
        if 0 <= note <= 20:
            notes_liste.append(note)
        else:
            print("Erreur: La note doit être entre 0 et 20.")
    except ValueError:
        print("Erreur: Veuillez saisir un nombre.")

if notes_liste:
    moyenne = calculer_moyenne(notes_liste)
    print(f"\nNombre de modules: {len(notes_liste)}")
    print(f"Votre moyenne générale est: {moyenne:.2f}")
    
    if moyenne >= 10:
        print("Résultat: Admis (ناجح) 🎉")
    else:
        print("Résultat: Ajourné (راسب)")
else:
    print("Aucune note saisie.")