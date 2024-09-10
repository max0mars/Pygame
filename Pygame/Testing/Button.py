import pygame


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