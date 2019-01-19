"""
This program loads, scales, and sets the image of two of my game object sprites (which aren't animated),
the coin and the open door. I will simply access them from the Game program when I want to display 
them to the screen. I didn't do this with the closed door because I use it in my levels as a platform.

By: Suhana Nadeem
"""

import pygame

class GameObject_Sprites(object):

    # I will set the images of the corresponding game objects using the variables "coin" and "Door_Open", so they will already be loaded and scaled, in the Game program.

    image = pygame.image.load("Graphics/coin.png") # Accessing the coin image from the graphics folder.
    image = pygame.transform.scale(image, (16, 16))
    coin = image

    image = pygame.image.load("Graphics/DoorOpen.png") # Accessing the DoorOpen image from the graphics folder.
    image = pygame.transform.scale(image, (58, 96))
    DoorOpen = image