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

arc(screen, Red,[0,295,50,5], 0.35, 2.8, 3)







    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()