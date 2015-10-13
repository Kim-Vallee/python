#!/usr/bin/python3.4

def p(*args):
    print(args)

chaine = 'coucou mon frère'
chaine.upper() #Va mettre la chaîne en majuscule grâce
               #Upper est une fonction et le "." permet (comme avec les modules) d'exprimer l'appartenance
               #applicable sur TOUTE les chaînes de caractères

type(chaine)   #Donne <class 'str'>
    # un objet est issu d'une classe <---- IMPORTANT*
    # La classe est une forme de type de donnée, sauf qu'elle permet de définir des fonctions et variables propres au type
    #Les objets, que j'ai présentés comme des variables, pouvant contenir d'autres variables ou fonctions (que l'on appelle méthodes).
    # On appelle une méthode d'un objet grâce à objet.methode()
# ---------------- Exemples de modules pour str ------------------------
chaine.lower() #met en minuscule
chaine.capitalize() #Met la première lettre en majuscule
chaine.center(50).encode() #Met au milieu avec 50 la taille finale qu'on souhaite obtenir
                           #On peut aussi voir que l'on peut ajouter deux methodes à la suite
# ---------------- La méthode format -----------------------------------
zero = '.'
un = 26
formation = "ceci est un texte{0} Il se compose de exactement {1} lettres".format(zero, un) #Qq explications:
                        #Si tu te souviens pas, la methode format permet que lorsque Python exécute cette méthode,
                        #il remplace dans notre chaîne {0} par la première variable passée à la méthode format
                        #, {1} par la deuxième variable… et ainsi de suite.
