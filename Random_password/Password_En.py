# Created by Gabypotter08, the 10/02/2025in Python 3.7
# Coding utf-8

from random import *

def mot_de_passe(nbr_tour:int=1)->str:
    """
    Give a random password
    """
    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQWXYZ0123456789?,.;/:§!%ù¨^£$µ*+=°)àç_è-("é&)'
    mdp=''
    for i in range(nbr_tour):
        for i in range(randint(0,3)):
            mdp=mdp+alphabet[randint(0,92)]
    return mdp

a=input("How many lap of the function do you want?")
a=int(a)

print(mot_de_passe(a))
