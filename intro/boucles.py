#!/usr/bin/python3.4

from modularites.print import *

nb = 20
i = 0
while i <= nb:
    p("Nombre numéro : {}".format(i))
    i += 1

chaine = "Coucou"
for lettre in chaine: #Lettre takes successively the value of each of the letters one by one
    if lettre in "aeiouyAEIOUY": #Another use of "in" word
        p(lettre)
    else:
        p("*")

while True:
    sortir = input("Entrez Q pour sortir : ")
    if sortir.lower() == "q":
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
