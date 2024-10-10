#How to Use:

# create new button with the specified traits: 
# list<button>, button text, font, color, size(x,y), and position(x,y)
# then use addfunc() to assign an action to this button.

# to display the button:
# for i in list<Button>: 
#     i.draw()

# for events:
# call Button.handleEvent(list, event)

import pygame
class Button():
    rectangle = None

    def __init__(self, list: list, txt: str, font: pygame.font, color: str, size: tuple, pos: tuple):
        self.txt = txt
        self.size = size
        self.color = color
        self.pos = pos
        self.font = font
        self.active = True
        self.rectangle = pygame.Rect(size, pos)
        self.rectangle.center = (pos)
        list.append(self)

    def draw(self, screen):
        if(not self.active):
            return
        sc = pygame.Surface((self.size[0], self.size[1]))
        sc.fill(self.color)
        txt = self.font.render(self.txt, True, 'Black')
        rect = txt.get_rect(center = (self.size[0]/2, self.size[1]/2))
        sc.blit(txt, rect)

        self.rectangle = sc.get_rect(center = self.pos)
        screen.blit(sc, self.rectangle)


    def enable(self):
        self.active = True
    def disable(self):
        self.active = False
    def func(self):
        return self.function()
    
    def addfunc(self, func: callable):
        self.function = func
    
    def handleEvent(list:list, event:pygame.event):
        if(event.type == pygame.MOUSEBUTTONDOWN):
            for i in list:
                if(i.rectangle.collidepoint(event.pos)):
                    i.func()