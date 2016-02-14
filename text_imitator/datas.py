#!/usr/bin/python3.4
# coding: utf8
"""File where all the datas are stocked"""
import string
import sys
import random

indices = list()
liste_text = list()
alphabet = string.ascii_lowercase + string.punctuation + string.whitespace
alphabet = alphabet.replace('"','')
alphabet = alphabet.replace('.','')
alphabet = alphabet.replace('\n','')
alphabet = list(alphabet)
pourcentage_lettre = list()
new_text = str()
chance_after_letter = dict()
temp_list = list()
temp_list_chance = list()
temp_last = 0
createdtxt = str()
temp_rand = int()
splitted_txt = str()
