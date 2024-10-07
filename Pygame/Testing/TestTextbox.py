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
        Textbox.handleEvent(textboxes, event)
    
    for i in textboxes:
        i.draw(screen)
    dt = clock.tick(60)
    pygame.display.update()