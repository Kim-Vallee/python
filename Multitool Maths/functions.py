#!/usr/bin/python2.7
# coding: utf8

from datas import *

def get_chapter():
    """ Getting a chapter without errors"""
    try:
        chapter = input('Veuillez entrer le numéro du chapitre que vous voulez travailler / avoir les réponses : ')
        chapter = int(chapter)
        if chapter == '' or chapter == 0:
            raise ValueError
    except NameError:
        print('Veuillez entrer un numéro s\'il vous plait, pas une lettre ... \n')
        get_chapter()
    except ValueError:
        print('Veuillez entrer un numéro s\'il vous plait, pas rien du tout ... \n')
        get_chapter()
    else:
        return chapter

def check_chapter(chapter):
    """Function checking if the chapter correspond to what the one expect"""
    if chapter in dict_chapter.keys():
        question = "Est-ce bien le chapitre sur " + dict_chapter[chapter] + "? [Y/n] : "
        goon = str(raw_input(question))
        if goon.lower() == 'n':
            print('voici la liste des chapitres disponibles : ')
            print(dict_chapter.sort())
            check_chapter(get_chapter())
        elif goon.lower() != 'y' and goon.lower() != 'n':
            print('Veuillez répondre par y ou n (yes/no)')
            check_chapter(chapter)
