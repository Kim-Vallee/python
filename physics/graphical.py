#!/usr/bin/python2.7
from pylab import *
from numpy import *
from math import sin as sinem
from random import *
# i = 0
# listx = list()
# listy = list()
# while i < 1000:
#     listx.append(i)
#     listy.append(randrange(100))
#     i += 1
# x = listx
# y = listy
# plot(x,y)
# show()


# x = linspace(0, 10, 100)
# y = sin(x)
# plot(x,y)
# show()

# xpoints = list()
# ypoints = list()
# for x in linspace(0, 10, 100): # Same thing then before but this time we do it point by point
#     xpoints.append(x)
#     ypoints.append(sinem(x))
#
# plot(xpoints,ypoints,"ko") # Will produce a graph with dots k = black = color    o = dots = style
# ylim(-1.1,1.1) # Changes the limits of y axis on the graph
# xlabel("x axis")
# ylabel("sin(x)")
# show()

x = linspace(0,10,100)
y1 = sin(x)
y2 = cos(x)
plot(x,y1,"k-")
plot(x,y2,"k--")
xlabel("x axis")
ylabel("sin(x) and cos(x)")
ylim(-1.1,1.1)
show()
