#!/usr/bin/python3.4

import sys
sys.path.insert(0, "/home/etilawin/Documents/python/intro")
from modularites.print import *

dictionnary = dict()
dictionnary = {}
p(type(dictionnary))

dictionnary["pseudo"] = 'Etilawin'
dictionnary["password"] = '9568574531'
dictionnary["email"] = 'kimik@hotmail.fr'
p(dictionnary)
# del dictionnary["password"]
# p(dictionnary)
# old_email = dictionnary.pop('email') # Different because .pop method print the value which is deleted
# p(old_email)

def coucou():
    print('Voilà je suis la fonction la plus inutile du monde : coucou')
def hibou():
    print('hiboux coucou hiboux...')

functions = {}
functions['c'] = coucou
functions['h'] = hibou
functions['c']()

for cle in dictionnary:
    print(cle) # Will show keys in a random way but not their values

for values in dictionnary.values():
    print(values) # Now will show the values thx to method values

for key,value in dictionnary.items():
    print('Votre {} est : {}'.format(key,value)) # Shows both keys and values

# About dictionnaries in functions look in fonctions.py line 59-61
