#!/usr/bin/python3.4
#encoding : utf-8
from time import *

def NotWorkingAnymore(function):
    """ Saying a function is now useless """
    def Old_Function():
        """ Modificating an old function """
        raise RuntimeError('The function you tried to use is useless now')
    return Old_Function

# @NotWorkingAnymore
def hey():
    """ Saying hi """
    print('hi')

def controller_Time(secs):
    """Controlling time needed for a function to activate"""
    def decorator(function_to_execute):
        """Defining decorator """

        def modificated_function():
            """ Function returned by decorator """
            time_before = time() # Avant d'executer la fonction
            returned_value = function_to_execute() #On execute la fonction
            time_after = time()
            Executing_time = time_after - time_before
            if Executing_time >= secs:
                print("la fonction à pris {} pour s'executer".format(\
                Executing_time))
            return returned_value
        return modificated_function
    return decorator

@controller_Time(0)
def fast():
    i = 0
    while i < 1000:
        print('working')
        i+=1
