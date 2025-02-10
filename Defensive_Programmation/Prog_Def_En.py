# Created by Gabypotter08, the 10/02/2025 in Python 3.7
# Coding utf-8

"""
Defensive programming and good practice in python

Exemples with : Verify if a list is sort, look for the max and min, everage calculation
"""


"""
#exemple using assert 
def my_function(a: str='a', b: str='b', c: int=3, d:bool=False)->str:
    assert type(a)==str and type(b)==str, "Need a str" #Assert, follow by an logic expression evaluated to True follow by an error message if evaluated to False
    assert type(c)==int, "Need an int"
    assert type(d)==bool, "Need a bool"
    if d== True:
        resultat=a+b
    else:
        resultat=a*c
    return resultat
"""

#Sort from least to most

"""
def tri_ok(liste:list)->bool:
    #""
    Give back True if the list is sort
    #""
    for i in range(len(liste)-1):
        if liste[i+1]<liste[i]:
            return False
    return True

assert tri_ok([1,4,5,6,12,74]) == True
assert tri_ok([1,4,5,6,12,-4]) == False
"""

#Sort

def tri_ok(liste:list, c:bool=True)->bool:
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

assert tri_ok([1,4,5,6,12,74]) == True
assert tri_ok([1,4,5,6,12,-4]) == False
assert tri_ok([1,4,5,6,12,74],c=False) == False
assert tri_ok([11,4,-5,-6,-12,-74],c=False) == True
