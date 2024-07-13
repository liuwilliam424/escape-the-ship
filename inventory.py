#Project Name: The Great Ship Escape
#Members: Eric Xu, Michael Gao, William Liu, Andrew Wang
#Date: 5/9/2022
#Description: File for inventory generating, slot updating and adding

from copy import deepcopy
from util import MouseBox, Util
import pygame
import g
from pygame.locals import *
from CONSTS import *


class Inventory:
    # set up inventory variables
    INVENTORY_DIMENSIONS = INVENTORY_WIDTH, INVENTORY_HEIGHT = (370, 100)
    GRID_SIZE = 80
    MAX_SIZE = 4
    BORDER_WIDTH = 10
    POS = (int((SCREEN_WIDTH-INVENTORY_WIDTH)/2),
           SCREEN_HEIGHT-20-INVENTORY_HEIGHT)

    def drop_obj(self, pos, i):
        self.active_slot[i] = False
        # Configures additional attributes for Interactable initialization
        tool = deepcopy(self.slots[i].data)
        tool["use"] = {"type": "tool"}
        tool["pos"] = pos
        #Adds the tool as an interactable to the game environment. 
        g.game.cur_room.add_interactable(tool)

    def __init__(self):
        # setup slot dimensions
        self.slots = [None]*self.MAX_SIZE
        self.active_slot = [False]*self.MAX_SIZE

        # setup inventory background
        self.bg_image = Util.load_image(
            "media/inventory.png", self.INVENTORY_DIMENSIONS)
        self.active_box = Util.load_image(
            "media/inventory_spot.png", (self.GRID_SIZE, self.GRID_SIZE))
        self.show = False
        self.visible = False

        self.tool_data = Util.load_ts_file("meta/tools.ts")
        for [name, obj] in self.tool_data.items():
            obj["name"] = name  # for identification purposes

        # Intialize crafting data
        crafting_data_raw = Util.load_ts_file("meta/crafting.ts")
        self.crafting_data = {}
        for [b, a] in crafting_data_raw.items():
            self.crafting_data[frozenset(a)] = b
        #Setting up inventory space to be added to the front layer of the game. 
        self.bg_surface = pygame.Surface(self.INVENTORY_DIMENSIONS)
        self.bg_surface.blit(self.bg_image, (0, 0))
        self.bounding_boxes = pygame.sprite.Group()
        #Adding the tools to the inventory. 
        for i in range(self.MAX_SIZE):
            box_sprite = BoxSurface(self.GRID_SIZE, self.BORDER_WIDTH, i)
            self.bounding_boxes.add(box_sprite)
            self.bg_surface.blit(box_sprite.image, box_sprite.rect)

    def update_status(self, player):
        '''
        Updates status of inventory (currently handling only obj drops)
        from player location and key presses. 
        '''

        x = player.rect.left
        keys = g.game.keys_pressed
        #Show inventory when i is pressed.
        if 'i' in keys:
            self.show = not self.show
        if self.show:
            for key in keys:
                # key pressed might not be an int
                try:
                    i = int(key)-1
                    # Drops object when key between 1-4 is pressed. 
                    if i in list(range(self.MAX_SIZE)):
                        if self.slots[i]:  # if the slot exists
                            self.drop_obj([x, 10], i)
                            self.slots[i] = None
                except ValueError:
                    # key pressed was not a number
                    pass
            if "mouse" in keys:
                hit = pygame.sprite.spritecollideany(
                    MouseBox(self.POS), self.bounding_boxes)
                if hit:
                    i = hit.i
                    if self.slots[i]:
                        self.active_slot[i] = not self.active_slot[i]
            # crafting UI
            if 'c' in keys:
                selected_items = []
                for i in range(self.MAX_SIZE):
                    if self.active_slot[i]:
                        selected_items.append(self.slots[i].name)
                crafting_product = self.crafting_data.get(
                    frozenset(selected_items))
                if crafting_product:
                    # finished crafting and replace items
                    g.game.summon_dialog(f"You crafted a {crafting_product}!")
                    for i in range(self.MAX_SIZE):
                        if self.active_slot[i]:
                            self.active_slot[i] = False
                            self.slots[i] = None
                    self.add(crafting_product)
                else:
                    # detect for wrong recipe
                    g.game.summon_dialog("Invalid recipie!")

    def render(self):
        if not self.show:
            return

        # render inventory
        inventory_surface = pygame.Surface(
            self.INVENTORY_DIMENSIONS, pygame.SRCALPHA, 32)

        active_surface = pygame.Surface(
            self.INVENTORY_DIMENSIONS, pygame.SRCALPHA, 32)
        for i, tool in enumerate(self.slots):
            # top left of current inventory slot
            top_left = (int(self.BORDER_WIDTH+(self.BORDER_WIDTH +
                        self.GRID_SIZE)*i), int(self.BORDER_WIDTH))
            if self.active_slot[i]:
                active_surface.blit(self.active_box, top_left)
            if tool:
                (w, h) = tool.image.get_size()

                active_surface.blit(tool.image, (int(top_left[0]+(self.GRID_SIZE-w)/2),
                                                 int(top_left[1]+(self.GRID_SIZE-h)/2)))

        inventory_surface.blit(self.bg_surface, (0, 0))
        inventory_surface.blit(active_surface, (0, 0))

        g.game.overlay_surface.blit(inventory_surface, self.POS)

    def add(self, name):
        # add into inventory
        if not self.tool_data.get(name):
            g.game.summon_dialog(
                f"You've obtained the invalid object {name}! This should not happen")
            return
        #put the tool into the left-most empty slot 
        for i in range(self.MAX_SIZE):
            if self.slots[i] == None:
                # empty
                self.slots[i] = InventoryItem(self.tool_data[name])
                return True
        return False

    def has(self, name):
        '''
        Checks if item name is present in inventory
        '''
        #Iterates and searches through the list of items in inventory to 
        for i in range(self.MAX_SIZE):
            if self.slots[i] and self.slots[i].name == name:
                return True
        return False


class BoxSurface(pygame.sprite.Sprite):
    def __init__(self, GRID_SIZE, BORDER_WIDTH, i) -> None:
        # definition of box
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(LIGHT_BLUE)
        self.i = i  # identifies its position
        self.rect = self.image.get_rect()
        self.rect.topleft = (
            BORDER_WIDTH+(BORDER_WIDTH+GRID_SIZE)*i, BORDER_WIDTH)


class InventoryItem:
    # initiate variables
    OBJECT_SIZE = 60

    def __init__(self, data):
        self.data = data
        self.name = data["name"]
        self.image = Util.load_image(data["images"][0])
        w, h = self.image.get_size()
        scaling_factor = min(self.OBJECT_SIZE/w, self.OBJECT_SIZE/h)
        # math for box sizing
        w = int(w*scaling_factor)
        h = int(h*scaling_factor)
        self.image = pygame.transform.scale(self.image, (w, h))
        if not self.data.get("size"):
            self.data["size"] = [w, h]

    # def slotrender(self,display):
    # text = self.render(str(self.count), True, (0, 0, 0))
    #  display.blit(self.image, self.rect)
    #  display.blit(text, self.rect.midright)
