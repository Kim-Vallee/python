#!/usr/bin/python3.4
# coding: utf8
"""File where all the datas are stocked"""
import string

indices = list()
alphabet = list(string.ascii_lowercase + string.punctuation + string.whitespace)
alphabet = [x for x in alphabet if x != '"']
pourcentage_lettre = list()
new_text = str()
chance_after_letter = dict()
temp_list = list()
temp_list_chance = list()
temp_last = 0
createdtxt = str()
temp_rand = int()
