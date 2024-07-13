#Project Name: The Great Ship Escape
#Members: Eric Xu, Michael Gao, William Liu, Andrew Wang
#Date: 5/9/2022
#Description: File for initiating game attributes and holding global variables. 

from ctypes import util
import string
import pygame
from pygame.locals import *

from util import Util
import CONSTS
from player import Player
from room import Room
import sys
from dialog import Dialog


class Game():
    '''
    Manages pygame <> Player <> Level <> Dialog interactions
    '''

    def __init__(self):
        #Defining game attributes
        self.screen = pygame.display.set_mode(CONSTS.size)
        self.cur_frame = 0
        self.player = Player()
        self.clock = pygame.time.Clock()
        self.dialog = Dialog()
        self.overlay_surface = pygame.Surface(CONSTS.size, pygame.SRCALPHA,
                                              32)  # where do we put this; handles stationary UI components
        self.keys_pressed = []
        self.room_cache = {} #saves data of previously entered rooms
        self.end = "ongoing"
    #Plays music
    def play_music(self):
        Util.play_music()
    #Creates dialog box with text
    def summon_dialog(self, txt, callback=None, options=None):
        if type(txt) == type(""):
            txt = [txt] 
        self.dialog = Dialog(txt, callback, options)
    #Sets up the room
    def setup_room(self, room: string):
        if hasattr(self, "cur_room"):
            self.room_cache[self.cur_room.room_name] = self.cur_room
            self.cur_room.begin_transition(room)
        else:
            self.cur_room = Room(room)
    #Ends the game 
    def game_over(self):
        self.end = "over"
        self.end_start = self.cur_frame

    def loop(self):

        while True:
            #Global event variables
            self.keys_pressed = [] #keys pressed at this current iteration

            self.screen.fill((0, 0, 0))
            self.overlay_surface.fill(CONSTS.TRANSPARENT)
            #Processes keys
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.keys_pressed.append(event.unicode)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.keys_pressed.append("mouse")
            if not (self.cur_room.next_room_name):
                self.player.update_player_state() #includes inventory status.
                
            else:
                self.player.stop()

            
            #Render inventory and update layers of the game. 
            self.player.inventory.render()
            self.cur_room.update_layers()

            #If space key is pressed then process collisions
            if ' ' in self.keys_pressed and not self.dialog.dialog_active():
                self.player.process_collisions()

            self.dialog.update_and_display_dialog()

            #draw everything
            dx, dy = self.cur_room.calc_offset()
            self.screen.blit(self.cur_room.all_layers, [dx, dy])
            self.screen.blit(self.overlay_surface,(0,0))

            self.clock.tick_busy_loop(30)
            # print(self.clock.get_fps())
            pygame.display.update()

            # Update rooms if necessary
            if self.cur_room.gone:
                # If current room has dimmed to 0, switch to next one
                next_room = self.cur_room.next_room_name
                if next_room in self.room_cache.keys():
                    self.cur_room = self.room_cache[next_room]
                    self.cur_room.reset()
                else:
                    self.cur_room = Room(self.cur_room.next_room_name)
            self.cur_frame += 1
            #Ending the game. 
            if self.end == "over":
                if self.cur_frame == self.end_start+1:
                    print("Game over in 5 seconds.")
                if self.cur_frame - self.end_start > 150:
                    pygame.quit()
                    sys.exit()

