#!/usr/bin/python3.4

import sys
import os
import random as r
from donnees import *
from fonctions import *

end = False
while end == False:
    afficherMot()
    lettre = str(input("Veuillez choisir une lettre : "))
    if lettre in word and lettre not in lettre_trouvees and lettre != "":
        print('la lettre est dans le mot!')
        lettre_trouvees.append(lettre)
    elif lettre not in word:
        print('la lettre n\'est pas dans le mot!')
        chances = chances - 1
    elif lettre in lettre_trouvees:
        print('Tu as déjà trouvé cette lettre!')
    elif lettre == "":
        print('Tu n\'as pas rentré de lettre!')
    print('il vous reste ' + str(chances) + ' chances')
    if chances == 0 or sorted(mot_decompose) == sorted(lettre_trouvees):
        print("Bravo tu as trouvé le mot" + word)
        end = True
nickname = str(input('Ton pseudo : '))
check_name(nickname)
AddScore(nickname)
