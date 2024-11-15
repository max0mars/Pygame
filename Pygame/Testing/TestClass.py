import pygame

_100 = 200
OFFSETLEFT = 50
sizex = 200
sizey = 200

class BANK():
    rectangle = None
    attackCount = 0
    countTotal = 10
    elims = 0
    def __init__(self, name, money, debt, speed):
        self.name = name
        self.money = money
        self.total = money
        self.debt = debt
        self.speed = speed

    def __str__(self):
        return f"{self.name}: ${self.money} - ${self.debt}"

    def names(b):
        list = []
        for i in b:
            list.append(i.name)
        return list
    
    def copy(self):
        return BANK(self.name, self.money, self.debt, self.speed)

    def surf(self, font):
        sc = pygame.Surface((sizex, sizey))
        sc.set_colorkey((255,0,255))
        sc.fill((255,0,255))
        txt = font.render(self.name, True, 'Black')
        rect = txt.get_rect(midbottom = (sizex/2, sizey - 5))

        percent = self.money/self.total
        left = (0, rect.centery)
        right = (_100 * percent, rect.centery)

        pygame.draw.line(sc, 'red', left, right, 30)

        percent = self.attackCount / self.countTotal
        left = (0, rect.centery + 10)
        right = (_100 * percent, rect.centery + 10)
        pygame.draw.line(sc, 'grey', left, right, 10)
        pygame.draw.circle(sc, 'green', (sizex/2, sizey/2), 40)
        elimtxt = font.render(str(self.elims), True, 'Black')
        elimrect = elimtxt.get_rect(center = ((sizex/2, sizey/2)))
        pygame.draw.rect(sc, 'black', sc.get_rect(), 5)
        sc.blit(txt, rect)
        sc.blit(elimtxt, elimrect)

        
        #sc.convert_alpha()
        return sc

    
