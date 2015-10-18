#!/usr/bin/python3.4

from modularites.print import *

print('un petit mot')
ma_variable = 53
print(ma_variable)

def division(nbr, multi = 2):
    """ Function that multiply any number by two if the 2nd arg has not been given """
    p(nbr / multi)

#division(5, 4)
#division(4)

def carre(nbr):
    return nbr * nbr

carre(5) #Nothing happends
carre_de_5 = carre(5)
p(carre_de_5) #Now 25 appears so "print" != "return" (also "return" end the function proceedings)

ma_fonction_lambda = lambda nbr: nbr * 2
p(ma_fonction_lambda(3))

def args_unknown(arg1, arg2, *reste):
    nbr = arg1 * arg2
    p(nbr)
    reste = list(reste)
    p(reste)

args_unknown(2, 3, 'hello', 'my name is bryan', 'ça marche!')



def afficher(*parametres, sep=' ', fin='\n'):
    """Fonction chargée de reproduire le comportement de print.
    Elle doit finir par faire appel à print pour afficher le résultat.
    Mais les paramètres devront déjà avoir été formatés.
    On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :
    print(chaine, end='')"""
    # args have tuple form
    # So we need to convert them
    parametres = list(parametres)
    # Every value gets in str
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    # Creating the final str
    chaine = sep.join(parametres)
    chaine += fin
    print(chaine, end='')


ma_liste = [45,56,34,67]
print(*ma_liste) # Transform each value in arguments
