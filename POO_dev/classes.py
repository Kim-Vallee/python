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

    def __repr__(self):
        """ What's in my object? """
        return('First Name = {} \n Last Name = {} \n Age = {} \n living = {}'.format(self.Fname,self.Lname,self.age,self.living))

    def __str__(self):
        """When ask to print it"""
        return('Avec __str__ : \n First Name = {} \n Last Name = {} \n Age = {} \n living = {}'.format(self.Fname,self.Lname,self.age,self.living))

    def __setattr__(self,attributeN,attributeV):
        """Method called when we change the value of an attribute"""
        object.__setattr__(self,attributeN,attributeV)

    def __getattr__(self,name):
        """Trying to access an unreal object"""
        print('My poor friend, this attribut \' {} \' does not exist'.format(name))
        answer = str(input('Do you want to create it?(Y/N) : '))
        if answer.upper() == 'Y':
            value = str(input('Please enter the attribute value : '))
            object.__setattr__(self,name,value)

    def __delattr__(self, attr):
        """What's happening when trying to del an attribute"""
        raise AttributeError('Nope, You are not allowed to do that!')

    def _get_living(self):
        """Called to read the living of someone"""
        print('Getting the living attribute')
        return self._living

    def _set_living(self, new_living):
        """Changes the actual living of someone"""
        print('Mr.{} is moving to {}.'.format(self.Lname, new_living))
        self._living = new_living

    living = property(_get_living,_set_living)

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

class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""


    objets_crees = 0 # Le compteur vaut 0 au départ
    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1
    def combien(cls):
        """Méthode de classe affichant combien d'objets ont été créés"""
        print("Jusqu'à présent, {} objets ont été créés.".format(
                cls.objets_crees))
    combien = classmethod(combien)

class ZDict:
    """Classe enveloppe d'un dictionnaire"""
    def __init__(self):
        """Notre classe n'accepte aucun paramètre"""
        self._dictionnaire = {}
    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""

        return self._dictionnaire[index]
    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""

        self._dictionnaire[index] = valeur

class ma_liste:
    """Trying smthing"""
    def __init__(self):
        """defining basics variables"""
        self.ma_list = [1,2,3,4,5]
    def __contains__(self,test):
        """Trying to see if its in """
        if test in self.ma_list:
            return True
        else:
            return False

class Time:
    """Showing the time you want"""
    def __init__(self,min=0,sec=0):
        """defining..."""
        self.min = min
        self.sec = sec
    def __str__(self):
        """printing time"""
        return('It\'s acctually {0:02}:{1:02}'.format(self.min,self.sec))
    def __repr__(self):
        """printing time"""
        return('It\'s acctually {0:02}:{1:02}'.format(self.min,self.sec))
    def __add__(self,newadd):
        """Adding time"""
        new_time = Time()

        new_time.sec = self.sec
        new_time.min = self.min

        new_time.sec += newadd

        if type(newadd) == int:
            new_time.min = new_time.sec // 60
            new_time.sec = new_time.sec % 60

        else:
            print('Veuillez entrer un nombre!')

        return new_time
