import tkinter as tk
from tkinter import messagebox

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
        label_resultat.config(text=f"{res}", fg="#ffffff")
    except ValueError:
        messagebox.showerror("Erreur", "Nombres invalides !")

# الإعدادات ديال الألوان (Theme)
BG_COLOR = "#2c3e50"     # أزرق غامق للخلفية
BTN_COLOR = "#3498db"    # أزرق فاتح للأزرار
TEXT_COLOR = "#ecf0f1"   # أبيض مائل للرمادي للنصوص

root = tk.Tk()
root.title("COLCULATRICE PRO - HASSAN")
root.geometry("350x500")
root.config(bg=BG_COLOR)

# عنوان البرنامج
tk.Label(root, text="CALCULATRICE PRO", font=("Helvetica", 16, "bold"), 
         bg=BG_COLOR, fg=BTN_COLOR).pack(pady=20)

# خانات الإدخال بستايل نقي
tk.Label(root, text="Nombre 1", bg=BG_COLOR, fg=TEXT_COLOR).pack()
entry1 = tk.Entry(root, font=("Arial", 14), bd=0, highlightthickness=2)
entry1.config(highlightbackground="#bdc3c7", highlightcolor=BTN_COLOR)
entry1.pack(pady=10, ipady=5)

tk.Label(root, text="Nombre 2", bg=BG_COLOR, fg=TEXT_COLOR).pack()
entry2 = tk.Entry(root, font=("Arial", 14), bd=0, highlightthickness=2)
entry2.config(highlightbackground="#bdc3c7", highlightcolor=BTN_COLOR)
entry2.pack(pady=10, ipady=5)

# اختيار العمليات (Radiobuttons)
v = tk.StringVar(root, "+")
frame_op = tk.Frame(root, bg=BG_COLOR)
frame_op.pack(pady=10)

for op in ["+", "-", "*", "/"]:
    tk.Radiobutton(frame_op, text=op, variable=v, value=op, 
                   bg=BG_COLOR, fg=TEXT_COLOR, selectcolor="#34495e",
                   font=("Arial", 12, "bold")).side = tk.LEFT
    tk.Radiobutton(frame_op, text=op, variable=v, value=op, 
                   bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

# زر الحساب بستايل عصري
btn_calc = tk.Button(root, text="CALCULER", command=calculer, 
                    bg=BTN_COLOR, fg="white", font=("Arial", 12, "bold"),
                    bd=0, cursor="hand2", activebackground="#2980b9")
btn_calc.pack(pady=30, ipadx=40, ipady=10)

# منطقة النتيجة
tk.Label(root, text="RÉSULTAT", bg=BG_COLOR, fg=BTN_COLOR, font=("Arial", 10)).pack()
label_resultat = tk.Label(root, text="0.0", font=("Helvetica", 24, "bold"), 
                         bg=BG_COLOR, fg=TEXT_COLOR)
label_resultat.pack()

root.mainloop()