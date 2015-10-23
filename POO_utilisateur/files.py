#!/usr/bin/python3.4

import sys
import os
import pickle
sys.path.insert(0, "/home/etilawin/Documents/python/intro")
os.chdir('/home/etilawin/Documents/python/fichiers') # Python knows where to open files (as if we were in the dir)
from modularites.print import *

fichier = open('fichier.txt', 'r')
contenu = fichier.read()
p(contenu)
fichier.close() # Never forget to close a file, as soon as you open it
                # I advice to write the close statment to be sure not to
                # forget it
del fichier

fichier = open('fichier.txt', 'w')
fichier.write('J\'ai tout remplacé c\'est ouf non :o!')
fichier.close()
del fichier

with open('fichier.txt', 'r') as fichier: # It closes automatically the file
    p(fichier.read())

# fichier.closed() Not working I don't know why. To check
armes = {
    'massue' : 1,
    'épée' : 2,
    'couteau' : 1,
    'poings' : 10,
}
with open('donnees', 'wb') as donnees: # b following w means binary
    my_pickler = pickle.Pickler(donnees)
    my_pickler.dump(armes) # Add objects in donnees

with open('donnees', 'rb') as donnees:
    my_pickler = pickle.Unpickler(donnees)
    score = my_pickler.load() # Loads only one object so if more than one must
                              # call more than once

p(score)
