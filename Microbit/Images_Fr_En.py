from microbit import *

#To show the images delete '"""'

"""
image1 = Image("09090:""90909:""09090:""90909:""09090:""90909")
display.show(image1)
"""
"""
for x in range(5):
    for y in range(5):
        if (x+y)%2!=0: 
            display.set_pixel(x,y,9)
        else:
            display.set_pixel(x,y,0)
"""
"""
image2 = Image("03579:""03579:""03579:""03579:""03579:")
display.show(image2)
"""
"""
for x in range(5):
    for y in range(5):
        if y==1:
            display.set_pixel(y,x,3)
        elif y==2:
            display.set_pixel(y,x,5)
        elif y==3:
            display.set_pixel(y,x,7)
        elif y==4:
            display.set_pixel(y,x,9)
"""
"""
while True:
    for x in range(5):
        for y in range(5):
            display.set_pixel(x,y,1+2*x)
        sleep(200)
    display.clear()
"""

"""
image3 = Image("35790:""57903:""79035:""90357:""03579:")
display.show(image3)
"""
"""
for x in range(5):
    for y in range(5):
        if (x+y)%5==0:
            display.set_pixel(x,y,3)
        elif (x+y)%5==1:
            display.set_pixel(x,y,5)
        elif (x+y)%5==2:
            display.set_pixel(x,y,7)
        elif (x+y)%5==3:
            display.set_pixel(x,y,9)
        elif (x+y)%5==4:
            display.set_pixel(x,y,0)
"""
