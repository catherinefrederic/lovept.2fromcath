import math
from turtle import *

def heart(k):
    return 15*math.sin(k)**3

def heart1(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)

speed(1500)
bgcolor('black')
for i in range(6000):
    goto(heart(i)*20,heart1(i)*20)
    for j in range(5):
        color('magenta')

done()