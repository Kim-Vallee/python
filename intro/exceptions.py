#!/usr/bin/python3.4

import sys
sys.path.insert(0, "/home/etilawin/Documents/python/intro")
from modularites.print import *

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    #assert 6 < 4
except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
    pass
except ValueError:
    print("Could not convert data to an integer.")
    pass
#except AssertionError:
    #print("Not true so assertion error")
except:
    print ("Unexpected error:", sys.exc_info()[0])
    raise
    pass

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))     # the exception instance
    print(inst.args)      # arguments stored in .args
    print(inst)           # __str__ allows args to be printed directly
    x, y = inst.args
    print('x =', x)
    print('y =', y)
    pass

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
