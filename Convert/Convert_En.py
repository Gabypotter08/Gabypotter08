# Created by Gabypotter08 in Python 3.7
# Coding utf-8

def celsius(valeur_fahrenheit) -> float:
    """
    Convert fahrenheit in celsius
    """
    valeur_celsius=(valeur_fahrenheit-32)*5/9
    return valeur_celsius

def fahrenheit(valeur_celsius)->float:
    """
    convert celsius en fahrenheit
    """
    valeur_fahrenheit=(valeur_celsius* 9/5) + 32 
    return valeur_fahrenheit

def miles(valeur_km)-> float:
    """
    convert kilometres in miles
    """
    valeur_miles=valeur_km/1,609
    return valeur_miles

def km(valeur_miles)-> float:
    """
    convert miles en kilometres
    """
    valeur_km=valeur_miles*1,609
