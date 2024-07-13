#Project Name: The Great Ship Escape
#Members: Eric Xu, Michael Gao, William Liu, Andrew Wang
#Date: 5/9/2022
#Description: File for utility functions, image loading, mouse generation. 

import json
import pygame
from argparse import ArgumentError
import json
import re

#creates a sprite for current mouse position; used to detect collisions with sprites
class MouseBox(pygame.sprite.Sprite):
    def __init__(self,offset=(0,0)):
        super().__init__()
        x,y = pygame.mouse.get_pos()
        dx,dy = offset
        x-=dx
        y-=dy
        self.rect = pygame.Rect(x,y,1,1) 

class Util:
    # Utility methods

    #loads image as surface and resizes
    def _load_image(file_path, width, height):
        img = pygame.image.load(file_path)
        img = pygame.transform.scale(img, (width, height))

        return img

    #alternate constructors for loading image
    def load_image(file_path, *args):
        if len(args) == 0:
            return pygame.image.load(file_path)
        elif len(args) == 1:

            return Util._load_image(file_path, args[0][0], args[0][1])
        elif len(args) == 2:
            return Util._load_image(file_path, args[0], args[1])
        else:
            raise ArgumentError("Invalid argument for load_image()")

    #loads file path in read
    def load_file(file_path):

        with open(file_path, 'r') as f:
            return f.read()

    #loads typescript data files
    def load_ts_file(file_path):
        # parses the json data out of ts file (used for typechecking database)
        raw_string = Util.load_file(file_path)
        return json.loads(re.search("=\s*(\{(.|\n)+\})", raw_string).groups()[0])

    #plays music and loops
    def play_music():
        pygame.mixer.music.load('media/audio/calm_music.mp3')
        pygame.mixer.music.play(-1)  # plays and loops music infinitely
        pygame.mixer.music.set_volume(0.6)
