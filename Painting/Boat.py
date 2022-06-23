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

screen = pygame.display.set_mode((600, 400))
"""Sand,Sea,Sky"""
polygon(screen, Yellow, [(0,400),(0,300),(600,300),(600,400)])


polygon(screen, Blue, [(0,300),(0,200),(600,200),(600,300)])
"""for _ in range (15"""
ellipse(screen, Yellow,[0,290,50,20])
ellipse(screen, Blue,[50,290,50,20])
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

"""Boat"""
rect(screen,Brown, [320,220 , 200, 30])
circle(screen,Brown,[320,220],30, draw_bottom_left=True)
polygon(screen,Brown,[(520,220), (590,220),(520,250)])
circle(screen,White,(535,231), 8)
circle(screen,Black,(535,231), 8,2)

"""Sail"""
polygon(screen, Black, [(400,220),(408,220),(408,120),(400,120)])

polygon(screen, Grey, [(408,120),(468,170),(428,170)])
polygon(screen, Black, [(408,120),(468,170),(428,170)], 1)

polygon(screen, Grey, [(408,220),(468,170),(428,170)])
polygon(screen, Black, [(408,220),(468,170),(428,170)], 1)

"""Cloud"""
circle(screen,White,(140,50), 20)
circle(screen,Black,(140,50), 20,1)

circle(screen,White,(120,65), 20)
circle(screen,Black,(120,65), 20,1)

circle(screen,White,(170,50), 20)
circle(screen,Black,(170,50), 20,1)

circle(screen,White,(150,70), 20)
circle(screen,Black,(150,70), 20,1)

circle(screen,White,(180,70), 20)
circle(screen,Black,(180,70), 20,1)

circle(screen,White,(200,50), 20)
circle(screen,Black,(200,50), 20,1)

circle(screen,White,(210,69), 20)
circle(screen,Black,(210,69), 20,1)





    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()