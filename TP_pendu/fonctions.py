#!/usr/bin/python3.4

import sys
import os
import pickle
from donnees import *
os.chdir('/home/etilawin/Documents/python/TP_pendu')

p = print

def check_name(name):
    """ Checking the name, its length"""
    name = str(name)
    if (len(name) < 3) or (len(name) > 10):
        check_name(input("Veuillez mettre entre 2 et 10 lettres : "))

def afficherMot():
    """Show the word with only the letters discovered"""
    for l in word:
        if l in lettre_trouvees:
            print(l)
        else:
            print('*')

def creer_scores():
    """Creating the object that contains the scores
    and add it to the file"""
    scores_vierge = {}
    with open('scores', 'wb') as scores:
        mon_pickler = pickle.Pickler(scores)
        mon_pickler.dump(scores_vierge)

def AddScore(name):
    """Function adding the nickname in the database"""
    with open('scores', 'rb') as scores:
        mon_depickler = pickle.Unpickler(scores)
        try:
            score_recupere = mon_depickler.load()
        except EOFError:
            creer_scores()
            AddScore(name)
        else:
            if name in score_recupere.keys():
                score_recupere[name] += int(chances)
            else:
                score_recupere[name] = chances
    with open('scores', 'wb') as scores:
        mon_pickler = pickle.Pickler(scores)
        mon_pickler.dump(score_recupere)

    print('ton nouveau score est ' + str(score_recupere[name]))
