#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def f(x):
    return 2*x + 5

def integral(limitsAndFunction):
    """This function calculate an integral of a function and return the result
    as an int"""
    if not isinstance(limitsAndFunction, list):
        raise TypeError('The parameter must be a list')
    elif len(limitsAndFunction) != 2:
        raise TypeError('The list must contain 2 objects')
    a = limitsAndFunction[0]
    b = limitsAndFunction[1]
    marches = 100 * 10**(b-a)
    xi = 0
    h = (b-a)/marches
    result = 0
    for i in range(0,marches-1):
        xi = a + i*h
        result += f(xi)
    result *= h
    return result

def derivative(f,h=1e-8,n=1):
    h1 = h/2
    i = 1
    def g(x):
        return ( f(x+h1) - f(x-h1) ) / h
    return g

limits = [2,3]
print(integral(limits))

g = derivative(f)
print(g(1))
