#!/usr/bin/python3.4
# coding: utf8
"""Main file to run"""
# On importe toute les données nécessaires
from datas import *
from functions import *
import sys
import random

texte = notre_text(str(input('Voulez vous utiliser un de nos texte ? [y/n] : ')))
texte = supprime_accent(texte) # On supprime les accents
longueur_texte = len(texte) # On récupère la longueur du texte

for ltrs in texte: # On transforme tout le texte en liste
    liste_text.append(ltrs)

# On récupère les chances d'avoir une lettre après une autre
i = 0
while i <len(alphabet): # On parcours tout l'alphabet
    # On regarde où se situent les différents index de la lettre
    indices.append([j for j, x in enumerate(liste_text) if x == alphabet[i]])
    # On reset les variables temporaires
    temp_list = []
    temp_list_chance = []
    temp_last = 0

    j = 0
    # On fait tourner jusqu'à ce qu'il n'y ait plus de correspondance avec cette lettre
    # Voir l.23
    while j < len(indices[i]):
        # Try / except pour éviter les erreurs de dernier charactère
        try:
            # On stock les lettres suivants la lettre alphabet[i] dans temp_list
            temp_list.append(liste_text[indices[i][j] + 1])
        except IndexError:
            pass
        finally:
            j += 1

    g = 0
    while g < len(alphabet):
        if (temp_list.count(alphabet[g])) != 0: # On évite les zéros inutiles
            # Try catch pour éviter la division par zero
            try:
                # On compte le nombre de fois qu'il y a de lettre alphabet[g] après
                # la lettre alphabet[i] et on le met en pourcentage
                percent = round((temp_list.count(alphabet[g])/len(temp_list))*100)
                # Pour éviter d'avoir un pourcentage supérieur à zero à cause des
                # arrondis
                if((percent + temp_last) > 100):
                    percent = 100
                    temp_last = 0
                # On ajoute à une liste temporaire un tuple (ici sous forme de liste)
                # qui servira à completer un dico
                temp_list_chance.append([alphabet[g],percent + temp_last])
                # Pour des raisons de facilité d'aléatoire, la probabilité vaut
                # la probabilité originiel + les probabilités précédentes
                temp_last += percent
            except ZeroDivisionError:
                pass
        g += 1
    # On ajoute la liste temp_list_chance au dico qui vaut
    # letter: [[following letter, percent][another following letter,another percent]]
    chance_after_letter[alphabet[i]] = temp_list_chance
    i += 1

splitted_txt = texte.split()
print(splitted_txt)
print(splitted_txt[0][0])
