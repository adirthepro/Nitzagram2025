from classes.Post import *
import pygame
from constants import *
from helpers import *

class Comment:
    def __init__(self):
        self.text=read_comment_from_user()

    def display_comment(self):
        font=pygame.font.SysFont('chalkduster.ttf',COMMENT_TEXT_SIZE)
        txt=font.render(self.text,True,BLACK)
        screen.blit(txt,[FIRST_COMMENT_X_POS,FIRST_COMMENT_Y_POS])




