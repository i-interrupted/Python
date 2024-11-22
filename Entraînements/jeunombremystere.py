import random 

# L'ordinateur choisit un nombre aléatoire
nombre_mystere = random.randint(1, 100)

#Initialisation des variables
trouve = False
essais = 0

print("Bienvenue dans le jeu du Nombre Mystère !")
print("Devinez le nombre entre 1 et 100")

# Demander une entrée de l'utilisateur
while not trouve: 
   try:
      essai = int(input("Entrez un nombre : "))
      essais += 1

# Vérification de l'entrée
      if essai > nombre_mystere :
        print("C'est trop grand !")
      elif essai < nombre_mystere :
        print("C'est trop petit !")
      else:
        print(f"Bravo ! Vous avez trouvé le nombre mystère en {essais} essais.")
        trouve = True  
   except ValueError:
     print("Veuillez rentrer un nombre.")