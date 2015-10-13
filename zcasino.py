#!/usr/bin/python3.4
import math
import random
#espace défini aux variables de base
argent = 1000
continuer_partie = True
#fin de l'espace défini aux variables
#----------------------------------------------------------------------
while continuer_partie:
    print("vous avez",argent,"€") #On dit à l'utilisateur son argent
    #
    #________________________________________________________________
    #
    nombre_mise = -1 #On définit une mise négative pour entretenir la boucle si il y a une erreur

    #
    #Début de la boucle -------------------------------------------------------------------------
    #

    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("veuillez mettre le nombre sur lequel vous voulez parier compris entre 0 et 49 : ")
        try: #On essaye de convertir le nombre en chiffre et on vérifie qu'il soit compris entre 0 et 49...
            nombre_mise = int(nombre_mise)
            if nombre_mise < 0:
                raise ValueError()
            elif nombre_mise > 49:
                raise ValueError()
        except ValueError: #... sinon on fais recommencer la boucle
            print("vous n'avez pas saisi de nombre")
            nombre_mise = -1
            continue #Le continue permet de passer le reste de la boucle
        else: #On met la suite du code comme tout se passe bien
            if nombre_mise % 2 == 0: #on attribut les couleurs en fonction si le nombre est paire ou non
                couleur_mise = "rouge"
            else:
                couleur_mise = "noir"

    #
    #Fin de la boucle -------------------------------------------------------------------------
    #

    print('la couleur du nombre de votre mise est : ',couleur_mise) #Rappel de la couleur à l'utilisateur
    somme_mise = -1 #On définit une mise négative pour entretenir la boucle si il y a une erreur

    #
    #Début de la boucle -------------------------------------------------------------------------
    #

    while somme_mise < 0 or somme_mise > argent:
        somme_mise = input("veuillez parier la somme que vous voulez jouer : ")
        try:
            somme_mise = int(somme_mise)
            if somme_mise <= 0 or somme_mise > argent:
                raise ValueError()
        except ValueError:
            print("Veuillez miser correctement ! ")
            somme_mise = -1
            continue

    #
    #Fin de la boucle -------------------------------------------------------------------------
    #

    print("Pour le moment vous avez parié sur le numéro : ",nombre_mise," et vous avez misé : ",somme_mise)
    argent -= somme_mise #On retire la somme de la mise de l'argent de l'utilisateur

    print("La roulette tourne ...")

    nombre = random.randrange(49) #On définit le nombre aléatoirement

    #
    # Début if ... elif ... else -------------------------------------------------------------------------
    #

    if nombre % 2 == 0:
        couleur_nombre = "rouge"
    else:
        couleur_nombre = "noir"

    #
    # Fin if ... elif ... else -------------------------------------------------------------------------
    #

    print("vous êtes tomber sur le ",nombre," qui est ",couleur_nombre) # On dit à l'utilisateur qu'il est tombé sur tel nombre

    #
    # Début if ... elif ... else -------------------------------------------------------------------------
    #

    if nombre_mise == nombre: #si le nombre est le même on triple la mise
        print("bravo vous avez multiplié vos gains par 3!")
        somme_mise *= 3
        argent += somme_mise

    elif couleur_mise == couleur_nombre and nombre != nombre_mise: #Si il est de même couleur on la divise par deux
        print("Le nombre que vous avez choisi à la bonne couleur, vous gardez 50% de votre mise")
        somme_mise = math.ceil(somme_mise/2)
        argent += somme_mise

    else: #Si tout ce qui est précédent est faux, l'utilisateur perd la mise
        print("vous avez perdu sur toute la ligne")

    #
    # Fin if ... elif ... else -------------------------------------------------------------------------
    #

    if argent <= 0: #On vérifit que l'utilisateur à toujours de l'argent sinon on arrête là
        continuer_partie = False
        print("vous n'avez plus d'argent bye bye!")

    else:
        print("vous avez désormais",argent,"€")
        recommencer = 0

        while recommencer < 1 or recommencer > 2:
            recommencer = input("voulez-vous recommencer? 1 pour oui 2 pour non : ")

            try: #On vérifie ce que l'utilisateur à entré
                recommencer = int(recommencer)
                if recommencer < 1 or recommencer > 2:
                    raise ValueError()

            except ValueError: #Si il y  a une erreur on lui demande de ressaisir le chiffre
                print("veuillez entrer 1 ou 2")
                recommencer = 0
                continue

            else: #suite du code de try
                if recommencer == 1: #Si 1 on relance
                    print("c'est reparti pour un tour!\n")
                    continuer_partie = True

                else: #Si 2 on abandonne
                    print("bon ok...")
                    continuer_partie = False
