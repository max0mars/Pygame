import pygame
import random
from sys import exit

# Required to initialize
pygame.init()
sx = 500
sy = 600
screen = pygame.display.set_mode((sx,sy))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
running = True
time = 0
dt = 0

font1 = pygame.font.Font(None, 50)#(font file location, font size)
counter = 0


x_velo = 0
x_acc = 0.1
y_velo = 0
y_acc = 0.1

bounce = .9

player_pos = pygame.Vector2(80, 80)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mx,my) = pygame.mouse.get_pos()
            if(counter < 5):
                if(abs(abs(mx) - abs(player_pos.x)) < 60 and abs(abs(my) - abs(player_pos.y)) < 60):
                    if(x_velo > 0): x_velo += random.uniform(10, 60)
                    else : x_velo -= random.uniform(10, 60)

                    if(y_velo > 0): y_velo += random.uniform(10, 60)
                    else : y_velo -= random.uniform(10, 60)
                    counter += 1



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)


    text_surface = font1.render(str(counter), True, 'Blue')
    time_surface = font1.render(str(round(time, 2)), True, 'Blue')
    screen.blit(text_surface,(sx/2,50))
    screen.blit(time_surface,(sx/2,100))


    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     #player_pos.y -= 300 * dt
    #     y_velo -= y_acc
    # if keys[pygame.K_s]:
    #     #player_pos.y += 300 * dt
    #     y_velo += y_acc
    # if keys[pygame.K_a]:
    #     #player_pos.x -= 300 * dt
    #     x_velo -= x_acc
    # if keys[pygame.K_d]:
    #     #player_pos.x += 300 * dt
    #     x_velo += x_acc
    player_pos.y += y_velo
    player_pos.x += x_velo

    if(player_pos.x < 40):
        x_velo = -x_velo
        x_velo *= bounce
        #counter+=1
        player_pos.x = 41
    elif(player_pos.x > sx-40):
        x_velo = -x_velo
        x_velo *= bounce
        #counter+=1
        player_pos.x = sx-41
    if(player_pos.y < 40):
        y_velo = -y_velo
        y_velo *= bounce
        #counter += 1
        player_pos.y = 41
    elif(player_pos.y > sy-40): 
        y_velo = -y_velo
        y_velo *= bounce
        #counter += 1
        player_pos.y = sy-41
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    if(counter < 5):
        time += dt
        

pygame.quit()

#*******************
#Rectangles
#*******************

#create a surface first 'player_surface'

#player_rect = pygame.Rect(left, top, width, height) #OR
#player_rect = player_surface.get_rect(topleft = (x,y)) # sets the position of rect to (x,y)
#locations for rect: topleft, midtop, topright, midleft, midright, bottomleft, midbottom, bottomright, center

#screen.blit(player_surface,player_rect) #puts surface in rect location

#player_rect.left += 1 #this will move the player to the right
#player_rect.left # this will return the left position of the player

#


#*******************
#Rectagle Collisions
#*******************

#rect1.colliderect(rect2) #check for collision between rect1 and rect2, returns 0 or 1
#careful because collision will trigger every frame

#rect1.collidepoint((x,y)) #check if rect is overtop position



#*******************
#mouse
#*******************

#pygame.mouse
#position, buttons being pressed, mouse visibility, and more!
#mouse_pos = pygame.mouse.get_pos() # returns tuple



#events to get mouse info
