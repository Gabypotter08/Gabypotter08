# Created by Gabypotter08 in Python 3.7
# Coding utf-8

from microbit import *


def clignotant_droit():
    for i in range(3):
        for x in range(5):
            for y in range(5):
                display.set_pixel(x,y,1+2*x)
            sleep(200)
        display.clear()

def clignotant_gauche():
    for i in range(3):
        for x in range(5):
            for y in range(5):
                display.set_pixel(4-x,y,1+2*x)
            sleep(200)
        display.clear()

#Pour utiliser les fonctions
while True:
    if button_b.is_pressed():
        clignotant_droit()
        sleep(200)
    elif button_a.is_pressed():
        clignotant_gauche()
        sleep(200)
    else:
        sleep(200)
