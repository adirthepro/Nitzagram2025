import pygame
from helpers import *
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from buttons import *
from ImagePost import ImagePost
from TextPost import TextPost
from Images import *

def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    img1 = ImagePost("username","Israel","Noa Kirel in Israel", 0, [],"Images/noa_kirel.jpg")
    txt1=TextPost("username","Israel","text",0,[],"Project",(0,0,255),(0,255,255))
    img2=ImagePost("username","Israel","Ronaldo is the goat",0,[],"Images/ronaldo.jpg")
    list_of_posts=[img1,txt1,img2]
    i=0
    running = True

    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(like_button,event.pos):
                    list_of_posts[i].add_like()
                else:
                    if i==2:
                        i=0
                    else:
                        i+=1



        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        list_of_posts[i].display()
        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
