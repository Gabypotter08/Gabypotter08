# Created by Gabypotter08, the 10/02/2025 in Python 3.7
# Coding utf-8

def celsius(valeur_fahrenheit:int=0) -> float:
    """
    convertir fahrenheit en celsius
    """
    valeur_celsius=(valeur_fahrenheit-32)*5/9
    return valeur_celsius

def fahrenheit(valeur_celsius:int=0)->float:
    """
    convertir celsius en fahrenheit
    """
    valeur_fahrenheit=(valeur_celsius* 9/5) + 32 
    return valeur_fahrenheit


def miles(valeur_km:int=0)-> float:
    """
    convertir kilomètres en miles
    """
    valeur_miles=valeur_km/1,609
    return valeur_miles

def km(valeur_miles:int=0)-> float:
    """
    convertir miles en kilomètres
    """
    valeur_km=valeur_miles*1,609
    return valeur_km


def livre(val_kg:int=0)-> float:
    """
    convertir kilogrammes en livres
    """
    val_livres=val_kg/2,205
    return val_livres
    
def kg(val_livres:int=0)-> float:
    """
    convertir livres en kilogrammes
    """
    val_kg=val_livres*2,205
    return val_kg
