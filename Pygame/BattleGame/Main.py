import pygame
import random
from sys import exit

from Character import Character

FIGHT = 1
STOP = 0
state = STOP

pygame.init()
sx = 500
sy = 600
screen = pygame.display.set_mode((sx,sy))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
running = True
dt = 0

font1 = pygame.font.Font(None, 50)#(font file location, font size)

guy = Character('circle', 20, 7, 6)
Tim = Character('square', 50, 4, 2.5)
#clock = time.clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if(state == STOP):
        screen.fill("blue")
        guy_surface = pygame.Surface(sx, sy)
        
    
    dt = clock.tick(60) / 1000

pygame.quit()