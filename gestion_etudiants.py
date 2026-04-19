import tkinter as tk
from tkinter import messagebox

class GestionNotesBTS:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de Gestion des Notes - BTS")
        self.root.geometry("450x450")
        self.root.configure(bg="#f0f0f0")
        
        self.notes = []

        # --- Interface Graphique (GUI) ---
        
        # Titre
        self.lbl_title = tk.Label(root, text="Gestion des Notes Etudiants", font=("Arial", 16, "bold"), bg="#f0f0f0")
        self.lbl_title.pack(pady=20)

        # Zone Nom
        tk.Label(root, text="Nom de l'étudiant :", bg="#f0f0f0", font=("Arial", 10)).pack(pady=2)
        self.entry_nom = tk.Entry(root, font=("Arial", 12), width=30)
        self.entry_nom.pack(pady=5)

        # Zone Note
        tk.Label(root, text="Entrez une note (0-20) :", bg="#f0f0f0", font=("Arial", 10)).pack(pady=2)
        self.entry_note = tk.Entry(root, font=("Arial", 12), width=10)
        self.entry_note.pack(pady=5)

        # Bouton Ajouter
        self.btn_ajouter = tk.Button(root, text="Ajouter Note", command=self.ajouter_note, bg="#3498db", fg="white", font=("Arial", 10, "bold"), width=15)
        self.btn_ajouter.pack(pady=10)
        
        # Liste des notes affichées
        self.lbl_notes_liste = tk.Label(root, text="Notes saisies : []", bg="#f0f0f0", fg="#555")
        self.lbl_notes_liste.pack(pady=5)

        # Bouton Calculer et Sauvegarder
        self.btn_save = tk.Button(root, text="Calculer Moyenne & Enregistrer", command=self.calculer_et_sauvegarder, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"))
        self.btn_save.pack(pady=20)

    def ajouter_note(self):
        try:
            valeur = self.entry_note.get()
            note = float(valeur)
            if 0 <= note <= 20:
                self.notes.append(note)
                self.lbl_notes_liste.config(text=f"Notes saisies : {self.notes}")
                self.entry_note.delete(0, tk.END)
            else:
                messagebox.showwarning("Erreur", "La note doit être comprise entre 0 et 20")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide (ex: 15.5)")

    def calculer_et_sauvegarder(self):
        nom = self.entry_nom.get()
        if not nom or not self.notes:
            messagebox.showwarning("Attention", "Veuillez remplir le nom et ajouter au moins une note")
            return
        
        moyenne = sum(self.notes) / len(self.notes)
        
        # Sauvegarde dans le fichier texte
        try:
            with open("notes_bts.txt", "a", encoding="utf-8") as f:
                f.write(f"Etudiant: {nom} | Moyenne: {moyenne:.2f}/20 | Notes: {self.notes}\n")
            
            messagebox.showinfo("Succès", f"Résultat pour {nom}\nMoyenne: {moyenne:.2f}/20\nDonnées enregistrées !")
            
            # Réinitialisation (Reset)
            self.notes = []
            self.lbl_notes_liste.config(text="Notes saisies : []")
            self.entry_nom.delete(0, tk.END)
            
        except Exception as e:
            messagebox.showerror("Erreur Fichier", f"Impossible d'enregistrer : {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionNotesBTS(root)
    root.mainloop()