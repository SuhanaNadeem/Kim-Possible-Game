"""
These are my Game Object sprites
"""

import pygame

WIN_WIDTH = 960
WIN_HEIGHT = 540

class GameObject_Sprites:
    image = pygame.image.load("Graphics/coin.png")
    image = pygame.transform.scale(image, (16, 16))
    coin = image

    image = pygame.image.load("Graphics/DoorOpen.png")
    image = pygame.transform.scale(image, (58, 96))
    Door_Open = image