#Project Name: The Great Ship Escape
#Members: Eric Xu, Michael Gao, William Liu, Andrew Wang
#Date: 5/9/2022
#Description: File for dialog box generation and text updating

from itertools import accumulate
import pygame
from CONSTS import SCREEN_HEIGHT, SCREEN_WIDTH
from pygame.locals import *
import g


class Dialog:
    def __init__(self, texts=[], callback=None, options=None):
        #constants for dialog box size
        self.SIZE = self.WIDTH, self.HEIGHT = (
            0.9 * SCREEN_WIDTH), (0.25 * SCREEN_HEIGHT)
        self.BORDER = 20
        self.TEXT_SPEED = 2
        
        self.font = pygame.font.Font(
            'media/ship_fonts/ShipporiMincho-Bold.ttf', 21) 

        #initializing instance variables for dialog box instance
        self.texts = list(map(self.parse, texts))
        self.text_array_index = 0
        self.text = [""] #current text
        self.displayed_text = [""]

        #render initial update of text
        self.update_text()

        self.textbox = None
        self.callback = callback
        self.options = options  # map of options
        # Don't render on first refresh; prevents [space] bar collisions
        self.first = True

    #process text for display
    def parse(self, txt: str):
        words = txt.split(" ")
        res = [""]
        for word in words:
            if len(res[-1]) == 0 or (self.font.size(res[-1]+word)[0] <= (self.WIDTH - (2 * self.BORDER))):
                res[-1] += word+" "
            else:
                res.append(word+" ")
        return res

    #changes text to relative to current frame
    def update_text(self, texts=None):
        # new array of text
        if texts:
            self.texts = texts
            self.text_array_index = 0
        if self.dialog_active():
            self.text = self.texts[self.text_array_index]
            self.displayed_text = [""]
            self.start_frame = g.game.cur_frame

    #clears text 
    def clear_text(self):
        self.texts = []
        self.text = None

    #checks if dialog is active
    def dialog_active(self):
        return len(self.texts) > 0

    #creates box that surrounds box
    def render_box(self):
        self.textbox = pygame.Surface(self.SIZE,pygame.SRCALPHA,32)
        self.textbox.fill((39, 44, 46))
        inside_dimensions = (
            self.WIDTH - self.BORDER), (self.HEIGHT - self.BORDER)
        pygame.draw.rect(self.textbox, (181, 193, 199),
                         ((self.BORDER/2, self.BORDER/2), inside_dimensions))
        
        self.render_text()

        # draw it onto the screen
        g.game.overlay_surface.blit(
            self.textbox, ((0.05 * SCREEN_WIDTH), (0.07 * SCREEN_HEIGHT)))
    
    #retrieve characters
    def _get_characters(self,txt):
        res = 0
        for t in txt:
            res+=len(t)
        return res

    #allow for multiple pages of text within dialog
    def next_text(self):
        if self._get_characters(self.displayed_text)==self._get_characters(self.text):

            self.text_array_index += 1
            if self.text_array_index <= len(self.texts)-1:
                self.update_text()
            else:
                self.clear_text()
                return False
        else:
            self.displayed_text=self.text
        return True
        
    #render text abstract function
    def render_text(self):
        
        self.bottom_text()
        self.render_main_text()

    #render written text with multiple rows with word wrap
    def render_main_text(self):

        for _ in range(self.TEXT_SPEED):
            row = len(self.displayed_text)-1
            if len(self.displayed_text[row])==len(self.text[row]):
                if row+1==len(self.text):
                    break
                row+=1
                self.displayed_text.append("")
            self.displayed_text[row]+=self.text[row][len(self.displayed_text[row])]
            
            
        for [row, txt] in enumerate(self.displayed_text):
            row_text = self.font.render(txt, True, (0,0,0))
            self.textbox.blit(row_text, (20, 10+23*row))

    #blinking bottom text
    def bottom_text(self):
        font = pygame.font.Font(
            'media/ship_fonts/ShipporiMincho-Regular.ttf', 15)

        if (g.game.cur_frame - self.start_frame) % 30 < 15:
            text = font.render("Press Space to Skip", False, (220, 100, 100))
            self.textbox.blit(text, (230, 84))

    #checks callback history
    def check_if_callback_activated(self):
        keys_pressed = g.game.keys_pressed

        for key in keys_pressed:
            if key in self.options.keys():
                self.callback(self.options[key])
                self.clear_text()
                return
                
    #updates text every frame to correct level of text
    def update_and_display_dialog(self):
        if self.first:
            self.first = False
        elif self.dialog_active():
            if ' ' in g.game.keys_pressed:
                if not self.next_text():
                    return
            self.render_box()
            if(self.options):
                self.check_if_callback_activated()
