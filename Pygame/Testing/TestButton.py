import pygame
from sys import exit
from TestClass import BANK
from Button import Button
import random

pygame.init()
sx = 800
sy = 400
screen = pygame.display.set_mode((sx, sy))
running = True
font1 = pygame.font.Font(None, 25)
clock = pygame.time.Clock()
dt = 0

Buttons = []
Colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'pink']
cdex = random.randrange(0,7)

b = Button(Buttons, "Change Color", font1, 'gray', (200, 50), (400,200))

def bfunc():
    global cdex
    last = cdex
    while(last == cdex):
        cdex = random.randrange(0,7)

b.addfunc(bfunc)
     

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            for i in Buttons:
                if(i.rectangle.collidepoint(mpos)):
                    i.func()

    screen.fill(Colors[cdex])
    screen.blit(b.surf(), b.rectangle)
    dt = clock.tick(60)
    pygame.display.update()