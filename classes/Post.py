import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """

    def __init__(self, username, location, description, likes_counter):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = likes_counter
        self.comments = []
        self.comments_display_index = 0

    def add_like(self):
        self.likes_counter+=1

    def add_comment(self,text):
        if isinstance(self.comments,list):
            self.comments.append(text)

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        #username
        font=pygame.font.SysFont('chalkduster.ttf',UI_FONT_SIZE)
        text_username = font.render(self.username,True,BLACK)
        screen.blit(text_username,[USER_NAME_X_POS,USER_NAME_Y_POS])
        #location
        text_location=font.render(self.location,True,BLACK)
        screen.blit(text_location,[LOCATION_TEXT_X_POS,LOCATION_TEXT_Y_POS])
        #likes
        text_likes=font.render(self.likes_counter,True,BLACK)
        screen.blit(text_likes,[LIKE_TEXT_X_POS,LOCATION_TEXT_Y_POS])
        #description
        text_description=font.render(self.description,True,BLACK)
        screen.blit(text_description,[DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS])
        #comments
        self.display_comments()

        # TODO: write me!


    def display_username(self):
        font = (pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE))
        text_username = font.render(self.username, True, BLACK)
        screen.blit(text_username, [USER_NAME_X_POS, USER_NAME_Y_POS])
    def display_location(self):
        font = (pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE))
        text_location = font.render(self.location, True, BLACK)
        screen.blit(text_location, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])
    def display_likes(self):
        font = (pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE))
        text_likes = font.render(f"this post has {self.likes_counter} likes", True, BLACK)
        screen.blit(text_likes, [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS])
    def display_description(self):
        font = (pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE))
        text_description = font.render(self.description, True, BLACK)
        screen.blit(text_description, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                #position_index = 0
                break
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



