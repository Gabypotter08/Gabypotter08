# Created by Gabypotter08, the 10/02/2025 in Python 3.7
# Coding utf-8

"""
Programmation défensive et bonnes pratique en python

Exemples avec : vérifier une liste triée, cherche max/min, calcul moyenne
"""

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

def maximum(liste:list)->float:
    """
    Renvoie la valeur maxi d'une liste de valeurs numériques
    """
    assert len(liste)>0, "La liste est vide"
    retour = liste[0]
    for i in range(len(liste)):
        try:
            liste[i] =float(liste[i]) #essaie de convertir la valeur en float
        except:
            continue #si impossible, on passe à la valeur suivante dans la liste

        if liste[i] > retour:
                retour = liste[i]
    return retour

def minimum(liste:list)->float:
    """
    Renvoie la valeur mini d'une liste de valeurs numériques
    """
    assert len(liste)>0, "La liste est vide"
    retour = liste[0]
    for i in range(len(liste)):
        try:
            liste[i] =float(liste[i]) #essaie de convertir la valeur en float
        except:
            continue #si impossible, on passe à la valeur suivante dans la liste

        if liste[i] < retour:
                retour = liste[i]
    return retour

def extremum(liste:list, m:bool=True)->float:
    """
    Renvoie la valeur maxi ou mini d'une liste de valeurs numériques
    Si m==True, renvoie la maxi si m==False, renvoi le mini
    """
    assert len(liste)>0, "La liste est vide"
    retour = liste[0]
    for i in range(len(liste)):
        try:
            liste[i] =float(liste[i]) #essaie de convertir la valeur en float
        except:
            continue #si impossible, on passe à la valeur suivante dans la liste

        if m: #On cherche le maximum
            if liste[i] > retour:
                    retour = liste[i]
        else: #On cherche le minimum
            if liste[i] < retour:
                    retour = liste[i]
    return retour



def moyenne(liste:list)->float:
    """
    Renvoie la moyenne des valeurs d'une liste
    """
    assert len(liste)>0, "La liste est vide"
    total=0
    for i in range(len(liste)):
        try:
            liste[i] =float(liste[i]) #essaie de convertir la valeur en float
        except: #except généraliste
            continue #si impossible, on passe à la valeur suivante dans la liste
        total+= liste[i]
    return total/len(liste)

def moyenne2(liste:list)->float:
    return sum(liste)/len(liste)

def moyenne_coef(liste:list)->float:
    """
    Renvoie la moyenne coefficientée des valeurs de la liste
    valeur de la liste = paire note, coef
    """
    assert len(liste)>0, "La liste est vide"
    total=0
    coef=0
    for i in range(len(liste)):
        try:
            liste[i][0] = float(liste[i][0]) #essaie de convertir la valeur en float
            liste[i][1] = float(liste[i][1])
        except:
            continue
        total += liste[i][0] * liste[i][1]
        coef += liste[i][1]
    return total/coef


#façon alternative de gérer les boucles for spécifique à Python
def extremum2(liste:list, m:bool=True)->float:
    """
    Renvoie la valeur maxi ou mini d'une liste de valeurs numériques
    Si m==True, renvoie la maxi si m==False, renvoi le mini
    """
    assert len(liste)>0, "La liste est vide"
    retour = liste[0]
    for val in list:
        try:
            val = float(val) #essaie de convertir la valeur en float
        except: #except généraliste
            continue #si impossible, on passe à la valeur suivante dans la liste

        if m: #On cherche le maximum
            if val > retour:
                    retour = val
        else: #On cherche le minimum
            if val < retour:
                    retour = val
    return retour

def moyenne3(liste:list)->float:
    """
    Renvoie la moyenne des valeurs d'une liste
    """
    assert len(liste)>0, "La liste est vide"
    total=0
    for note in liste:
        try:
            note=float(note)
        except:
            continue
        total+= note
    return total/len(liste)

def moyenne_coef2(liste:list)->float:
    """
    Renvoie la moyenne coefficientée des valeurs de la liste
    valeur de la liste = paire note, coef
    """
    assert len(liste)>0, "La liste est vide"
    total=0
    coef=0
    for note,cf in liste:
        try:
            note= float(note)
            cf= float(cf)
        except:
            continue
        total += note*cf
        coef += cf
    return total/coef








assert tri_ok([1,4,5,6,12,74]) == True
assert tri_ok([1,4,5,6,12,-4]) == False
assert tri_ok([1,4,5,6,12,74],c=False) == False
assert tri_ok([11,4,-5,-6,-12,-74],c=False) == True

assert maximum([1478, 2, 5, 4, 78, "-98", 511, 'er', 1478]) == 1478
#Compare le résultat de nos fonctions avec celui des fonctions natives
assert maximum([1478, 2, 5, 4, 78, "-98", 511, 'er', -1478]) == max([1478, 2, 5, 4, 78, 511, 1478])

assert minimum([1478, 2, 5, 4, 78, "-98", 511, 'er', -1478]) == -1478
assert minimum([1478, 2, 5, 4, 78, "-98", 511, 'er', -1478]) == min([1478, 2, 5, 4, 78, 511, -1478])

assert extremum([1478, 2, 5, 4, 78, "-98", 511, 'er', -1478]) == 1478
assert extremum([1478, 2, 5, 4, 78, "-98", 511, 'er', -1478], m=False) == -1478

assert moyenne([1,2,3,5,8,45])==mean([1,2,3,5,8,45])
assert moyenne([1,2,3,5,8,45])==moyenne2([1,2,3,5,8,45])
assert moyenne_coef([[12,4],[10,1],[14,3]]) == 12.5
assert moyenne_coef([[12,4],['abs',5],[14,4]]) == moyenne_coef([[12,4],[14,4]])
assert moyenne_coef2([[12,4],['abs',5],[14,4]]) == moyenne_coef2([[12,4],[14,4]])
assert moyenne_coef2([[12,4],[10,1],[14,3]]) == 12.5
