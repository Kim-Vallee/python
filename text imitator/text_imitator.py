# coding: utf8
# On importe toute les données nécessaires
from datas import *
from functions import *
import sys
import random

print('Veuillez entrer un texte de 1000 charactères ou plus : ')
texte = str(sys.stdin.read(1000)) # sys.stdin.read()
                                # permet de copier tout
                                # un texte.
texte = supprime_accent(texte) # On supprime les accents
longueur_texte = len(texte) # On récupère la longueur du texte

liste_text = []
for ltrs in texte: # On transforme tout le texte en liste
    liste_text.append(ltrs)

i = 0
while i < len(alphabet):
    # On récupère les positions (index) de la lettre alphabet[i]
    indices.append([j for j, x in enumerate(liste_text) if x == alphabet[i]])
    # On divise le nombres d'index obtenus par la longueur du texte puis on
    # Multiplie par mille pour obtenir un pourcentage (sur 1000 du coup)
    pourcentage_lettre.append(round((len(indices[i]) / longueur_texte)*1000))
    # Optionel: on affiche le résultat pour chaque lettre
    print('Le charactère ' + str(alphabet[i]) + ' à '+str(pourcentage_lettre[i])
     + ' chance sur mille d\'apparaître')
    i += 1

new_text_length = int(input('Please enter a length for the text to be created :\
 '))
