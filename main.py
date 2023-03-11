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

def draw_circle(radius, border_color, fill_color):
    pd()
    begin_fill()
    color(border_color, fill_color)
    circle(radius)
    end_fill()
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
    goto(0, 0)


# Nikolay


"""
Start position of turtle
"""

goto(0, 0)
pu()


"""
Start of drawing
"""

# Egor

# rt(270)
# # Truck
# pd()
# goto(250,0)
# lt(45)
# draw_triangle(sqrt(20000),200,sqrt(20000),'black','Black')
# rt(45)
# draw_rectangle(75,75,0,'Black','Black')
# goto(-100,0)
# draw_rectangle(100,100,0,'Black','DarkRed')
# goto(-100,100)
# draw_rectangle(100,100,0,'Black','azure3')
# goto(-170,100)
# rt(90)
# draw_triangle(100, sqrt(100**2 + 70**2), 70,'Black','azure3')
# lt(90)
# goto(-170,0)
# draw_rectangle(100,70,0,'black','DarkRed')
# goto(20,75)
# draw_rectangle(100,200,0,'Black','Gold2')
# goto(0,-30)
# draw_rectangle(30,250,0,'Black','Black')
# goto(320,175)
# lt(90)
# draw_triangle(100,sqrt(100**2 + 100**2),100,'Black','gold2')
# goto(20,150)
# rt(90)
# draw_triangle(100,sqrt(100**2 + 100**2),100,'Black','gold2')
# lt(90)
# goto(-155,50)
# # wheels
# draw_circle(15,'Black','gold')
# goto(-90,35)
# draw_circle(50,'Black','gray50')
# goto(230,35)
# draw_circle(50,'Black','gray50')
# goto(115,35)
# draw_circle(50,'Black','gray50')
# goto(-90,5)
# draw_circle(20,'Black','gray80')
# goto(230,5)
# draw_circle(20,'Black','gray80')
# goto(115,5)
# draw_circle(20,'Black','gray80')
# goto(-90,-5)
# draw_circle(10,'Black','Black')
# goto(230,-5)
# draw_circle(10,'Black','Black')
# goto(115,-5)
# draw_circle(10,'Black','Black')


# Evgeny
# a - leg, b - hypotenuse, c - base

"""Car body."""
goto(-330, -50)
draw_rectangle(260, 10, 0, 'black', 'black')

goto(-345, -40)
draw_rectangle(40, 40, 0, 'black', 'BlueViolet')

goto(-290, 0)
draw_triangle(50, sqrt(50**2 + 55**2), 55, 'black', 'BlueViolet')

goto(-290, 0)
draw_rectangle(95, 25, 0, 'black', 'BlueViolet')

goto(-290, 7.5)
draw_rectangle(15, 10, 0, 'black', 'red')

goto(-385, 80)
lt(90)
draw_triangle(30, sqrt(30**2 + 55**2), 55, 'black', 'CadetBlue1')
rt(90)


right(180)
"""Right wheel."""
goto(-350, -65)
draw_circle(30, 'black', 'gray50')
goto(-350, -58)
draw_circle(23, 'black', 'gray80')
goto(-350, -41)
draw_circle(6, 'black', 'BlueViolet')


"""Left wheel."""
goto(-580, -65)
draw_circle(30, 'black', 'gray50')
goto(-580, -58)
draw_circle(23, 'black', 'gray80')
goto(-580, -41)
draw_circle(6, 'black', 'BlueViolet')


# Nikolay


done()

