# Created by Gabypotter08 in Python 3.7
# Coding utf-8

from random import *

def dice(nbr_faces:int=6, nbr_lance:int = 1): 
    """
    function to simulate a dice
    """
    liste_result=[] 
    for i in range(nbr_lance): 
        liste_result.append(randint(1, nbr_faces)) 
    return liste_result 

faces = input('How many faces do your dice have? ') 
face = int(faces) 
tour = input('How many throw do you want to do ')
tour = int(tour) 

print(dice(face, tour))
