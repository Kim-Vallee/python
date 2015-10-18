#!/usr/bin/python3.4

from modularites.print import *

nb = 20
i = 0
while i <= nb:
    p("Nombre numéro : {}".format(i))
    i += 1

chaine = "Coucou"
for letter in chaine: #letter takes successively the value of each of the letters one by one
    if letter in "aeiouyAEIOUY": #Another use of "in" word
        p(letter)
    else:
        p("*")

while True:
    leave = input("Entrez Q pour quitter : ")
    if leave.lower() == "q":
        p("bye")
        break

x = 1
while x < 20:
    if x % 3 == 0:
        x += 4
        p("on ajoute 4 x vaut {}".format(x))
        continue
    else:
        x += 1
        p(x)


my_list = ['coucou', 'Ma bite', 'Mes bites']
for i, elt in enumerate(my_list):
   print("À l'indice {} se trouve {}.".format(i, elt)) #Creates tuples: as lists but not editable
