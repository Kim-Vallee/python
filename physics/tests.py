#!/usr/bin/python3.4
import math

# Functions

def degrees_to_radian(number):
    """Change a number in degrees to radians"""
    number = number*math.pi/180
    return float(number)

# Constant

g = 9.81
G = 6.67e-11
M = 5.97e24
R = 6371e3
c = 299792458
ly = 9.4607e15 # Light year in meters
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

# Exercice 5 : How long with a speed and distance (light relativity)
v = float(input("Please enter the percentage of speed of light you wanna try : "))
v = v * c
x = int(input("How far is the point you wanna reach in light years : "))
t = x*c/v
print('It takes {} years for a passenger to reach the point'.format(t))
print('It takes twice for someone on earth')
