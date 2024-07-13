#Project Name: The Great Ship Escape
#Members: Eric Xu, Michael Gao, William Liu, Andrew Wang
#Date: 5/9/2022
#Description: File for rooms, background transition, and player movement. 

import json
import pygame
from math import floor
from util import Util
import g
from interactables import *
from CONSTS import *
from border import Border
import re



class Room():
    # walls just beyond the boundary of the screen to keep the player in the room
    wall_thickness = 10

    def init_background(self, backgrounds):
        for i in range(len(backgrounds)):
            self.background_layer.blit(Util.load_image(
                backgrounds[i], floor(self.width/len(backgrounds)), self.height), [i*self.width/len(backgrounds), 0])

    def begin_transition(self, room):
        if self.next_room_name:
            return  # there's already a next room being transitioned to
        self.init_frame = g.game.cur_frame
        self.next_room_name = room
        self.last_player_location = g.game.player.rect.bottomleft

    def init_interactable(self, data):
        data["pos"][1] = self.height-data["pos"][1]
        if data.get("use"):
            obj_type = data["use"]["type"]
            if obj_type == "portal":
                return Portal(data)
            if obj_type =="tool":
                return Tool(data)
            if obj_type == "faucet":
                return Faucet(data)
            if obj_type == "trap":
                return Trap(data)
            raise TypeError(
                "you have invalid interactable object type "+obj_type)
        else:
            return Interactable(data)

    

    def update_layers(self):
        '''
        Updates all interactables and draws all layers (including background, objects, and character) on all_layers Surface
        '''
        opacity = min(255, (g.game.cur_frame-self.init_frame)*20)
        if self.next_room_name:  # if a next room exists, fade out instead of fade in
            opacity = 255-opacity
            if opacity == 0:
                self.gone = True

        self.active_layer.fill(TRANSPARENT)
        self.interactables.update()
        self.interactables.draw(self.active_layer)
        if not self.next_room_name:
            self.active_layer.blit(g.game.player.surf, g.game.player.rect)
        self.all_layers.fill(TRANSPARENT)
        self.all_layers.blit(self.background_layer, [0, 0])
        self.all_layers.blit(self.active_layer, [0, 0])

        self.all_layers.set_alpha(opacity)


    def reset(self):
        '''
        Resets room (while keeping the essentials) for future use
        '''
        self.gone = False
        self.next_room_name = None
        self.init_frame = g.game.cur_frame
        g.game.player.rect.bottomleft = self.last_player_location
        
    def add_interactable(self,data):
        self.interactables.add(self.init_interactable(data))
    
    def __init__(self, room):
        map_data = Util.load_ts_file(f"rooms/{room}.ts")
        self.room_name = room
        self.next_room_name = None
        self.gone = False  # completed transition to next room
        self.last_player_location = None  # saves player location upon room exit

        self.init_frame = g.game.cur_frame

        self.width = map_data["width"]
        self.height = map_data["height"]

        self.borders = pygame.sprite.Group()
        self.interactables = pygame.sprite.Group()

        self.background_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA,
                                               32)  # borders, background, etc. (stuff that don't change)
        self.active_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA,
                                           32)  # characters, objects, etc. (stuff that can change I guess)
        self.all_layers = pygame.Surface([self.width, self.height], pygame.SRCALPHA,
                                         32)
        self.init_background(map_data["background"])
        self.init_walls(map_data.get("borders"))


        g.game.player.rect.bottomleft = (
            map_data["player_x"],self.height - map_data["player_y"])

        for obj in map_data.get("objects") or []:
            if obj.get("inherit"):
                inherited_obj = obj["inherit"]
                file_path = f"rooms/objects/{inherited_obj}.ts"
                extra_data = Util.load_ts_file(file_path)
                extra_data.update(obj)
                obj = extra_data
            self.add_interactable(obj)


        # self.borders.draw(self.background_layer) (hide borders; not sure if this is necessary)

        if "dialog" in map_data:
            g.game.summon_dialog(map_data["dialog"])

    def init_wall(self, w, h, cx, cy):
        self.borders.add(Border((w, h), (cx, cy)))

    def init_walls(self,borders):
        # inits room with top left corner on top left of screen
        w, h = self.width, self.height
        cx = w / 2
        cy = h / 2
        self.init_wall(w + self.wall_thickness * 2,
                       self.wall_thickness, cx, cy + h / 2 + self.wall_thickness / 2)
        self.init_wall(w + self.wall_thickness * 2,
                       self.wall_thickness, cx, cy - h / 2 - self.wall_thickness / 2)
        self.init_wall(self.wall_thickness, h, cx +
                       (w + self.wall_thickness) / 2, cy)
        self.init_wall(self.wall_thickness, h, cx -
                       (w + self.wall_thickness) / 2, cy)
        if borders:
            for border in borders:
                self.init_wall(self.wall_thickness,h,border+self.wall_thickness//2,cy)
    def calc_offset(self):
        x = g.game.player.rect.centerx
        dx = -min(max(x - SCREEN_WIDTH / 2, 0), self.width - SCREEN_WIDTH)
        if self.width < SCREEN_WIDTH:
            dx = (SCREEN_WIDTH-self.width)/2
        return (dx, (SCREEN_HEIGHT-self.height)/2)
