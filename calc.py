# --- PROGRAMME : CALCULATRICE PROFESSIONNELLE ---

# Définition des fonctions pour chaque opération
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur: Division par zéro impossible"
    return a / b

# Boucle principale (Pour que le programme reste ouvert)
while True:
    print("\n--- MENU DE CALCUL ---")
    
    user_input = input("Entrez le 1er nombre (ou 'quitter' pour finir): ")
    
    if user_input.lower() == 'quitter':
        print("Fin du programme...")
        break
    
    try:
        # Conversion de l'entrée en nombre décimal
        num1 = float(user_input)
        
        op = input("Choisissez l'opérateur (+, -, *, /): ")
        num2 = float(input("Entrez le 2ème nombre: "))

        # Logique de calcul
        if op == '+':
            print(f"Résultat: {addition(num1, num2)}")
        elif op == '-':
            print(f"Résultat: {soustraction(num1, num2)}")
        elif op == '*':
            print(f"Résultat: {multiplication(num1, num2)}")
        elif op == '/':
            print(f"Résultat: {division(num1, num2)}")
        else:
            print("Erreur: Opérateur non reconnu.")

    except ValueError:
        print("Erreur: Veuillez saisir des nombres valides.")

print("-----------------------")