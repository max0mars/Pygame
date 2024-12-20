import pygame
from sys import exit
from TestClass import BANK
from Button import Button
from Textbox import Textbox

import random

pygame.init()
sx = 800
sy = 400
screen = pygame.display.set_mode((sx, sy))
running = True
font1 = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
dt = 0

player = BANK('Me', 100, 10, 5)

state = 0 #0 = menu, 1 = fight

menu = pygame.Surface((sx,sy))

color_light = (170,170,170) 
color_dark = (100,100,100)

buttonx = 140
buttony = 40


#test
def testFunc():
    print("Button Function")

buttons = []
testButton = Button(buttons, 'PLAY', font1, 'gray', (buttonx,buttony), (400, 200))

textboxes = []
namebox = Textbox(textboxes, font1, (400,50), (400,150), default='Enter your name here', color=(220,220,220))

def play():
    if(namebox.text == ''):
        namebox.default = 'Pls Enter Name!'
        return
    global state
    state = 1
    global visibleDudes
    testButton.active = False
    namebox.active = False
    player.name = namebox.text

    visibleDudes = [player.copy(), dude3.copy()]
    shopText.active = True

testButton.addfunc(play)

player = BANK("Player", 500, 25, 20)

dude = BANK('Fred', 25, 10, 10)
dude2 = BANK('Ned', 200, 30, 8)
dude3 = BANK('Ted', 500, 50, 5)
dude4 = BANK('Bill', 2000, 50, 4)
dude5 = BANK('Mack', 10000, 300, 3)
dudes = [dude, dude2, dude3, dude4, dude5]
visibleDudes = [] * 2
dudesurf = [None] * 2


shop = pygame.Surface((800,400))
shop.fill("red")
shopText = Textbox(textboxes, font1, (400,50), (400,150), default='Shop', color=(220,220,220), readOnly=True, active=False)
shopText.draw(shop)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        Button.handleEvent(buttons, event)
        Textbox.handleEvent(textboxes, event)

    screen.fill("white")
    
    for i in buttons: #display all buttons
        i.draw(screen)
    for i in textboxes:
        i.draw(screen)

    if(state == 1):
        shopText.draw(shop)
        screen.blit(shop,(0,0))
        # for n in range(2):
        #     if(visibleDudes[n].money <= 0):#check if dude is out of money
        #         state = 0
        #         continue
        #     visibleDudes[n].attackCount += dt/1000 * visibleDudes[n].speed
        #     if(visibleDudes[n].attackCount > 10):
        #         visibleDudes[n].attackCount = 0
        #         if(n == 0):
        #             visibleDudes[1].money -= visibleDudes[0].debt
        #         else:
        #             visibleDudes[0].money -= visibleDudes[1].debt

        #     dudesurf[n] = visibleDudes[n].surf(font1)#get the surface
        #     visibleDudes[n].rectangle = dudesurf[n].get_rect(center = (200 + 400 * n, 200))# set the rect
        #     screen.blit(dudesurf[n], visibleDudes[n].rectangle)#send to the screen

            
            

    dt = clock.tick(60)
    pygame.display.update()




    # List of 5 dudes
    # two are always visible
    # picks a random one to fill the spot of one when they run out of money


    # check if two slots are filled
    # if yes do nothing
    # if no get random number 0-4
    # copy that dude into the slot
    # check money of dudes in the slots
    # if 0 remove from slot

