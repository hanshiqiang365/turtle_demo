#author: hanshiqiang365 （微信公众号：韩思工作室）

from turtle import *
from random import *
from math import *
import pygame
import time

def tree(n,l):
    pd()
    color('sienna') 
    pensize(n)
    forward(l)

    if n>0:
        b = random()*15+10
        c = random()*15+10
        d = l*(random()*0.25+0.7)
        right(b)
        tree(n-1,d)
        left(b+c)
        tree(n-1,d)
        right(c)
    else:
        right(90)
        color('lightcoral')
        circle(3)
        left(90)
        if(random()>0.7):
            pu()
            t = heading()
            an = -40 +random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
            pd()
            right(90)
            color('lightcoral')
            circle(2)
            left(90)
            pu()
            t=heading()
            setheading(an)
            backward(dis)
            setheading(t)
    pu()
    backward(l)

def petal(m):
    for i in range(m):
        a = 200 - 400 * random()
        b = 10 - 20 * random()
        pu()
        forward(b)
        left(90)
        forward(a)
        pd()
        color('lightcoral')
        circle(1)
        pu()
        backward(a)
        right(90)
        backward(b)


title('Sakura Falling drawed by hanshiqiang365 - Happy New Year 2020 ')

screensize(bg='wheat')

pygame.mixer.init()
pygame.mixer.music.load("sakura_bgm.mp3")
pygame.mixer.music.play(-1)

time.sleep(10)

ht()
speed(0)
tracer(100000000,0)
pu()
backward(100)
left(90)
pu()
backward(300)
tree(12,100)
petal(200)

pu()
goto(10, -380)
pd()
write('韩思工作室出品', font=("繁体隶书", 30, "bold"))

done()

