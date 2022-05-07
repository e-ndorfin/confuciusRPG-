import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            '../graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            '../graphics/objects/03.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)


class Trigger(pygame.sprite.Sprite):  # needs to connect with other Trigger
    # maybe can append to ordered list/dictinoary with corresponding pairs?
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            '../graphics/blank.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
