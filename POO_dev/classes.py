#!/usr/bin/python3.4
#encoding : utf-8
class People:
    """ This class define a person by:
        - His first name
        - His last name
        - His age
        - His living """
    def __init__(self,Fname,Lname,age,living):
        """ Class constructor, each attribute will have
        a defined value """
        self.Fname = Fname
        self.Lname = Lname
        self.age = age
        self.living = living
class BlackBoard:
    """This is my personnal BlackBoard
    where I can write and erase everything on
    a 'surface' """
    def __init__(self):
        """ Our surface is basically empty """
        self.surface = ""
    def ecrire(self, writing):
        """ Writes a message """
        if self.surface != "":
            self.surface += "\n"
        self.surface += writing
    def read(self):
        """Print"""
        print(self.surface)
    def clean(self):
        """cleaning"""
        self.surface = ""
