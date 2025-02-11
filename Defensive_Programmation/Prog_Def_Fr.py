# Created by Gabypotter08, the 10/02/2025 in Python 3.7
# Coding utf-8

"""
Programmation défensive et bonnes pratique en python

Exemples avec : vérifier une liste triée, cherche max/min, calcul moyenne
"""


"""
#exemple utilisation assertions et mise en page d'une fonction
def ma_fonction(a: str='a', b: str='b', c: int=3, d:bool=False)->str:
    assert type(a)==str and type(b)==str, "Il faut passer un str" #Assertion, suivi d'une expression logique évaluer à True suivi d'un msg d'erreur si évaluée à False
    assert type(c)==int, "Il faut passer un int"
    assert type(d)==bool, "Il faut passer un booléen"
    if d== True:
        resultat=a+b
    else:
        resultat=a*c
    return resultat
"""

#Croissant

"""
def tri_ok(liste:list)->bool:
    #""
    Renvoie True si la liste est triée par ordre croissant
    #""
    for i in range(len(liste)-1):
        if liste[i+1]<liste[i]:
            return False
    return True

assert tri_ok([1,4,5,6,12,74]) == True
assert tri_ok([1,4,5,6,12,-4]) == False
"""

#Croissant ou décroissant

def tri_ok(liste:list, c:bool=True)->bool:
    #DOCSTRINGS
    """
    Renvoie True si la liste est triée par ordre croissant
    Si c==False: renvoie True si la liste est triée par ordre décroissant
    La fonction peut aussi vérifier si un str est par ordre alphabétique
    """
    if c: #On vérifie l'ordre croissant
        for i in range(len(liste)-1):
            if liste[i+1]<liste[i]:
                return False
    else: #On vérifie l'ordre décroissant
        for i in range(len(liste)-1):
            if liste[i+1]>liste[i]:
                return False
    return True

assert tri_ok([1,4,5,6,12,74]) == True
assert tri_ok([1,4,5,6,12,-4]) == False
assert tri_ok([1,4,5,6,12,74],c=False) == False
assert tri_ok([11,4,-5,-6,-12,-74],c=False) == True


def max_min(liste:list, a:bool=True)->float:
    """
    revoie le maximum ou le minimum d'une liste
    Si a==True, revoie le maximum
    Si a==False, renvoie le minimum
    """
    max_min=liste[0]
    if a:
        for i in range(len(liste)):
            if max_min > liste[i]:
                assert max_min>liste[i]
            else:
                max_min=liste[i]
    else:
        for i in range(len(liste)):
            if max_min < liste[i]:
                assert max_min<liste[i]
            else:
                max_min=liste[i]
    return max_min

def moyenne(liste:list):
    """
    Donne la moyenne d'une liste
    """
    nbr_notes=len(liste)
    somme_notes=0
    for i in range(len(liste)):
        somme_notes+=liste[i]
    moyenne=somme_notes/nbr_notes
    return moyenne
