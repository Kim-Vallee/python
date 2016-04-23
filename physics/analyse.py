#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from math import sqrt,exp,pi,sin
import matplotlib.pyplot as plt
from numpy import linspace

def f(x):
    return x**2

def Fu(t,z):
    return -3 * z

def F(t,x,y):
    return y

def G(t,x,y):
    return sin(x)

def expmap(x):
    return exp(x)

def integral(function,a,b,n): # Méthode des rectangles
    """This function calculate an integral of a function and return the result
    as an int with rectangles"""
    z = 0
    h = (b-a)/float(n)
    for i in range(n):
        z += function(a+i*h)
    return z*h

def trapintegral(function,a,b,n): # Méthode des trapèze
    """ Variante de la précédente avec des trapèzes"""
    h = (b-a)/float(n)
    xi = 0.5*(function(a)+function(b))
    for i in range(1,n):
        xi =xi + function(a+i*h)
    return xi*h

def Simpsonintegral(function,a,b,n):
    h = (b-a)/float(n)
    z = (function(a) + function(b))/6
    for i in range(1,n):
        z += function(a+i*h)/3
    for i in range(n):
        z += function(a+(2*i+1)*h/2)*2/3
    return h*z

def derivative(f,h=1e-8):
    h1 = h/2
    def g(x):
        return ( f(x+h1) - f(x-h1) ) / h
    return g

def Newton(x,n): # Résolution approchée de f(x) = 0
    a = float(x)
    g = derivative(f)
    for i in range(n):
        a=a - (f(a)/g(a))
    return a

def Euler(F,t0,tf,y0,n):
    """Resoudre une équation diff par la méthode d'Euler"""
    t = t0
    y = y0
    h = (tf-t0)/float(n)
    temps = [t0]
    fonction = [y0]
    for i in range(n):
        y = y+h*F(t,y)
        t = t+h
        temps.append(t)
        fonction.append(y)
    plt.plot(temps,fonction,'b')
    return fonction

def Euler2(F,G,t0,tf,x0,y0,n):
    """ Résoudre un couple d'equa diff"""
    t = t0
    x = x0
    y = y0
    h = (tf-t0)/float(n)
    temps = [t0]
    lapins = [x0]
    renards = [y0]
    for i in range(n):
        x,y = x + h*F(t,x,y) , y + h*G(t,x,y) # On attribut les 2 en même temps
                                              # pour montrer la simultanéité
        t += h
        temps.append(t)
        lapins.append(x)
        renards.append(y)
    # plt.plot(temps,lapins,'b-')
    # plt.plot(temps,renards,'r--')
    plt.plot(lapins,renards,'g')
    return lapins,renards

Euler2(F, G, 0, 20, 3*pi/4, 0, 10000)
plt.show()


# print(integral(f, 0, 1, 100)) #more efficient for affine functions
# print(trapintegral(f, 0, 1, 100))
# print(Simpsonintegral(f, 0, 1, 100)) # Most efficient for curved function
