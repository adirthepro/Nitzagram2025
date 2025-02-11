from classes.Post import *
import pygame
from constants import *
from helpers import screen


class ImagePost(Post):
    def __init__(self, username, location, description, likes_counter, comments,image):
        super().__init__(username, location, description, likes_counter, comments)
        img=pygame.image.load(image)
        self.img=pygame.transform.scale(img,(POST_WIDTH,POST_HEIGHT))

    def display(self):
        super().display_username()
        super().display_location()
        super().display_likes()
        super().display_description()
        super().display_comments()

        screen.blit(self.img,(POST_X_POS,POST_Y_POS))

