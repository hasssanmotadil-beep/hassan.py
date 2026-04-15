import tkinter as tk
from tkinter import messagebox

# Fonctions de calcul
def calculer():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        op = v.get()
        
        if op == "+": res = n1 + n2
        elif op == "-": res = n1 - n2
        elif op == "*": res = n1 * n2
        elif op == "/":
            if n2 != 0: res = n1 / n2
            else: 
                messagebox.showerror("Erreur", "Division par zéro!")
                return
        
        label_resultat.config(text=f"Résultat: {res}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")

# Fenêtre principale
root = tk.Tk()
root.title("Calculatrice BTS - Hassan")
root.geometry("300x400")

# Champs de saisie
tk.Label(root, text="Nombre 1:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Nombre 2:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Choix de l'opération
v = tk.StringVar(root, "+")
tk.Label(root, text="Opération:").pack(pady=5)
for text in ["+", "-", "*", "/"]:
    tk.Radiobutton(root, text=text, variable=v, value=text).pack()

# Bouton Calculer
tk.Button(root, text="Calculer", command=calculer, bg="blue", fg="white").pack(pady=20)

# Résultat
label_resultat = tk.Label(root, text="Résultat: ", font=("Arial", 12, "bold"))
label_resultat.pack()

root.mainloop()