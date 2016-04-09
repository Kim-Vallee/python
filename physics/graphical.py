#!/usr/bin/python2.7
#encoding : utf-8
# from visual import sphere
from pylab import *
from numpy import *
from math import sin as sinem
from math import sqrt,pi
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

# x = linspace(0,10,100)
# y1 = sin(x)
# y2 = cos(x)
# plot(x,y1,"k-")
# plot(x,y2,"k--")
# xlabel("x axis")
# ylabel("sin(x) and cos(x)")
# ylim(-1.1,1.1)
# show()

# theta = linspace(0,2*pi,100) # First theta takes a 100 values between 0 and 2pi
# x = 2*cos(theta) + cos(2*theta) # Then x and y are defined with sin cos and theta(remember it's an array)
# y = 2*sin(theta) - sin(2*theta)
# plot(x,y) # We plot this and get a curved triangle (deltoid curve)
# show()

# theta = linspace(0,10*pi,1000) # Taking 1000 cause it's nicer
# r = theta**2 # R is another range of value of theta, or in another words r = f(theta) where f(theta) = theta**2
# x = r*cos(theta) # Then we convert them in Cartesian coordinaates
# y = r*sin(theta)
# plot(x,y)
# show()

# theta = linspace(0,24*pi,10000)
# r = exp(cos(theta)) - 2*(cos(4*theta)) + sin(theta/12)**5 #
# x = r*cos(theta)                                          #  Fey's function
# y = r*sin(theta)                                          #
# plot(x,y)
# show()

# Wave interference
wavelength = 5.0
k = 2*pi/wavelength
xi0 = 1
separation = float(input('Please enter the separation between two rocks (1-50) : ')) # Separation of both centers in centimeters
side = 200.0 # Sides of the square in cm
points = 600 # Amount of points
spacing = side / points # Spacing of points in cm

# Calculate the positions of the centers of the circles
x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2

# Make an array to store the heights
xi = empty([points,points],float)

# Calculate the values in the array
for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j
        r1 = sqrt((x-x1)**2 +(y-y1)**2)
        r2 = sqrt((x-x2)**2 +(y-y2)**2)
        xi[i,j] = xi0*sin(k*r1) + xi0*sin(k*r2)

# Make the plot
imshow(xi,origin="lower",extent=[0,side,0,side])
gray()
show()
