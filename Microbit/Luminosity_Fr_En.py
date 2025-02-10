# Created by Gabypotter08 in Python 3.7
# Coding utf-8

from microbit import *

while True:
    luminosite = display.read_light_level()
    print(luminosite)
    if luminosite <= 50 :
        display.show(Image.ASLEEP)
    elif luminosite < 200 :
        display.show(Image.HAPPY)
    else:
        display.show(Image.CONFUSED)
    
    sleep(200)
    display.clear()
