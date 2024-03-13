from turtle import *

tracer(0)
screensize(2000, 2000)
k = 30

left(90)

for i in range(2):
    forward(9*k)
    right(90)
    forward(15*k)
    right(90)

penup()
forward(12*k)
right(90)
pendown()

for i in range(2):
    forward(6*k)
    right(90)
    forward(12*k)
    right(90)

penup()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(5)

done()