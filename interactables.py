#Project Name: The Great Ship Escape
#Members: Eric Xu, Michael Gao, William Liu, Andrew Wang
#Date: 5/9/2022
#Description: File for interactables, object uses, and player interaction. 

import pygame
from util import Util
import g

class Interactable(pygame.sprite.Sprite):
    DEFAULT = 0
    HOVER = 1
    ACTIVE = 2

    def __init__(self, data):
        super().__init__()
        #Interactable attributes
        self.data = data
        self.dialog_shown = False
        #Image of the Interactable
        img_urls = data["images"]
        size = data["size"]
        pos = data["pos"]
        self.one_way_image_states = data.get("one_way_animation") or []
        #Creates 3 different image states.
        for _ in range(3-len(img_urls)):
            img_urls.append([])
        for i in range(3):
            if(type(img_urls[i]) != type([])):
                img_urls[i] = [img_urls[i]]  # make it a single array
        
        self.images = [[Util.load_image(
            img_url, size) for img_url in img_urls[i]] for i in range(len(img_urls))]
        for i in range(1, 3):
            self.images[i] = self.images[i] or self.images[i-1]
        # pos is relative to bottom left corner (origin)
        self.image_index = 0
        self.image_state = self.DEFAULT
        self.image = self.images[self.image_state][self.image_index]

        self.activation_timeout = 10  # number of frames before no longer active
        self.active_frame = -1
        #Gets area and position of the image
        self.rect = self.image.get_rect(bottomleft=(pos[0], pos[1]))

    def update(self):
        '''
        Updates image based on its current state
        '''
        img_index_delta = 1
        
        prev_image_state = self.image_state
        #If the player collides with the interactable
        if pygame.sprite.collide_rect(self, g.game.player):
            #Update the image
            if self.active_frame != -1 and g.game.cur_frame-self.active_frame <= self.activation_timeout:
                self.image_state = self.ACTIVE
            else:
                self.image_state = self.HOVER
        else:
            self.image_state = self.DEFAULT

        if prev_image_state != self.image_state:
            if prev_image_state in self.one_way_image_states and self.image_index > 0:
                # reset previous state first
                img_index_delta = -1
                self.image_state = prev_image_state
            else:
                self.image_index = 0

        self.image = self.images[self.image_state][self.image_index]
        image_length = len(self.images[self.image_state])
        self.image_index = (self.image_index+img_index_delta) % image_length
        if self.image_state in self.one_way_image_states:
            # basically prevent the index from going back
            if img_index_delta == 1 and self.image_index == 0:
                self.image_index = image_length-1
    #The Interactable performs an action
    def activate(self,show_dialog = True):
        if self.data.get("dialog") and show_dialog:
            if not (self.data.get("dialog_once") and self.dialog_shown):

                g.game.summon_dialog(self.data["dialog"])
                self.dialog_shown = True
        
        self.active_frame = g.game.cur_frame
#Subclass of Interactable for pickapable tools
class Tool(Interactable):
    def __init__(self, data):
        super().__init__(data)
        
        self.name = data["name"]
    #The tool is added to the inventory
    def activate(self):
        if g.game.player.inventory.add(self.name):
            self.kill()
            super().activate()
        else:
            g.game.summon_dialog("Your inventory is full!")
#Subclass of Interactable for portals to go to different rooms/floors
class Portal(Interactable):
    def __init__(self, data):
        super().__init__(data)
        self.activation_timeout = 100  # don't make it unactivate
        self.use_data = data["use"]
        self.dest = self.use_data["dest"]
    def onKeyReturn(self,key):
        g.game.setup_room(key)
        return super().activate()
    #Brings player to different room
    def activate(self):
        if type(self.dest) == type({}):
            if self.dest.get("object"):
                obj = self.dest["object"]
                dests = self.dest["dest"]
                dest = dests[g.game.player.inventory.has(obj)]
                g.game.setup_room(dest)
                return super().activate()

            else:
                dialog = self.dest["prompt"].copy()
                keys = ", ".join(self.dest["options"].keys())
                dialog[0]+=(f" Press any of the following keys: {keys}")
                g.game.summon_dialog(dialog,self.onKeyReturn,self.dest["options"])
        else:
            g.game.setup_room(self.dest)
            return super().activate()

#Allows player to pick up an object.
class Faucet(Interactable):
    def __init__(self, data):
        super().__init__(data)
        use_data = data["use"]
        self.has_object = True
        self.object_name = use_data["object"]
        self.failed_dialog = use_data.get("inventory_full_statement") or "There's something here, but your inventory is full."
    #Adds object in Faucet to inventory. 
    def activate(self):
        if self.has_object:
            if g.game.player.inventory.add(self.object_name):
                
                self.has_object = False
                return super().activate()
            else:
                g.game.summon_dialog(self.failed_dialog)
        return super().activate(False)
#Subclass of Interactable that ends game. 
class Trap(Interactable):
    def __init__(self, data):
        super().__init__(data)
        self.use_data = data["use"]
        self.when = self.use_data["when"]
        self.touching = False
    #Detects if player touches trap.
    def update(self):
        super().update()
        if self.when == "immediate":
            if self.touching == False:
                if pygame.sprite.collide_rect(self, g.game.player):
                    super().activate()
                    g.game.game_over()
                    self.touching = True
                else:
                    self.touching = False
    #Ends game
    def activate(self):
        super().activate()
        g.game.game_over()