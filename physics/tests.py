#!/usr/bin/python2.7
import math
import numpy
# import numpy

# Functions

def degrees_to_radian(number):
    """Change a number in degrees to radians"""
    number = number*math.pi/180
    return float(number)
def four(n):
    """multiply by four a number"""
    n = n*4
    return n

# Constant

g = 9.81 # Acceleration due to gravity
G = 6.6738e-11 # Newton's gravitational constant in m^3*kg^-1*s^-2
R = 6371e3 # Radius of earth in meters
c = 299792458 # speed of light
ly = 9.4607e15 # Light year in meters
h_j = 6.62606957e-34 # In jouls/second
h_v = 4.1343359e-15 # in eV/seond
hb = h_v/2*math.pi

# # Exercice 1 : Where is the object?
#
# h = int(input('Please enter the height of the tour (in meters) : '))
# t = int(input('Please enter the time (in seconds): '))
# s = (g*t**2)/2
#
# print('The ball is actually {} meters height'.format(h-s))
#
# # Exercice 2 : How long before the object falls?
# h = int(input('Please enter the height of the tour (in meters) : '))
# t = math.sqrt(h/g*2)
#
# print('The ball will touch the ground in {} s'.format(t))

# # Exercice 3 : Amount of time for a satellite to go around earth
# M = 5.97e24 # Mass of earth in kg
# T = int(input('please enter the time for the object to make a whole orbit in seconds : '))
# h = ((G*M*T**2)/(4*math.pi**2))**(1/3) - R
# print('The altitude will be {} meters'.format(h))

# # Exercice 4 : Converting polar coordinates
# r = int(input('Please enter the radius : '))
# theta = int(input('Please enter the angle : '))
# # Converting to cartesians
# x = r*math.cos(degrees_to_radian(theta))
# y = r*math.sin(degrees_to_radian(theta))
# print('The cartesian coordinates of the point are x : {}, y : {}'.format(x,y))

# # Exercice 5 : How long with a speed and distance (light relativity)
# v = float(input("Please enter the percentage of speed of light you wanna try : "))
# v = v * c
# x = float(input("How far is the point you wanna reach in light years : "))
# t = x*c/v
# print('It takes {} years for a passenger to reach the point'.format(t))
# print('It takes twice for someone on earth')

# # Exercie 2.5 : Quantum potential step
# m = 9.11e-31
# E = 10
# V = 9
# k1 = math.sqrt(2*m*E)/hb
# k2 = math.sqrt(2*m*(E-V))/hb
# T = 4*k1*k2/(k1+k2)**2
# R = ((k1-k2)/(k1+k2))**2
# print("Probability of reflection : {}%, Probability of transmission : {}%".format(R,T))

# # Exercice 2.6 : Planetary orbits -> unsolved
# M = 1.9891e30 # Mass of the sun in kg
# l1 = float(input('Please enter the distance to the sun at perihelion : '))
# v1 = float(input('please enter it\'s velocity at perihelion : '))
# a = 1
# b = -(2*G*M/(v1*l1))
# c = -(v1**2+2*G*M/l1)
# delta = b**2 - 4*a*c # Using determinant from 2nd degree equations
# v2 = (-b + math.sqrt(delta))/(2*a) # v2 values the smallest sqaureroot result
# l2 = l1*v1/v2 # As we know l1*v1 = l2*v2
# a = 0.5*(l1+l2)  # Kepler's law derived give this
# b = math.sqrt(l1 * l2)
# T = 2*math.pi*a*b/(l1*v1) # Orbital period
# e = (l2-l1)/(l2+l1)
# print('The velocity at aphelion is {} m/s and the distance is {} m. \
# It\'s orbital period is equal to {} years and it\'s orbital eccentricity\
#  is equal to {} m'.format(v2,l2,T/(60**2*24*365),e))

# # Exercise 2.7 : Catalan numbers
# C = 1
# i = 0
# while C <= 1000000000:
#     C = ((4*i+2)/(i+2))*C
#     i+=1
#     print(C)

# # Getting the length of a vector...
# r = [0,0,0]
# r[0] = float(input('PLease enter the x coordinate : '))
# r[1] = float(input('PLease enter the y coordinate : '))
# r[2] = float(input('PLease enter the z coordinate : '))
# length = math.sqrt(r[0]**2 + r[1]**2 + r[2]**2)
# mean = sum(r)/len(r) # Mean means "moyenne" sum() adds everything in a list
# print('The vector has {} length'.format(length))
# p('The mean of the list r is equal to {}'.format(mean))

# # Arrays :
# a = numpy.zeros(3,float)
# print(a)
# a = numpy.zeros([4,3],float) # Creating kind of a matrice full of zeros
# print(a)
# a = numpy.zeros(100,complex) # Adding a hundred complex numbers 0
# print(a)
# a = numpy.empty(4,float) # Adding random numbers
# print(a)

r = [1,2,3]
r2 = list(map(four,r))
MyArray = numpy.array([r,r2], float)
print(MyArray)
MyArray[0,0] = 2
print(MyArray)

MyArray = numpy.loadtxt("arrays.txt",float)
print(MyArray)

MyArray2 = MyArray * 2 # Multiply the whole array
MyArray2[0] /= 2 # Divide the line i MyArray[i] (lines start at 0)
MyArray2[2] *= 10 # Multiply by a hundred the number i of the j line MyArray[j,i] (both starts at zero)
# print(MyArray)
a = numpy.array([1,2,3,4],float)
b = numpy.copy(a)*2
print(a)
print(b)
# print(b/a+1)
# print(b/(a+1))
# print(1/a)
print(numpy.dot(a,b))

# # Getting the "geometric mean" (wtf is this???)
# values = numpy.loadtxt("arrays.txt",float)
# logs = numpy.array(map(math.log,values),float)
# geometric = math.exp(sum(logs)/len(logs))
# print(geometric)
