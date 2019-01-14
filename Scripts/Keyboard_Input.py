"""
Key Input Handler that decides what variables to set true depending on what keys are pressed.

"""

import pygame
from Globals import *


def KeyInput_Handler(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            Globals.isRunning = False
        if event.key == pygame.K_UP:
            Globals.up = True
        if event.key == pygame.K_DOWN:
            Globals.down = True
        if event.key == pygame.K_LEFT:
            Globals.left = True
        if event.key == pygame.K_RIGHT:
            Globals.right = True

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            Globals.up = False
        if event.key == pygame.K_DOWN:
            Globals.down = False
        if event.key == pygame.K_RIGHT:
            Globals.right = False
        if event.key == pygame.K_LEFT:
            Globals.left = False
