'''
Title
Group:
Gagol Egor
Tarlo Evgeny
Karpenko Nikolay
'''

from turtle import *
from math import *
# Drawing speed (0 - the fastest)
speed(0)


# Egor
# function to a rectangle
#
def draw_rectangle(width, length, angle, border_color, fill_color):
    pd()
    rt(angle)
    fd(width)
    rt(90)
    fd(length)
    rt(90)
    fd(width)
    rt(90)
    fd(length)

draw_rectangle(20,50,0,0,0)

# Evgeny

# function to draw a rectangle
# side - left and right sides
# base - the base
# angle - the angle under which you need to draw
# corner - the corner between side and base
# border_color - the color of border
# fill_color - the color of fill
def triangle(side, base, angle, corner, border_color, fill_color):
    rt(angle)
    fd(side)




# Nikolay


done()
