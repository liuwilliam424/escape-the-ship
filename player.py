#Project Name: The Great Ship Escape
#Members: Eric Xu, Michael Gao, William Liu, Andrew Wang
#Date: 5/9/2022
#Description: File for player attributes, movement, and animation

import pygame
import g
from pygame.locals import *
import numpy
from inventory import Inventory
from util import Util

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    WIDTH, HEIGHT = SIZE = (90, 180)

    def __init__(self):
        super().__init__()

        self.surf = pygame.Surface(self.SIZE, pygame.SRCALPHA, 32)
        self.skin = Util.load_image(
            'media/main_char/default.png', self.WIDTH, self.HEIGHT)
        self.surf.blit(self.skin, (0, 0))
        self.rect = self.surf.get_bounding_rect()

        self.vel = vec(0, 0)
        self.acc = vec(0, 3.4)
        self.jump_loop = 0
        self.inventory = Inventory()
        

    def check_collision(self, x, y):
        self.rect.move_ip([x, y])
        collide = pygame.sprite.spritecollideany(self, g.game.cur_room.borders)
        self.rect.move_ip([-x, -y])
        return collide

    def update_player_state(self):
        # handles player movement and inventory status
        self.move()
        self.inventory.update_status(self)

    def move(self):
        ACC = 2.4
        FRIC = -.15

        pressed_keys = pygame.key.get_pressed()
        # print(self.vel, self.acc)
        self.acc.x = 0
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.acc.x += -ACC
            self.skin = Util.load_image(
                'media/main_char/run_left' + str(int(g.game.cur_frame % 6<3)) + '.png', self.WIDTH, self.HEIGHT)
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.acc.x += ACC
            self.skin = Util.load_image(
                'media/main_char/run_right' + str(int(g.game.cur_frame % 6<3)) + '.png', self.WIDTH, self.HEIGHT)

        if not (pressed_keys[K_RIGHT] or pressed_keys[K_LEFT] or pressed_keys[K_a] or pressed_keys[K_d]):
            self.skin = Util.load_image(
                'media/main_char/default.png', self.WIDTH, self.HEIGHT)

        self.surf = self.skin
        # print(self.surf.get_rect().w)
        if(self.on_ground()):
            self.jump_loop = 0  # reset jumping

        if (pressed_keys[K_UP] or pressed_keys[K_w]) and self.jump_loop < 5:
            self.vel.y -= 9
            self.jump_loop += 1

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        delt = self.vel + 0.5 * self.acc
        sy = numpy.sign(delt.y)
        sx = numpy.sign(delt.x)

        while sy != 0 and self.check_collision(0, delt.y):
            delt.y -= sy
            self.vel.y = 0
        while sx != 0 and self.check_collision(delt.x, 0):
            delt.x -= sx
            self.vel.x = 0
        self.rect.move_ip(delt.x, delt.y)

    def stop(self):
        self.vel = vec(0, 0)

    # def update(self, delt):
    #     self.rect.move_ip(delt.x, delt.y)
    #     global borders
    #     hits = pygame.sprite.spritecollide(self, borders, 0)
    #     if (hits):
    #         self.vel.y = 0
    #         self.rect.midbottom = (self.rect.midbottom[0], hits[0].rect.top)

    def process_collisions(self):
        collisions = pygame.sprite.spritecollide(
            self, g.game.cur_room.interactables, False)
        for obj in collisions:
            needs_item = obj.data.get("needs")
            if needs_item:
                item = needs_item["object"]
                dialog = needs_item.get("dialog")
                reverse = needs_item.get("reverse")
                stop_action = not self.inventory.has(item)
                if reverse:
                    stop_action = not stop_action

                if stop_action:
                    g.game.summon_dialog(dialog or f"You're missing the item {item}!")
                    continue
            obj.activate()

    def on_ground(self):
        return self.rect.bottom == g.game.cur_room.height
