#!/usr/bin/python3.4

import sys
import os
import random as r

list_of_word = [
    'concours',
    'joie',
    'vie',
    'test',
    'anticonstitution',
    'mediter',
]
lettre_trouvees = []

fini = False

word = list_of_word[r.randrange(0, len(list_of_word))]

chances = 8

mot_decompose = []
for l in word:
    if l not in mot_decompose:
        mot_decompose.append(l)
