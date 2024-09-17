import pygame
from sys import exit
from Textbox import Textbox

pygame.init()
sx = 800
sy = 400
screen = pygame.display.set_mode((sx, sy))
running = True
font1 = pygame.font.Font(None, 15)
clock = pygame.time.Clock()
dt = 0

textboxes = []

textbox = Textbox(textboxes, font1, (400,50), (400,150))
textbox2 = Textbox(textboxes, font1, (400,50), (400,250))

while running:
    screen.fill('green')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            for i in textboxes:
                if(i.rectangle.collidepoint(mpos)):
                    i.selected = True
                else:
                    i.selected = False
    
    for i in textboxes:
        screen.blit(i.surf(), i.rectangle)
    dt = clock.tick(60)
    pygame.display.update()