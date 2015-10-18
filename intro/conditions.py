#!/usr/bin/python3.4

def p(*args):
    print(*args)
a = 5
b = 6
if a > b:
    p("en effet a vaut {} et b vaut {}".format(a, b))
elif a < b:
    p("en effet a vaut {} et b vaut {}".format(a, b))
else:
    p("en effet a vaut {} et b vaut {} donc ils sont égaux".format(a, b))

booleen = True
if booleen is not True:
    p("La variable n'est pas vraie")
elif booleen is True:
    p('la variable est vraie')
else:
    p("la variable n'est pas booleen")


# Programm which tests if a year is leap or not

year = input("Saisissez une année : ")
try:
    year = int(year)
except:
    p('On a demandé un nombre!')
else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")
