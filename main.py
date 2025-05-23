import pygame


class Bullet(pygame.sprite.Sprite):
 def __init__(self, x, y, bullet_group, player):
    super().__init__()

    self.VELOCITY = 20
    self.RANGE = 500
   
