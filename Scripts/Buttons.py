"""
Creating Buttons and assigning functions for each button. 

Author: Suhana Nadeem
"""

import pygame
from Globals import *
from Scripts.GUI import *

class Buttons(object):
    def Play_Menu():
        Globals.scene = "Instructions"

    def Exit():
        pygame.mixer.music.stop()
        Globals.isRunning = False
    
    def Play_Instructions():
        Globals.scene = "Game" 

WIN_WIDTH = 960
WIN_HEIGHT = 540

# Play Button
btnPlay_Instructions = Menu.Button(text="START", rect=(0, 0, 150, 75),
                      bg=UltraColor.Fog, fg=UltraColor.White, bgr=UltraColor.Green, tag=("Instructions", None))
btnPlay_Instructions.Left = 215
btnPlay_Instructions.Top = WIN_HEIGHT - 120
btnPlay_Instructions.Command = Buttons.Play_Instructions

btnPlay_Menu = Menu.Button(text="PLAY", rect=(0, 0, 150, 75),
                      bg=UltraColor.Fog, fg=UltraColor.White, bgr=UltraColor.Green, tag=("Menu", None))
btnPlay_Menu.Left = 525
btnPlay_Menu.Top = WIN_HEIGHT - 230
btnPlay_Menu.Command = Buttons.Play_Menu

btnExit = Menu.Button(text="EXIT", rect=(0, 0, 150, 75), bg=UltraColor.Fog,
                      fg=UltraColor.White, bgr=UltraColor.Green, tag=("Menu", None))
btnExit.Left = btnPlay_Menu.Left + 200
btnExit.Top = btnPlay_Menu.Top 
btnExit.Command = Buttons.Exit

btnExit2 = Menu.Button(text="EXIT", rect=(0, 0, 160, 60), bg=UltraColor.Fog,
                       fg=UltraColor.White, bgr=UltraColor.Green, tag=("GameOver", None))
btnExit2.Left = WIN_WIDTH - 244
btnExit2.Top = WIN_HEIGHT - 320
btnExit2.Command = Buttons.Exit
