#Project Name: The Great Ship Escape
#Members: Eric Xu, Michael Gao, William Liu, Andrew Wang
#Date: 5/9/2022
#Description: File for border and player containment

# TODO: make Interactable not so repetitive with Border?
import pygame
from util import Util

class Border(pygame.sprite.Sprite):
    def __init__(self, size, pos):
        super().__init__()
        # TODO: why do we need an image here :/
        self.image = Util.load_image("media/wall_border.png", size[0], size[1])
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))

    def update(self):
        pass


