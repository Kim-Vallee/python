#!/usr/bin/python3.4

from modularites.print import *

print('un petit mot')
ma_variable = 53
print(ma_variable)

def division(nbr, multi = 2):
    """ Function that multiply any number by two if the 2nd arg has not been given """
    p(nbr / multi)

# Division(5, 4)
# Division(4)

def square(nbr):
    return nbr * nbr

square(5) # Nothing happends
square_5 = square(5)
p(square_5) # Now 25 appears so "print" != "return" (also "return" end the function proceedings)

my_lambda_function = lambda nbr: nbr * 2
p(my_lambda_function(3))

def args_unknown(arg1, arg2, *reste):
    nbr = arg1 * arg2
    p(nbr)
    reste = list(reste)
    p(reste)

args_unknown(2, 3, 'hello', 'my name is bryan', 'ça marche!')



def stick_up(*parametres, sep=' ', fin='\n'):
    """Function acting as print()
    But args must have been formated
    We must give print a simple str, and specify to end with nothing :
    print(chaine, end='')"""
    # Args have tuple form
    # So we need to convert them
    parametres = list(parametres)
    # Every value gets in str
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    # Creating the final str
    chaine = sep.join(parametres)
    chaine += fin
    print(chaine, end='')


my_list = [45,56,34,67]
print(*my_list) # Transform each value in arguments


# What about fuction with unexistant named args?

def dictionnary(**kwargs):
    p("the different args given are {}".format(kwargs))
dictionnary(name='my_name',nickname='Etilawin',other='other')
