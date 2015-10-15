#!/usr/bin/python3.4

import sys
sys.path.insert(0, "/home/etilawin/Documents/python/intro")
from modularites.print import *

a = "a,z,e,r,t,y,u,i,o,p,q,s,d,f,g,h,j,k,l,m,w,x,c,v,b,n"
b = a.split(',')
c = "".join(b)

for i, elmt in enumerate(b):
    p("à l'indice {} se trouve la lettre {}".format(i + 1, elmt))
p(a,b,c)
