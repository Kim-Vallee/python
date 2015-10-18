#!/usr/bin/python3.4

import sys
sys.path.insert(0, "/home/etilawin/Documents/python/intro")
from modularites.print import *

#créations de listes
liste = list()
liste = []
liste = [2 , 2.5, 'hello', []]

liste.append(5) #Adding something at the end of the list
liste.insert(2, 'Bonjour') #Add "onjour" at the 3rd place
liste.remove('hello')
p(liste)

tuple1 = (1,)
tuple2 = (1,2,5)

#Transform strings into lists or in return
string = 'Salut tout le monde !'
StringInList = string.split(' ')
ListInString = ",".join(StringInList)

Ma_liste_test = [45, 43, 84, 8]
Ma_liste_test = [st + 5 for st in Ma_liste_test] # Weird syntax but easy to understand
print(*Ma_liste_test)
