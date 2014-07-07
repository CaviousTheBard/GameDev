# -*- coding: utf-8 -*-

import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640, 360), 0, 32)

clock = pygame.time.Clock()
FPS = 24

clr1 = (22, 122, 211)
clr2 = (0, 44, 166)
clr3 = (34, 55, 245)

while True:
    #PROCESSES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #PROCESSES
    #LOGIC

    #LOGIC
    #DRAW

    pygame.draw.line(screen, clr2, (0, 0), (640, 360))

    pygame.display.flip()
    #DRAW

    clock.tick(FPS)
    print(clock)