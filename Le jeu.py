import random

option = ["🗿", "📄", "✂"]
Lettre_to_emoji = {"r" : "🗿", "p" : "📄", "c" : "✂"}

def choisir_arme():
    while True:
        try:
            joueur = input("Choisir ton arme entre une roche (r), du papier (p) ou une paire de ciseaux (c) : ").lower()
            if joueur not in Lettre_to_emoji:
                raise ValueError("Choix invalide")
            return Lettre_to_emoji[joueur]
        except ValueError:
            print("Choisis entre r pour roche, p pour papier ou c pour ciseaux.")
def game():
    ordinateur = random.choice(option)
    joueur = choisir_arme()

    if joueur== "🗿":
        rocher(joueur, ordinateur)
    elif joueur == "📄":
        papier(joueur, ordinateur)
    elif joueur == "✂":
        ciseaux(joueur, ordinateur)

def rocher(joueur, adversaire):
    if adversaire == "🗿":
        print(f"Égalité. Un combat de tête dur ne mêne à rien. {joueur}  vs {adversaire}.")
    elif adversaire == "📄":
        print(f"Perdu. Tu t'es fait envelopper.{joueur}  vs {adversaire}. ")
    elif adversaire == "✂":
        print(f"Gagné! Tu as détruit les ciseaux. {joueur}  vs {adversaire}.")

def papier(joueur, adversaire):
    if adversaire == "🗿":
        print(f"Gagné! Tu as enveloppé la roche. {joueur}  vs {adversaire}.")
    elif adversaire == "📄":
        print(f"Égalité. Deux feuilles de papier ne peuvent pas se surpasser. {joueur}  vs {adversaire}.")
    elif adversaire == "✂":
        print(f"Perdu. Tu t'es fait découper.{joueur}  vs {adversaire}. ")
        

def ciseaux(joueur, adversaire):
    if adversaire == "🗿":
        print(f"Perdu. Tu t'es fait écraser.{joueur}  vs {adversaire}. ")
    elif adversaire == "📄":
        print(f"Gagné! Tu as découpé le papier. {joueur}  vs {adversaire}.")
    elif adversaire == "✂":
        print(f"Égalité. Un combat de ciseaux ne mène à rien (sauf pour des lesbiennes). {joueur}  vs {adversaire}.")

game()