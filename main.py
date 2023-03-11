"""
Title: Hyper Truck
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


"""
Functions for drawing shapes.
"""

# Egor
def draw_rectangle(width, length, angle, border_color, fill_color):
    pd()
    begin_fill()
    color(border_color, fill_color)
    rt(angle)
    fd(width)
    rt(90)
    fd(length)
    rt(90)
    fd(width)
    rt(90)
    fd(length)
    end_fill()
    rt(90)
    pu()
    goto(0,0)


# Evgeny
def triangle_exist(a, b, c):
    """Return True if a triangle with sides a, b, c exists."""
    return a + b > c and b + c > a and c + a > b


def triangle_angle(a, b, c):
    """Return the angle (in degrees) opposite the side of length a in the
     triangle with sides a, b, c."""
    return degrees(acos((b**2 + c**2 - a**2) / (2.0 * b * c)))


def draw_triangle(a, b, c, border_clr, fill_clr):
    """Draw a triangle with sides of lengths a, b, c.
    For right triangle: a - leg, b - hypotenuse, c - base.
    border_clr - color of a border; fill_clr - color of fill."""
    corner_1 = triangle_angle(b, c, a)
    corner_2 = triangle_angle(c, a, b)
    color(border_clr, fill_clr)
    assert(triangle_exist(a, b, c))
    pd()
    begin_fill()
    print("The first vertex: ", pos())
    forward(c)
    left(180 - corner_1)
    print("The second vertex: ", pos())
    forward(a)
    left(180 - corner_2)
    print("The third vertex: ", pos())
    forward(b)
    right(360 - (corner_1 + corner_2))
    end_fill()
    pu()


# Nikolay


"""
Start position of turtle
"""

goto(0, 0)


"""
Start of drawing
"""

# Egor

rt(270)
# # Square1
draw_rectangle(75,75,0,'blue1','brown')
# Square 2
goto(-100,0)
draw_rectangle(100,100,0,'blue1','brown')
# Square 3
goto(-100,100)
draw_rectangle(100,100,0,'blue1','brown')
goto(-150,100)
rt((1/sqrt(5)))
draw_triangle(50,100,sqrt(12500),'blue1','brown')


# Evgeny


# Nikolay


done()

