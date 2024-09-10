import pygame


class Character():
    def __init__(self, name, health, damage, attackSpeed):
        self.name = name
        self.health = health
        self.damage = damage
        self.attackSpeed = attackSpeed
        self.cooldown = 10/attackSpeed
    def __str__(self):
        return f"{self.name} has {self.health} hp, {self.damage} attack, and an attack speed of {self.attackSpeed}"
    def attack(self, time, target):
        #update cooldowns of all abilities
        #get list of abilities not on cooldown
        #randomly pick one OR use in sequence?
        self.cooldown -= time
        if(self.cooldown < 0):
            target.health -= self.damage
            self.cooldown = 10/self.attackSpeed
    def surface(self, font, x, y):
        surf = font.render(self.name, False, 'Black')
        rec = surf.get_rect(center = (x, y))
        return surf

