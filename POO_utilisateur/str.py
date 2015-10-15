#!/usr/bin/python3.4

import sys
sys.path.insert(0, "/home/etilawin/Documents/python/intro")
from modularites.print import *


chaine = 'coucou mon frère'
chaine.upper() #Met en majuscule

type(chaine)   #Donne <class 'str'>
    # un objet est issu d'une classe <---- IMPORTANT*
    # La classe est une forme de type de donnée, sauf qu'elle permet de définir des fonctions et variables propres au type
    # Les objets, que j'ai présentés comme des variables, pouvant contenir d'autres variables ou fonctions (que l'on appelle méthodes).


# ---------------- Exemples de modules pour str ------------------------

chaine.lower() #met en minuscule
chaine.capitalize() #Met la première lettre en majuscule
chaine.center(50).encode() #Met au milieu avec 50 la taille finale qu'on souhaite obtenir

# ---------------- La méthode format -----------------------------------

zero = '.'
un = 26
formation = "ceci est un texte{0} Il se compose de exactement {1} lettres".format(zero, un)
formation2 ="""
 {no_rue}, {nom_rue}
    {code_postal} {nom_ville} ({pays})""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
        # Ici on remplace les nombres
        #Par des chaînes de caractères = autre possibilité mais obligé de nommer les variables avec le bon nom



age = 20
part1 = 'J\'ai actuellement'
final = part1 + str(age) + 'ans!'
final[0]
final[-1]
len(final) #Donne la longueur de la chaine en caractères (Attention les espaces et tout comptent!)



# ------------------ Parcourir une chaîne grâce à while/for ---------------

chaine2 = "Salut"
i = 0
while i < len(chaine2):
    p(chaine2[i])
    i += 1

# ------------------ Sélectionner une partie de la chaîne ------------------

mot = "coucou"
try:
    mot[0] = "k" #Ne marche pas
except:
    print("En effet ça ne marche pas, on obtient un TypeError")
    pass

presentation = "hello :3"

presentation[0:2]
presentation[:2]

presentation[2:len(presentation)]
presentation[2:]

mot = "k" + mot[1:] # Et la ça marche
