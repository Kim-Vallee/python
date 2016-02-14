# coding: utf8
"""File where all the functions are stocked"""
def supprime_accent(texte):
    """ supprime les accents du texte source """
    texte = texte.lower()
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
    i = 0
    while i < len(accent):
        texte = texte.replace(accent[i], sans_accent[i])
        i += 1
        return texte
