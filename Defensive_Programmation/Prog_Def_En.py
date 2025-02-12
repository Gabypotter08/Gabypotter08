# Created by Gabypotter08, the 10/02/2025 in Python 3.7
# Coding utf-8

"""
Defensive programming and good practice in python

Exemples with : Verify if a list is sort, look for the max and min, everage calculation
"""

def sort_ok(liste:list, c:bool=True)->bool:
    #DOCSTRINGS
    """
    Give back True if the list is sort from least to most
    If c==False: Give back True if the list is sort from most to least
    The function can also check if a str is alphabetically sorted
    """
    if c: #Check if we verify from least to most
        for i in range(len(liste)-1):
            if liste[i+1]<liste[i]:
                return False
    else: #Check if we verify from most to least
        for i in range(len(liste)-1):
            if liste[i+1]>liste[i]:
                return False
    return True

def maximum(liste:list)->float:
    """
    Give back the biggest value
    """
    assert len(liste)>0, "list is empty"
    retour = liste[0]
    for i in range(len(liste)):
        try:
            liste[i] =float(liste[i]) 
        except:
            continue

        if liste[i] > retour:
                retour = liste[i]
    return retour

def minimum(liste:list)->float:
    """
    Give back the smallest value
    """
    assert len(liste)>0, "list is empty"
    retour = liste[0]
    for i in range(len(liste)):
        try:
            liste[i] =float(liste[i])
        except:
            continue 

        if liste[i] < retour:
                retour = liste[i]
    return retour

def peak(liste:list, m:bool=True)->float:
    """
    Give back le biggest or smallest value
    If m==True, give back the biggest, if m==False, give back the smallest
    """
    assert len(liste)>0, "list is empty"
    retour = liste[0]
    for i in range(len(liste)):
        try:
            liste[i] =float(liste[i]) 
        except:
            continue 

        if m: 
            if liste[i] > retour:
                    retour = liste[i]
        else: 
            if liste[i] < retour:
                    retour = liste[i]
    return retour



def mean(liste:list)->float:
    """
    Give back the mean of a list of value
    """
    assert len(liste)>0, "list is empty"
    total=0
    for i in range(len(liste)):
        try:
            liste[i] =float(liste[i]) 
        except: 
            continue 
        total+= liste[i]
    return total/len(liste)

def mean2(liste:list)->float:
    return sum(liste)/len(liste)

def mean_coef(liste:list)->float:
    """
    Give back the coefficient mean of a list
    Value of the list=mark, coef
    """
    assert len(liste)>0, "list is empty"
    total=0
    coef=0
    for i in range(len(liste)):
        try:
            liste[i][0] = float(liste[i][0]) 
            liste[i][1] = float(liste[i][1])
        except:
            continue
        total += liste[i][0] * liste[i][1]
        coef += liste[i][1]
    return total/coef



def peak2(liste:list, m:bool=True)->float:
    """
    Give back the peak value of a list
    if m==True, give back the max, if m==False, give back the min
    """
    assert len(liste)>0, "list is empty"
    retour = liste[0]
    for val in list:
        try:
            val = float(val) 
        except: 
            continue:
        if m: 
            if val > retour:
                    retour = val
        else: 
            if val < retour:
                    retour = val
    return retour

def mean3(liste:list)->float:
    """
    Give back the mean
    """
    assert len(liste)>0, "list is empty"
    total=0
    for note in liste:
        try:
            note=float(note)
        except:
            continue
        total+= note
    return total/len(liste)

def mean_coef2(liste:list)->float:
    """
    Give back the mean
    value of the list = mark, coef
    """
    assert len(liste)>0, "list is empty"
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


assert sort_ok([1,4,5,6,12,74]) == True
assert sort_ok([1,4,5,6,12,-4]) == False
assert sort_ok([1,4,5,6,12,74],c=False) == False
assert sort_ok([11,4,-5,-6,-12,-74],c=False) == True

assert maximum([1478, 2, 5, 4, 78, "-98", 511, 'er', 1478]) == 1478

assert minimum([1478, 2, 5, 4, 78, "-98", 511, 'er', -1478]) == -1478

assert peak([1478, 2, 5, 4, 78, "-98", 511, 'er', -1478]) == 1478
assert peak([1478, 2, 5, 4, 78, "-98", 511, 'er', -1478], m=False) == -1478

assert mean([1,2,3,5,8,45])==mean2([1,2,3,5,8,45])
assert mean_coef([[12,4],[10,1],[14,3]]) == 12.5
assert mean_coef([[12,4],['abs',5],[14,4]]) == mean_coef([[12,4],[14,4]])
assert mean_coef2([[12,4],['abs',5],[14,4]]) == mean_coef2([[12,4],[14,4]])
assert mean_coef2([[12,4],[10,1],[14,3]]) == 12.5
