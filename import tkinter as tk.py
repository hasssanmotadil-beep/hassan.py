import tkinter as tk
from tkinter import messagebox

# --- FONCTIONS DE CALCUL ---
def executer_calcul():
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        op = variable_op.get()
        
        if op == "+": res = n1 + n2
        elif op == "-": res = n1 - n2
        elif op == "*": res = n1 * n2
        elif op == "/":
            if n2 == 0:
                messagebox.showerror("Erreur", "Division par zéro impossible !")
                return
            res = n1 / n2
        
        label_resultat.config(text=f"Résultat : {res}", fg="green")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")

# --- CRÉATION DE L'INTERFACE ---
root = tk.Tk()
root.title("BTS Calculatrice - Hassan")
root.geometry("350x450")
root.config(padx=20, pady=20)

# Titre
tk.Label(root, text="Calculatrice Scientifique", font=("Arial", 14, "bold")).pack(pady=10)

# Champs de saisie
tk.Label(root, text="Premier Nombre :").pack()
entry_n1 = tk.Entry(root, font=("Arial", 12))
entry_n1.pack(pady=5)

tk.Label(root, text="Deuxième Nombre :").pack()
entry_n2 = tk.Entry(root, font=("Arial", 12))
entry_n2.pack(pady=5)

# Menu des opérations
tk.Label(root, text="Choisir l'opération :").pack(pady=5)
variable_op = tk.StringVar(root)
variable_op.set("+") # Valeur par défaut
options = tk.OptionMenu(root, variable_op, "+", "-", "*", "/")
options.pack(pady=5)

# Bouton Calculer
btn = tk.Button(root, text="CALCULER", command=executer_calcul, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"))
btn.pack(pady=20, fill="x")

# Résultat
label_resultat = tk.Label(root, text="Résultat : --", font=("Arial", 12, "bold"))
label_resultat.pack(pady=10)

root.mainloop()