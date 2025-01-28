from classes import Post
import pygame
from constants import *
from helpers import screen

class TextPost(Post):
    def __init__(self, username, location, description, likes_counter, comments,text,text_color,background_color):
        super().__init__(username, location, description, likes_counter, comments)
        font=pygame.font.SysFont('chalkduster.ttf',TEXT_POST_FONT_SIZE)
        self.text=font.render(text,True,text_color)
        self.background_color=background_color

    def display(self):
        screen.fill(self.background_color)
        screen.blit(self.text,(0.5*POST_X_POS,0.5*POST_Y_POS))
        super().display_username()
        super().display_location()
        super().display_likes()
        super().display_description()
        super().display_comments()
