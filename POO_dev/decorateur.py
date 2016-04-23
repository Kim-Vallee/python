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
            Executing_time = round(time_after - time_before, 0)
            if Executing_time >= secs:
                print("la fonction à pris {} seconde(s) pour s'executer".format(\
                Executing_time))
            return returned_value
        return modificated_function
    return decorator

def check_arguments(*a_args, **a_kwargs):

    def decorateur2(function):

        def modif(*args, **kwargs):
            if len(a_args) != len(args):
                print("nombre d'arguments donnés invalide")
                raise OverflowError('Weird number of args')
            return function(*args, **kwargs)
        return modif
    return decorateur2


@check_arguments(int, int)
def intervalle(inf,sup):
    print('l\'intervalle est de {}'.format(sup-inf))

intervalle(5, 8, 3)
