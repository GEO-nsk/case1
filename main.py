"""
Title: Hyper Truck and not only
Group:
Gagol Egor - 50
Tarlo Evgeny - 60
Karpenko Nikolay - 50
"""

from turtle import *
from math import *

# Full-screen mode.
screen = Screen()
screen.setup(width=1.0, height=1.0)

# Drawing speed (0 - the fastest).
speed(0)


"""
Functions for drawing shapes.
"""

# Egor
def draw_rectangle(width, length, angle, border_color, fill_color):
    """ Draw a rectangle

    :param width: width of rectangle
    :param length: length of rectangle
    :param angle: turns right rectangle
    :param border_color: color of border
    :param fill_color: color of fill
    :return: rectangle with your options
    """
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
    """ Draw a circle.

    :param radius: radius of circle
    :param border_color: color of border
    :param fill_color: color of fill
    :return: circle with your options
    """
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
    """Return the angle (in degrees) opposite the side of length a."""
    return degrees(acos((b**2 + c**2 - a**2) / (2.0 * b * c)))

def draw_triangle(a, b, c, border_clr, fill_clr):
    """Draw a triangle

    Draw a triangle with sides of lengths a, b, c.
    First the side c is drawn, then a and then b.
    border_clr - color of a border; fill_clr - color of fill.
    """

    corner_1 = triangle_angle(b, c, a)
    corner_2 = triangle_angle(c, a, b)
    color(border_clr, fill_clr)
    assert(triangle_exist(a, b, c))
    pd()
    begin_fill()
    forward(c)
    left(180 - corner_1)
    forward(a)
    left(180 - corner_2)
    forward(b)
    right(360 - (corner_1 + corner_2))
    end_fill()
    pu()
    goto(0, 0)


# Nikolay
def draw_pentagon(length, angle, border_color, fill_color):

    pd()
    begin_fill()
    color(border_color, fill_color)
    rt(angle)
    fd(length)
    rt(72)
    fd(length)
    rt(72)
    fd(length)
    rt(72)
    fd(length)
    rt(72)
    fd(length)
    rt(72)

    end_fill()
    pu()
    goto(0,0)

"""
Start position of turtle  
"""

goto(0, 0)
pu()


"""
Start of drawing  
"""

# Nikolay

# Sky
bgcolor('CadetBlue1')

# Road
goto(-2000, -65)
draw_rectangle(4000, 150, 0, 'cornsilk4', 'cornsilk4')

# Markup
goto(-2000, -135)
draw_rectangle(4000, 10, 0, 'GhostWhite', 'GhostWhite')

# River
goto(-2000, -215)
draw_rectangle(4000, 300, 0, 'DarkBlue', 'DarkBlue')

# Sun
goto(800, 340)
draw_circle(65, 'gold', 'gold')

# Grass
goto(-2000, 50)
draw_rectangle(4000, 115, 0, 'green1', 'green1')

# Egor
rt(270)

# Truck body
pd()
goto(250,0)
lt(45)
draw_triangle(sqrt(20000),200,sqrt(20000),'black','Black')
rt(45)
draw_rectangle(75,75,0,'Black','Black')
goto(-100,0)
draw_rectangle(100,100,0,'Black','DarkRed')
goto(-100,100)
draw_rectangle(100,100,0,'Black','azure3')
goto(-170,100)
rt(90)
draw_triangle(100, sqrt(100**2 + 70**2), 70,'Black','azure3')
lt(90)
goto(-170,0)
draw_rectangle(100,70,0,'black','DarkRed')
goto(-30,60)
draw_rectangle(5,15,0,'black','black')

# Truck ladle
goto(20,75)
draw_rectangle(100,200,0,'Black','Gold2')
goto(0,-30)
draw_rectangle(30,250,0,'Black','Black')
goto(320,175)
lt(90)
draw_triangle(100,sqrt(100**2 + 100**2),100,'Black','gold2')
goto(20,150)
rt(90)
draw_triangle(100,sqrt(100**2 + 100**2),100,'Black','gold2')
lt(90)
goto(-155,50)

