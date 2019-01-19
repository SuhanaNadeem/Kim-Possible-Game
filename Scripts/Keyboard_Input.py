"""
This file has a basic function that handles the user's keyboard inputs. It changes the values of 
some of my Globals variables depending on the key the user presses.
"""

import pygame
# Importing everything from pygame.
from Globals import *

# This is the function that is used in the Game program to respond to game events.
def KeyInput_Handler(event):
    if event.type == pygame.KEYDOWN:
        # If a key is pressed...
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
        # If a key is released...
        if event.key == pygame.K_UP:
            Globals.up = False
        if event.key == pygame.K_DOWN:
            Globals.down = False
        if event.key == pygame.K_RIGHT:
            Globals.right = False
        if event.key == pygame.K_LEFT:
            Globals.left = False