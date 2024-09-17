import pygame

selCol = (230,230,230)
unselCol = (250,250,250)

class Textbox():
    rectangle = None
    text = ''
    selected = False

    def __init__(self, list:list, font: pygame.font, size:tuple, pos: tuple):
        self.font = font
        self.size = size
        self.pos = pos
        list.append(self)

    def surf(self):
        sc = pygame.Surface((self.size[0], self.size[1]))
        sc.fill(selCol if self.selected else unselCol)
        txt = self.font.render(self.text, True, 'Black')
        rect = txt.get_rect(center = (self.size[0]/2, self.size[1]/2))
        sc.blit(txt,rect)

        self.rectangle = sc.get_rect(center = self.pos)
        return sc
    