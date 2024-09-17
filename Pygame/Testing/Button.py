import pygame


#How to Use:

# create new button with the specified traits: 
# list<button>, button text, font, color, size(x,y), and position(x,y)
# then use addfunc() to assign an action to this button.

# to display the button:
# for i in list<Button>: #list you created to store Buttons, can be named whatever
#     screen.blit(i.surf, i.rectangle)

# To check collisisons:
# if event.type == pygame.MOUSEBUTTONDOWN:
#             mpos = pygame.mouse.get_pos()
#             for i in list<Button>: 
#                 if(i.rectangle.collidepoint(mpos)):
#                     i.func()

class Button():
    rectangle = None

    def __init__(self, list: list, txt: str, font: pygame.font, color: str, size: tuple, pos: tuple):
        self.txt = txt
        self.size = size
        self.color = color
        self.pos = pos
        self.font = font
        list.append(self)
        self.surf()

    def surf(self):
        sc = pygame.Surface((self.size[0], self.size[1]))
        sc.fill(self.color)
        txt = self.font.render(self.txt, True, 'Black')
        rect = txt.get_rect(center = (self.size[0]/2, self.size[1]/2))
        sc.blit(txt, rect)

        
        #sc.convert_alpha()
        self.rectangle = sc.get_rect(center = self.pos)
        return sc

    def func(self):
        return self.function()
    
    def addfunc(self, func: callable):
        self.function = func