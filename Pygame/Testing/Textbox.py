#How to Use:

# create new textbox with the specified traits: 
# list<Textbox>, font, size(x,y), and position(x,y), 'Default' to set display when empty

# to display the button:
# for i in list<Textbox>: 
#     i.draw()

# for events:
# call Textbox.handleEvent(list, event)



import pygame
selCol = (230,230,230)
unselCol = (250,250,250)

class Textbox():
    rectangle = None
    text = ''
    selected = False


    def __init__(self, list:list, font: pygame.font, size:tuple, pos: tuple, **kwargs):
        self.font = font
        self.size = size
        self.pos = pos
        list.append(self)
        self.default = kwargs.get("Default", None)
        self.readOnly = kwargs.get("ReadOnly", False)
        self.color = kwargs.get("color", None)
        self.txt_surf = self.font.render(self.text, True, 'Black')
        self.rectangle = pygame.Rect(size, pos)
        self.rectangle.center = (pos)
        self.active = True
    
    def enable(self):
        self.active = True
    def disable(self):
        self.active = False
        self.selected = False

    def draw(self, screen):
        if(not self.active):
            return
        sc = pygame.Surface((self.size[0], self.size[1]))
        sc.fill(selCol if self.selected else (self.color if self.color else unselCol))
        if(self.text == ''):
            txt = self.font.render(self.default, True, 'Black')
        else:
            txt = self.font.render(self.text, True, 'Black')
        rect = txt.get_rect(center = (self.size[0]/2, self.size[1]/2))
        sc.blit(txt,rect)

        self.rectangle = sc.get_rect(center = self.pos)
        screen.blit(sc, self.rectangle)

    def handleEvent(list:list, event:pygame.event): #handles the events applicable to textbox
        if(event.type == pygame.MOUSEBUTTONDOWN):
            for i in list:
                if(not i.active or i.readOnly):
                    continue
                if(i.rectangle.collidepoint(event.pos)):
                    i.selected = True
                else:
                    i.selected = False
        if(event.type == pygame.KEYDOWN):
            for i in list:
                if(not i.selected or not i.active or i.readOnly):
                    continue
                else:
                    if(event.key < 65 or event.key > 122):
                        if(event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE):
                            i.text = i.text[:-1]
                        if(event.key == pygame.K_SPACE):
                            i.text += ' '
                    else :     
                        i.text += chr(event.key)
    