def afficher_flottant(flottant):
    """Function taking as arg a float and which outputs
    numerals representing the truncation of this number. The floatting part
    must have a maximul length of 3 numerals.
    Moreover, we will replace the decimal point by the comma"""

    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    print(",".join([partie_entiere, partie_flottante[:3]]))
if __name__ == "__main__":
    afficher_flottant(1.555854781)
