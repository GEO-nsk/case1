'''
Title
Group:
Gagol Egor
Tarlo Evgeny
Karpenko Nikolay
'''

from turtle import *
speed(0)  # Drawing speed (0 - the fastest)

# function to draw a line
line_lenght = 900
def line(line_lenght):
    pd()
    fd(line_lenght)
    pu()

# lines for dividing the drawing space into 3 parts
pu()
lt(90)
fd(450)
lt(90)
fd(150)
lt(90)
line(line_lenght)
lt(90)
fd(300)
lt(90)
line(line_lenght)

# Return to the starting point
setx(0)
sety(0)
rt(90)


# Egor


# Evgeny

# function to draw a rectangle
def rectangle(w, h):
    for i in range(2):
        fd(w)
        lt(90)
        fd(h)
        lt(90)


# Nikolay


done()
