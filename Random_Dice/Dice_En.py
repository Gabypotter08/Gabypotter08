# Created by Gabypotter08, the 10/02/2025 in Python 3.7
# Coding utf-8

from random import *

def dice(nbr_sides:int=6, nbr_throw:int = 1): 
    """
    function to simulate a dice
    """
    result=[] 
    for i in range(nbr_throw): 
        result.append(randint(1, nbr_sides)) 
    return result 

faces = input('How many faces do your dice have? ') 
face = int(faces) 
tour = input('How many throw do you want to do ')
tour = int(tour) 

print(dice(face, tour))
