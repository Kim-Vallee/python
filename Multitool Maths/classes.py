#!/usr/bin/python2.7
# coding: utf8

class DictionnaireOrdonne():
    """Notre dictionnaire ordonné. L'ordre des données est maintenu
    et il peut donc, contrairement aux dictionnaires usuels, être trié
    ou voir l'ordre de ses données inversées"""
    def __init__(self, base={}, **donnees):
        """Constructeur de notre objet. Il peut ne prendre aucun paramètre
        (dans ce cas, le dictionnaire sera vide) ou construire un
        dictionnaire remplis grâce :
        -   au dictionnaire 'base' passé en premier paramètre ;
        -   aux valeurs que l'on retrouve dans 'donnees'."""
        self._cles = [] # Liste contenant nos clés
        self._valeurs = [] # Liste contenant les valeurs correspondant à nos clés
        # On vérifie que 'base' est un dictionnaire exploitable
        if type(base) not in (dict, DictionnaireOrdonne):
            raise TypeError( \
                "le type attendu est un dictionnaire (usuel ou ordonne)")
        # On récupère les données de 'base'
        for cle in base:
            self[cle] = base[cle]
        # On récupère les données de 'donnees'
        for cle in donnees:
            self[cle] = donnees[cle]
    def __repr__(self):
        """Représentation de notre objet. C'est cette chaîne qui sera affichée
        quand on saisit directement le dictionnaire dans l'interpréteur, ou en
        utilisant la fonction 'repr'"""
        chaine = "{"
        premier_passage = True
        for cle, valeur in self.items():
            if not premier_passage:
                chaine += ", " # On ajoute la virgule comme séparateur
            else:
                premier_passage = False
            chaine += repr(cle) + ": " + repr(valeur)
        chaine += "}"
        return chaine
    def __str__(self):
        """Fonction appelée quand on souhaite afficher le dictionnaire grâce
        à la fonction 'print' ou le convertir en chaîne grâce au constructeur
        'str'. On redirige sur __repr__"""
        return repr(self)
    def __len__(self):
        """Renvoie la taille du dictionnaire"""
        return len(self._cles)
    def __contains__(self, cle):
        """Renvoie True si la clé est dans la liste des clés, False sinon"""
        return cle in self._cles
    def __getitem__(self, cle):
        """Renvoie la valeur correspondant à la clé si elle existe, lève
        une exception KeyError sinon"""
        if cle not in self._cles:
            raise KeyError( \
                "La clé {0} ne se trouve pas dans le dictionnaire".format( \
                cle))
        else:
            indice = self._cles.index(cle)
            return self._valeurs[indice]
    def __setitem__(self, cle, valeur):
        """Méthode spéciale appelée quand on cherche à modifier une clé
        présente dans le dictionnaire. Si la clé n'est pas présente, on l'ajoute
        à la fin du dictionnaire"""
        if cle in self._cles:
            indice = self._cles.index(cle)
            self._valeurs[indice] = valeur
        else:
            self._cles.append(cle)
            self._valeurs.append(valeur)
    def __delitem__(self, cle):
        """Méthode appelée quand on souhaite supprimer une clé"""
        if cle not in self._cles:
            raise KeyError( \
                "La clé {0} ne se trouve pas dans le dictionnaire".format( \
                cle))
        else:
            indice = self._cles.index(cle)
            del self._cles[indice]
            del self._valeurs[indice]
    def __iter__(self):
        """Méthode de parcours de l'objet. On renvoie l'itérateur des clés"""
        return iter(self._cles)
    def __add__(self, autre_objet):
        """On renvoie un nouveau dictionnaire contenant les deux
        dictionnaires mis bout à bout (d'abord self puis autre_objet)"""
        if type(autre_objet) is not type(self):
            raise TypeError( \
                "Impossible de concaténer {0} et {1}".format( \
                type(self), type(autre_objet)))
        else:
            nouveau = DictionnaireOrdonne()
            # On commence par copier self dans le dictionnaire
            for cle, valeur in self.items():
                nouveau[cle] = valeur
            # On copie ensuite autre_objet
            for cle, valeur in autre_objet.items():
                nouveau[cle] = valeur
            return nouveau
    def items(self):
        """Renvoie un générateur contenant les couples (cle, valeur)"""
        for i, cle in enumerate(self._cles):
            valeur = self._valeurs[i]
            yield (cle, valeur)
    def keys(self):
        """Cette méthode renvoie la liste des clés"""
        return list(self._cles)
    def values(self):
        """Cette méthode renvoie la liste des valeurs"""
        return list(self._valeurs)
    def reverse(self):
        """Inversion du dictionnaire"""
        # On crée deux listes vides qui contiendront le nouvel ordre des clés
        # et valeurs
        cles = []
        valeurs = []
        for cle, valeur in self.items():
            # On ajoute les clés et valeurs au début de la liste
            cles.insert(0, cle)
            valeurs.insert(0, valeur)
        # On met ensuite à jour nos listes
        self._cles = cles
        self._valeurs = valeurs
    def sort(self):
        """Méthode permettant de trier le dictionnaire en fonction de ses clés"""
        # On trie les clés
        cles_triees = sorted(self._cles)
        # On crée une liste de valeurs, encore vide
        valeurs = []
        # On parcourt ensuite la liste des clés triées
        for cle in cles_triees:
            valeur = self[cle]
            valeurs.append(valeur)
        # Enfin, on met à jour notre liste de clés et de valeurs
        self._cles = cles_triees
        self._valeurs = valeurs
