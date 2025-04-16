# Created by Gabypotter08, the 10/02/2025 in Python 3.7
# Coding utf-8

def celsius(val_fahrenheit:int=0) -> float:
    """
    Convert fahrenheit in celsius
    """
    val_celsius=(val_fahrenheit-32)*5/9
    return val_celsius

def fahrenheit(val_celsius:int=0)->float:
    """
    convert celsius to fahrenheit
    """
    val_fahrenheit=(val_celsius* 9/5) + 32 
    return val_fahrenheit


def miles(val_km:int=0)-> float:
    """
    convert kilometres to miles
    """
    val_miles=val_km/1,609
    return val_miles

def km(val_miles:int=0)-> float:
    """
    convert miles to kilometres
    """
    val_km=val_miles*1,609
    return val_km


def pound(val_kg:int=0)-> float:
    """
    convert kilograms to pound
    """
    val_pound=val_kg/2,205
    return val_pound
    
def kg(val_pound:int=0)-> float:
    """
    convert pound to kilograms
    """
    val_kg=val_pound*2,205
    return val_kg
