"""
This file has a function that handles the user's keyboard inputs. It updates the values of 
some of my Globals variables depending on the key the user presses and releases. Events from the Game
program are passed to this function, and the updated variables are then used to control Kim's movement.

By: Suhana Nadeem
"""

import pygame
# Importing everything from pygame.
from Globals import *

# This is the function that is used in the Game program to respond to game events.
def KeyInput_Handler(event):
    # If a key is pressed, certain variables will be updated depending on which key is pressed.
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            Globals.up = True
        if event.key == pygame.K_DOWN:
            Globals.down = True
        if event.key == pygame.K_LEFT:
            Globals.left = True
        if event.key == pygame.K_RIGHT:
            Globals.right = True

    # Otherwise, if a key is released, certain variables will be updated depending on which key is released.
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            Globals.up = False
        if event.key == pygame.K_DOWN:
            Globals.down = False
        if event.key == pygame.K_RIGHT:
            Globals.right = False
        if event.key == pygame.K_LEFT:
            Globals.left = False