import pygame
from math import pi
from pygame.draw import *

pygame.init()

FPS = 30

Black=(0,0,0)
Red=(255,0,0)
Blue=(0,0,255)
White=(255,255,255)
Skyblue=(135,206,235)
Grey=(105,105,105)
Brown=(139,115,85)
Yellow=(255,255,0)
Black1=(0,0,0,65)
White1=(255,255,255,65)

screen = pygame.display.set_mode((600, 400))
"""Sand,Sea,Sky"""
polygon(screen, Yellow, [(0,400),(0,300),(600,300),(600,400)])
polygon(screen, Blue, [(0,300),(0,200),(600,200),(600,300)])
for x in range (0,655,110):
    ellipse(screen, Yellow,[x,295,60,25])
    ellipse(screen, Blue,[(x+55),285,60,25])
polygon(screen, Skyblue, [(0,200),(0,0),(600,0),(600,200)])
"""Sun"""
circle(screen, Yellow, (520,80), 40)

"""Umbrella"""
polygon(screen, Brown, [(100,350),(100,250),(108,250),(108,350)])
polygon(screen, Red, [(100,250),(100,220),(108,220),(108,250)])

polygon(screen, Red, [(108,220), (188,250), (108,250)])
polygon(screen, Red, [(100,220), (20,250), (100,250)])

line(screen, Black,(108,220), (168,250))
line(screen, Black,(108,220), (148,250))
line(screen, Black,(108,220), (128,250))
line(screen, Black,(108,220), (108,250))

line(screen, Black,(100,220), (100,250))
line(screen, Black,(100,220), (80,250))
line(screen, Black,(100,220), (60,250))
line(screen, Black,(100,220), (40,250))

def boat (long, high, size):
    """ Функция, рисуящая лодку в заданых координатах, размер которой можно кратно задать 
    1 - обычная лодка, 2 в 2 раза большая итд.
    """
    x=long
    y=high
    s=size
    rect(screen,Brown, [x, y, 100*s, 15*s])
    circle(screen,Brown,[x,y],15*s, draw_bottom_left=True)
    polygon(screen,Brown,[(x+100*s,y), (x+100*s+35*s,y),(x+100*s,y+15*s)])
    circle(screen,White,(x+100*s+7*s,y+5*s), 4*s)
    circle(screen,Black,(x+100*s+7*s,y+5*s), 4*s,s)
    polygon(screen, Black, [(x+50*s,y),(x+50*s+4*s,y),(x+50*s+4*s,y-50*s),(x+50*s,y-50*s)])
    polygon(screen, Grey, [(x+50*s+4*s,y-50*s),(x+50*s+30*s,y-50*s+25*s),(x+50*s+30*s-20*s,y-50*s+25*s)])
    polygon(screen, Black, [(x+50*s+4*s,y-50*s),(x+50*s+30*s,y-50*s+25*s),(x+50*s+30*s-20*s,y-50*s+25*s)], 1)
    polygon(screen, Grey, [(x+50*s+4*s,y),(x+50*s+30*s,y-50*s+25*s),(x+50*s+30*s-20*s,y-50*s+25*s)])
    polygon(screen, Black, [(x+50*s+4*s,y),(x+50*s+30*s,y-50*s+25*s),(x+50*s+30*s-20*s,y-50*s+25*s)], 1)


"""Cloud"""
def cloud (long, high, size, shape, a):
    """ Функция, рисуящая облака в заданых координатах, размер которых можно кратно задать (от 0 до 2), 
    степень сплющенности shape, степень прозрачности где 1 - не прозрачно"""
    x=long
    y=high
    s=size
    z=shape
    """if a > 1:
    ellipse = pygame.Surface((1000,750), pygame.SRCALPHA)
    White=White1
    Black=Black1"""
    ellipse(screen, White,[x,y,30*s+10*z,40*s])
    ellipse(screen, Black,[x,y,30*s+10*z,40*s],1)
    
    ellipse(screen, White,[x-20*s,y+10*s,30*s+10*z,40*s])
    ellipse(screen, Black,[x-20*s,y+10*s,30*s+10*z,40*s],1)
    
    ellipse(screen, White,[x+30*s,y,30*s+10*z,40*s])
    ellipse(screen, Black,[x+30*s,y,30*s+10*z,40*s],1)
    
    ellipse(screen, White,[x+10*s,y+20*s,30*s+10*z,40*s])
    ellipse(screen, Black,[x+10*s,y+20*s,30*s+10*z,40*s],1)
    
    ellipse(screen, White,[x+40*s,y+20*s,30*s+10*z,40*s])
    ellipse(screen, Black,[x+40*s,y+20*s,30*s+10*z,40*s],1)
    
    ellipse(screen, White,[x+60*s,y,30*s+10*z,40*s])
    ellipse(screen, Black,[x+60*s,y,30*s+10*z,40*s],1)
    
    ellipse(screen, White,[x+70*s,y+20*s,30*s+10*z,40*s])
    ellipse(screen, Black,[x+70*s,y+20*s,30*s+10*z,40*s],1)



boat(100,200,1)
boat(300,250,2)
cloud(250,5,0.5,1,1)





    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()