#!/usr/bin/python3.4

def p(*args):
    print(*args)

print('un petit mot')
ma_variable = 53
print(ma_variable)

def division(nbr, multi = 2):
    """ Function that multiply any number by two if the 2nd arg has not been given """
    p(nbr / multi)

#division(5, 4)
#division(4)

def carre(nbr):
    return nbr * nbr

carre(5) #Nothing happends
carre_de_5 = carre(5)
p(carre_de_5) #Now 25 appears so "print" != "return" (also "return" end the function proceedings)

ma_fonction_lambda = lambda nbr: nbr * 2
p(ma_fonction_lambda(3))
