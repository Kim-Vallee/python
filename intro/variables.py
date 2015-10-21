#!/usr/bin/python3.4

def p(*args):
    print(*args)

#Deux variables différentes
name_of_the_var = 'valeur'
Name_Of_The_Var = 'valeur'
float1 = 3.5
int1 = 3
str1 = 'hello'
str2 = """ C'est
sur
plusieurs
lignes """
int1 += 3 # = 6
a, b = 5, 6 # Multiples allocations to variables


#Impossible to use these words
'''and del from none true as elif global nonlocal try assert else if not while
break except import or with class false in pass yield continue finally is
raise def for lambda return'''


del int1
