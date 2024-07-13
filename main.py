#Project Name: The Great Ship Escape
#Members: Eric Xu, Michael Gao, William Liu, Andrew Wang
#Date: 5/9/2022
#Description: File for running the game. 

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "" # placed in beginning after os, but before pygame imports in order to prevent pygame community from saying hello
import pygame
from game import Game
import g

# start the program
pygame.init()
# icons of ship
icon = pygame.image.load('media/boaticon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('The Great Ship Escape!')

game = Game()
g.game = game #So that other files can access the game obj (and its properties) without circular imports

# playing music
game.play_music()
game.setup_room("room114")
game.loop()

