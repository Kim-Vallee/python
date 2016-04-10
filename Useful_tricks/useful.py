#!/usr/bin/python3.4
from math import *
p = print
MyList = [1,2,3,4,5]
MyList = list(map(exp,MyList)) # Map creates an iterator and apply the funtction to each value of a list
p(MyList)
