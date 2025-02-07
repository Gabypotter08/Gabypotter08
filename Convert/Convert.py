# Created by Gabypotter08 in Python 3.7
# Coding utf-8

def celsius(valeur_fahrenheit) -> float:
    """
    convertir fahrenheit en celsius
    """
    valeur_celsius=(valeur_fahrenheit-32)*5/9
    return valeur_celsius

def fahrenheit(valeur_celsius)->float:
    """
    convertir celsius en fahrenheit
    """
    valeur_fahrenheit=(valeur_celsius* 9/5) + 32 
    return valeur_fahrenheit

def miles(valeur_km)-> float:
    """
    convertir kilomètres en miles
    """
    valeur_miles=valeur_km/1,609
    return valeur_miles

def km(valeur_miles)-> float:
    """
    convertir miles en kilomètres
    """
    valeur_km=valeur_miles*1,609