# wheels
draw_circle(15,'Black','gold')
goto(-90,35)
draw_circle(50,'Black','gray50')
goto(230,35)
draw_circle(50,'Black','gray50')
goto(115,35)
draw_circle(50,'Black','gray50')
goto(-90,5)
draw_circle(20,'Black','gray80')
goto(230,5)
draw_circle(20,'Black','gray80')
goto(115,5)
draw_circle(20,'Black','gray80')
goto(-90,-5)
draw_circle(10,'Black','Black')
goto(230,-5)
draw_circle(10,'Black','Black')
goto(115,-5)
draw_circle(10,'Black','Black')


# Evgeny
# Car body
goto(-330, -50)
draw_rectangle(260, 10, 0, 'black', 'black')
goto(-345, -40)
draw_rectangle(40, 40, 0, 'black', 'BlueViolet')
goto(-290, 0)
draw_triangle(50, sqrt(50**2 + 55**2), 55, 'black', 'BlueViolet')
goto(-290, 0)
draw_rectangle(95, 25, 0, 'black', 'BlueViolet')
goto(-385, -40)
draw_rectangle(75, 65, 0, 'black', 'BlueViolet')
goto(-460, -40)
draw_rectangle(85, 65, 0, 'black', 'BlueViolet')
goto(-545, -40)
draw_rectangle(40, 65, 0, 'black', 'BlueViolet')
goto(-585, -50)
rt(90)
draw_triangle(65, sqrt(65**2 + 30**2), 30, 'black', 'BlueViolet')
goto(-585, -20)
lt(90)
draw_rectangle(65, 45, 0, 'black', 'BlueViolet')

# Windows
goto(-385, 80)
lt(90)
draw_triangle(30, sqrt(30**2 + 55**2), 55, 'black', 'CadetBlue1')
rt(90)
goto(-385, 25)
draw_rectangle(75, 55, 0, 'black', 'CadetBlue1')
goto(-460, 25)
draw_rectangle(85, 55, 0, 'black', 'CadetBlue1')
goto(-585, 25)
rt(180)
draw_triangle(55, sqrt(55**2 + 40**2), 40, 'black', 'CadetBlue1')
lt(180)

# Roof
goto(-385, 77)
draw_rectangle(160, 3, 0, 'black', 'BlueViolet')

# Headlight
goto(-640, 20)
draw_circle(10, 'black', 'gold')

# Taillight
goto(-290, 7.5)
draw_rectangle(15, 10, 0, 'black', 'red')

# Right wheel
right(180)
goto(-350, -65)
draw_circle(33, 'black', 'gray50')
goto(-350, -57)
draw_circle(25, 'black', 'gray80')
goto(-350, -38)
draw_circle(6, 'black', 'black')

# Left wheel
goto(-580, -65)
draw_circle(33, 'black', 'gray50')
goto(-580, -57)
draw_circle(25, 'black', 'gray80')
goto(-580, -38)
draw_circle(6, 'black', 'black')

# Nikolay
# Apple Tree
goto(-800, 150)
draw_rectangle(50, 150, 0, 'Brown', 'Brown')
goto(-775, 140)
draw_circle(100, 'green', 'green')

# Apples
goto(-840, 180)
draw_circle(10, 'red', 'red')
goto(-840, 230)
draw_circle(10, 'red', 'red')
goto(-735, 200)
draw_circle(15, 'yellow', 'yellow')
goto(-770, 190)
draw_circle(10, 'red', 'red')
goto(-790, 250)
draw_circle(10, 'red', 'red')
goto(-800, 145)
draw_circle(15, 'yellow', 'yellow')
goto(-840, 260)
draw_circle(15, 'yellow', 'yellow')
goto(-800, 290)
draw_circle(10, 'red', 'red')
goto(-840, 180)
draw_circle(10, 'red', 'red')
goto(-735, 290)
draw_circle(15, 'yellow', 'yellow')

# Christmas tree leaves
goto(500, 200)
draw_triangle(40, 40, 50, 'DarkGreen', 'DarkGreen')
goto(487.5, 160)
draw_triangle(60, 60, 75, 'DarkGreen', 'DarkGreen')
goto(468.75, 100)
draw_triangle(90, 90, 112.5, 'DarkGreen', 'DarkGreen')

# Christmas tree trunk
goto(520, 100)
draw_rectangle(10, 50, 0, 'Brown', 'Brown')

# Bush
goto(800, 100)
draw_pentagon(70, 36, 'DarkGreen', 'DarkGreen')
done()



