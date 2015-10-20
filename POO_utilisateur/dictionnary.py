#!/usr/bin/python3.4

import sys
sys.path.insert(0, "/home/etilawin/Documents/python/intro")
from modularites.print import *

dictionnary = dict()
dictionnary = {}
p(type(dictionnary))

dictionnary["pseudo"] = 'Etilawin'
dictionnary["password"] = 'password'
dictionnary["email"] = 'kimik@hotmail.fr'
p(dictionnary)
del dictionnary["password"]
p(dictionnary)
old_email = dictionnary.pop('email') # Shorter than just before as it prints the value
p(old_email)

def coucou():
    print('Voilà je suis la fonction la plus inutile du monde : coucou')
def hibou():
    print('hiboux coucou hiboux...')

functions = {}
functions['c'] = coucou
functions['h'] = hibou
functions['c']()
