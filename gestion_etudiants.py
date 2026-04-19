import tkinter as tk
from tkinter import messagebox, ttk

class GestionBTSPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de Gestion BTS - Version Pro")
        self.root.geometry("500x600")
        self.root.configure(bg="#ecf0f1")
        
        self.data_notes = [] 

        # --- Style & UI ---
        title = tk.Label(root, text="Gestionnaire de Notes BTS", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="white", pady=10)
        title.pack(fill=tk.X)

        # Zone Nom
        frame_top = tk.Frame(root, bg="#ecf0f1")
        frame_top.pack(pady=10)
        
        tk.Label(frame_top, text="Nom de l'étudiant:", bg="#ecf0f1").grid(row=0, column=0, padx=5)
        self.entry_nom = tk.Entry(frame_top, font=("Arial", 11))
        self.entry_nom.grid(row=0, column=1, padx=5)

        # Zone Saisie Note et Coeff
        frame_input = tk.LabelFrame(root, text=" Saisie des Notes ", bg="#ecf0f1", padx=10, pady=10)
        frame_input.pack(pady=10, padx=20, fill=tk.X)

        tk.Label(frame_input, text="Note (0-20):", bg="#ecf0f1").grid(row=0, column=0)
        self.entry_note = tk.Entry(frame_input, width=8)
        self.entry_note.grid(row=0, column=1, padx=5)

        tk.Label(frame_input, text="Coefficient:", bg="#ecf0f1").grid(row=0, column=2)
        self.entry_coeff = tk.Entry(frame_input, width=8)
        self.entry_coeff.insert(0, "1")
        self.entry_coeff.grid(row=0, column=3, padx=5)

        tk.Button(frame_input, text="Ajouter à la liste", command=self.ajouter_ligne, bg="#3498db", fg="white").grid(row=1, columnspan=4, pady=10)

        # Tableau (Treeview)
        self.tree = ttk.Treeview(root, columns=("Note", "Coeff"), show='headings', height=6)
        self.tree.heading("Note", text="Note / 20")
        self.tree.heading("Coeff", text="Coefficient")
        self.tree.pack(pady=10, padx=20, fill=tk.X)

        # Boutons d'action
        btn_frame = tk.Frame(root, bg="#ecf0f1")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Calculer & Sauvegarder", command=self.finaliser, bg="#27ae60", fg="white", font=("Arial", 10, "bold"), padx=10).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Réinitialiser", command=self.reset, bg="#e74c3c", fg="white", padx=10).pack(side=tk.LEFT, padx=5)

    def ajouter_ligne(self):
        try:
            n = float(self.entry_note.get())
            c = float(self.entry_coeff.get())
            if 0 <= n <= 20 and c > 0:
                self.data_notes.append((n, c))
                self.tree.insert("", tk.END, values=(f"{n}/20", c))
                self.entry_note.delete(0, tk.END)
            else:
                messagebox.showwarning("Erreur", "Note entre 0-20 et Coeff > 0")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des chiffres valides")

    def get_mention(self, moy):
        if moy >= 16: return "Très Bien"
        elif moy >= 14: return "Bien"
        elif moy >= 12: return "Assez Bien"
        elif moy >= 10: return "Passable"
        else: return "Ajourné"

    def finaliser(self):
        nom = self.entry_nom.get()
        if not nom or not self.data_notes:
            messagebox.showwarning("Attention", "Nom ou notes manquants")
            return

        total_points = sum(n * c for n, c in self.data_notes)
        total_coeffs = sum(c for n, c in self.data_notes)
        moyenne = total_points / total_coeffs
        
        mention = self.get_mention(moyenne)
        statut = "ADMIS" if moyenne >= 10 else "AJOURNÉ"

        resultat_txt = f"Résultat: {statut}\nMoyenne: {moyenne:.2f}/20\nMention: {mention}"
        
        with open("notes_bts_complet.txt", "a", encoding="utf-8") as f:
            f.write(f"Etudiant: {nom} | Moyenne: {moyenne:.2f} | Statut: {statut} | Mention: {mention}\n")
        
        messagebox.showinfo(f"Bilan de {nom}", resultat_txt)
        self.reset()

    def reset(self):
        self.data_notes = []
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.entry_nom.delete(0, tk.END)
        self.entry_note.delete(0, tk.END)
        self.entry_coeff.delete(0, tk.END)
        self.entry_coeff.insert(0, "1")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionBTSPro(root)
    root.mainloop()
      