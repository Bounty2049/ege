from turtle import *

tracer(0)
k = 30

left(90)

for i in range(10):
    forward(9*k)
    right(90)
    forward(2*k)
    right(90)

penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*k, y*k)
        dot(5)

done()