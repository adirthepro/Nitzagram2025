from classes import Post
import pygame
from constants import *
from helpers import *

class Comment:
    def __init__(self,text):
        font=pygame.font.SysFont('chalkduster.ttf',COMMENT_TEXT_SIZE)
        self.text=font.render(text,True,BLACK)

    def display_comment(self):

        self.display_comment()


