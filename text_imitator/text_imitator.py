#!/usr/bin/python3.4
# coding: utf8
"""Main file to run"""
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

liste_text = list()
for ltrs in texte: # On transforme tout le texte en liste
    liste_text.append(ltrs)

# i = 0
# while i < len(alphabet):
#     # On récupère les positions (index) de la lettre alphabet[i]
#     # On divise le nombres d'index obtenus par la longueur du texte puis on
#     # Multiplie par mille pour obtenir un pourcentage (sur 1000 du coup)
#     # pourcentage_lettre.append(round((len(indices[i]) / longueur_texte)*1000))
#     # # Optionel: on affiche le résultat pour chaque lettre
#     # print('Le charactère ' + str(alphabet[i]) + ' à '+str(pourcentage_lettre[i])\
#     #  + ' chance sur mille d\'apparaître')
#     i += 1

i = 0
while i <len(alphabet):
    indices.append([j for j, x in enumerate(liste_text) if x == alphabet[i]])
    temp_list = []
    temp_list_chance = []
    temp_last = 0

    j = 0
    while j < len(indices[i]):
        try:
            temp_list.append(liste_text[indices[i][j] + 1])
        except IndexError:
            pass
        finally:
            j += 1

    g = 0
    while g < len(alphabet):
        if (temp_list.count(alphabet[g])) != 0:
            try:
                percent = round((temp_list.count(alphabet[g])/len(temp_list))*100, 1)
                if((percent + temp_last) > 100):
                    percent = 100
                    temp_last = 0
                temp_list_chance.append([alphabet[g],percent + temp_last])
                temp_last += round((temp_list.count(alphabet[g])/len(temp_list))*100)
            except ZeroDivisionError:
                pass
        g += 1

    chance_after_letter[alphabet[i]] = temp_list_chance
    i += 1
print(chance_after_letter)
print('\n\n\n')
print(chance_after_letter['f'])
print(len(alphabet))

new_text_length = int(input('Please enter a length for the text to be created :\
'))
first_letter = alphabet[random.randrange(0,25)]
createdtxt += first_letter

i = 0
while i < new_text_length:
    print(createdtxt)
    temp_inf = chance_after_letter[createdtxt[i]]
    temp_rand = random.randrange(0,100)
    print(temp_rand)
    j = 0
    while j < len(chance_after_letter[createdtxt[i]]):
        if chance_after_letter[createdtxt[i]][j] == chance_after_letter[createdtxt[i]][0]:
            if temp_rand >= 0 and temp_rand \
            <= chance_after_letter[createdtxt[i]][j+1][1]:
                createdtxt += chance_after_letter[createdtxt[i]][j][0]
                break
            else:
                j += 1
                continue
        elif temp_rand >= chance_after_letter[createdtxt[i]][j][1] and temp_rand \
        <= chance_after_letter[createdtxt[i]][j+1][1]:
            createdtxt += chance_after_letter[createdtxt[i]][j][0]
            break
        else:
            j += 1
    i += 1
