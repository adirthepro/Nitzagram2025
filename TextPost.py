from classes.Post import *
import pygame
from constants import *
from helpers import screen

class TextPost(Post):
    def __init__(self, username, location, description, likes_counter,text,text_color,background_color):
        super().__init__(username, location, description, likes_counter)
        font=pygame.font.SysFont('chalkduster.ttf',TEXT_POST_FONT_SIZE)
        self.text=font.render(text,True,text_color)
        self.background_color=background_color

    def display(self):
        square= pygame.Rect(POST_X_POS,POST_Y_POS,POST_WIDTH,POST_HEIGHT)
        pygame.draw.rect(screen,self.background_color,square)
        left_space = (POST_WIDTH - self.text.get_width()) / 2
        up_space=(POST_HEIGHT-self.text.get_height())/2

        screen.blit(self.text,(POST_X_POS + left_space,POST_Y_POS+up_space))
        super().display_username()
        super().display_location()
        super().display_likes()
        super().display_description()
        super().display_comments()
