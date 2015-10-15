#!/usr/bin/python3.4

from 'intro a python'.modularites.print import *

a = "a,z,e,r,t,y,u,i,o,p,q,s,d,f,g,h,j,k,l,m,w,x,c,v,b,n"
b = a.split(',')
c = "".join(b)

for i, elmt in enumerate(b):
    print("à l'indice {} se trouve la lettre {}".format(i + 1, elmt))
p(a,b,c)
