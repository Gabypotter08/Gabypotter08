# Created by Gabypotter08 in Python 3.7
# Coding utf-8

from microbit import *

a=0
b=0
c=0
while True:
    sleep(5000)
    a=button_a.get_presses()
    b=button_b.get_presses()
    c=a+b
    display.scroll('Boutton a')
    sleep(200)
    display.scroll(a)
    print(a)
    sleep(200)
    display.scroll('Boutton b')
    sleep(200)
    display.scroll(b)
    print(b)
    sleep(200)
    display.scroll('Global')
    sleep(200)
    display.scroll(c)
    print(c)
    sleep(200)
