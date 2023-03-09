"""
Title
Group:
Gagol Egor
Tarlo Evgeny
Karpenko Nikolay
"""

from turtle import *
from math import *

screen = Screen()
screen.setup(width=1.0, height=1.0)
"""Full-screen mode."""
speed(0)
"""Drawing speed (0 - the fastest)."""


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
def triangle_exist(a, b, c):
    """Return True if a triangle with sides a, b, c exists."""
    return a + b > c and b + c > a and c + a > b


def triangle_angle(a, b, c):
    """Return the angle (in degrees) opposite the side of length a in the
     triangle with sides a, b, c."""
    return degrees(acos((b**2 + c**2 - a**2) / (2.0 * b * c)))


def draw_triangle(a, b, c, border_clr, fill_clr):
    """Draw a triangle with sides of lengths a, b, c
    border_clr - color of a border; fill_clr - color of fill."""
    corner_1 = triangle_angle(b, c, a)
    corner_2 = triangle_angle(c, a, b)
    color(border_clr, fill_clr)
    assert(triangle_exist(a, b, c))
    begin_fill()
    forward(c)
    left(180 - corner_1)
    forward(a)
    left(180 - corner_2)
    forward(b)
    right(360 - (corner_1 + corner_2))
    end_fill()


draw_triangle(400, 350, 200, 'black', 'red')


# Nikolay


done()

