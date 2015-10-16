#!/usr/bin/python3.4

import sys
sys.path.insert(0, "/home/etilawin/Documents/python/intro")
from modularites.print import *

#créations de listes
liste = list()
liste = []
liste = [2 , 2.5, 'hello', []]

liste.append(5) #Adding something at the end of the list
liste.remove('hello')
p(liste)
