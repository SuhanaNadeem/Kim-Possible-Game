"""
This program loads, scales, and sets the image of my coin game object sprites (which isn't animated). I 
will simply access this from the Game program when I want to display coins to the screen. I didn't do 
this with the door because I use it in my levels as a platform.

By: Suhana Nadeem
"""

import pygame

class Coin_Sprite(object):

    # I will set the image of the coin game object using the variable "coin", so it will already be loaded and scaled, in the Game program.

    image = pygame.image.load("Graphics/coin.png") # Accessing the coin image from the graphics folder.
    image = pygame.transform.scale(image, (16, 16))
    coin = image