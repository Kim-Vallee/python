#!/usr/bin/python3.4

def p(*args):
    print(*args)
a = 5
b = 6
if a > b:
    p("en effet a vaut {} et b vaut {}".format(a, b))
elif a < b:
    p("en effet a vaut {} et b vaut {}".format(a, b))
else:
    p("en effet a vaut {} et b vaut {} donc ils sont égaux".format(a, b))

booleen = True
if booleen is not True:
    p("La variable n'est pas vraie")
elif booleen is True:
    p('la variable est vraie')
else:
    p("la variable n'est pas booleen")


# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

annee = input("Saisissez une année : ")
try: # Pour test si la personne aurait pas mis autre chose
    annee = int(annee)
except:
    p('On a demandé un nombre!')
else:
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")
