# Created by Gabypotter08 in Python 3.7
# Coding utf-8

from microbit import *


def right_indicator():
    for i in range(3):
        for x in range(5):
            for y in range(5):
                display.set_pixel(x,y,1+2*x)
            sleep(200)
        display.clear()

def left_indicator():
    for i in range(3):
        for x in range(5):
            for y in range(5):
                display.set_pixel(4-x,y,1+2*x)
            sleep(200)
        display.clear()

#To use functions
while True:
    if button_b.is_pressed():
        right_indicator()
        sleep(200)
    elif button_a.is_pressed():
        left_indicator()
        sleep(200)
    else:
        sleep(200)
