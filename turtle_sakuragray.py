#author: hanshiqiang365 （微信公众号：韩思工作室）

from turtle import *
from random import *
from math import *
import pygame
import time

def tree(n, l):
    pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n)
    forward(l)
    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        right(b)
        tree(n - 1, d)
        left(b + c)
        tree(n - 1, d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n, n)
        circle(2)
        left(90)
    pu()
    backward(l)

bgcolor(0.5, 0.5, 0.5)

title('Sakura drawed by hanshiqiang365 - Happy New Year 2020 ')

pygame.mixer.init()
pygame.mixer.music.load("sakura_bgm.mp3")
pygame.mixer.music.play(-1)

time.sleep(10)

ht()
speed(0)
tracer(1000000, 0)
left(90)
pu()
backward(300)
tree(12, 100)

pu()
goto(30, -300)
pd()
write('韩思工作室出品', font=("繁体隶书", 30, "bold"))

done()

