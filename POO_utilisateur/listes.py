#!/usr/bin/python3.4

import sys
sys.path.insert(0, "/home/etilawin/Documents/python/intro")
from modularites.print import *

#créations de listes
liste = list()
liste = []
liste = [2 , 2.5, 'hello', []]

liste.append(5) #Adding something at the end of the list
liste.insert(2, 'Bonjour') #Add "onjour" at the 3rd place
liste.remove('hello')
p(liste)

tuple1 = (1,)
tuple2 = (1,2,5)

#Transform strings into lists or in return
string = 'Salut tout le monde !'
StringInList = string.split(' ')
ListInString = ",".join(StringInList)

Ma_liste_test = [45, 43, 84, 8]
Ma_liste_test = [nb + 5 for nb in Ma_liste_test] # Weird syntax but easy to understand (simple way)
p(*Ma_liste_test)
Ma_liste_test2 = [45, 56, 3, 4, 6]
Ma_liste_test2 = [nb for nb in Ma_liste_test2 if nb % 2 == 0] # Will only print even numbers
                                                              # (Not working for floats)
p(Ma_liste_test2)


inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
 ]
inverse_inventaire = [(qte,nom) for nom,qte in inventaire] # Placing quantity before the name in a new list
p(inverse_inventaire)
inverse_inventaire.sort(reverse=True) # Sorting inverse_inventaire from the highest to the lowest
p(inverse_inventaire)
inventaire = [(nom,qte) for qte,nom in inverse_inventaire] # Replace inventaire by inverse_inventaire but with the right order
p(inventaire)
