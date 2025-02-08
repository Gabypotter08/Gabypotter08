# Created by Gabypotter08 in Python 3.7
# Coding utf-8

from random import *

def dice(nbr_faces:int=6, nbr_lance:int = 1): 
    """
    fonction qui simule un lancé de dé
    """
    liste_result=[] 
    for i in range(nbr_lance): 
        liste_result.append(randint(1, nbr_faces)) 
    return liste_result 

faces = input('Combien de faces à votre dé ? ') 
face = int(faces) 
tour = input('Combien de lancé voulez vous faire ? ')
tour = int(tour) 

print(dice(face, tour))
