# Created by Gabypotter08 in Python 3.7
# Coding utf-8

form microbit import *

while True:
    if button_b.is_pressed() and button_a.is_pressed():
        display.show(Image.ARROW_N)
    elif button_b.is_pressed():
        display.show(Image.ARROW_E)
        #sleep(1000)
    elif button_a.is_pressed():
        display.show(Image.ARROW_W)
        #sleep(1000)

        #sleep(1000)
    else:
        display.show(Image.ARROW_S)
    sleep(1000)
