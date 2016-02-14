#!/usr/bin/python3.4
# coding: utf8
import sys
import random
"""File where all the functions are stocked"""
def notre_text(answer):
    """ Function testing user's answer"""
    if answer.lower() == 'y':
        texte1 = "The stacked magazines were seriously worn. The piles weren\'t\
         neat, didn't seem to be arranged by year or subject matter. They weren\'t\
         bound together, fastened to anything or stored in containers, which meant\
         sudden stops were potentially life-threatening. The cab was also full of\
         smoke, which I attributed to spontaneous mildew combustion, or a dropped\
         cigarette or ashtray overflow which resulted in a slow burn through slick\
         paper. Maybe the guy was deeply involved in bizarre barbecue hara-kiri \
         peep-show suicide."
    elif answer.lower() == 'n':
        print('Veuillez entrer un texte de 200 charactères ou plus : ')
        texte1 = str(sys.stdin.read(400)) # sys.stdin.read()
                                        # permet de copier tout
                                        # un texte.
    else:
        notre_text(str(input('Veuillez répondre par y/n : ')))
    return texte1

def supprime_accent(texte):
    """ supprime les accents du texte source """
    texte = texte.lower()
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
    i = 0
    while i < len(accent):
        texte = texte.replace(accent[i], sans_accent[i])
        i += 1
        return texte
