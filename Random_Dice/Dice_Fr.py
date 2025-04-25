# Created by Gabypotter08, the 10/02/2025 in Python 3.7
# Coding utf-8

from random import *

def dice(nbr_side:int=6, nbr_throw:int = 1): 
    """
    fonction qui simule un lancé de dé
    """
    result=[] 
    for i in range(nbr_throw): 
        liste_result.append(randint(1, nbr_side)) 
    return result 

faces = input('Combien de faces à votre dé ? ') 
face = int(faces) 
tour = input('Combien de lancé voulez vous faire ? ')
tour = int(tour) 

print(dice(face, tour))
