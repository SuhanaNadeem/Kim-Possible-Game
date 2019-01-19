"""
Making the buttons to be used on different screens, and defining functions for each
of them. These will be accessed in the game program using the Tags.

This was simple to code because of the GUI program - it is essentially creating and customizing instances of the buttons class.

By: Suhana Nadeem
"""

# Importing functionality (variables, classes, functions) from my Globals program, the GUI program, and pygame.
import pygame
from Globals import *
from Scripts.GUI import *

# Creating a Buttons class with all the commands available to them.
class Buttons(object):

    def Play_Menu():
        # Perform tasks defined for the Instructions screen.
        Globals.scene = "Instructions"

    def Exit():
        # Stop gameplay.
        pygame.mixer.music.stop() # Stop playing the music.
        Globals.isRunning = False # The game has stopped running.
    
    def Play_Instructions():
        # Perform tasks defined for the Game screen (initate gameplay).
        Globals.scene = "Game"

"""
The following buttons are made through the GUI program I borrowed. Each button is an instance of 
the Button class inside of the Menu class (Menu.Button), and each button has text, a surface size (rect),
a defined foreground colour, a defined background colour, and a tag tuple. The tag is important because it
represents where my button will be displayed. 
"""

# Defining the window width and height for reference.
WIN_WIDTH = 960
WIN_HEIGHT = 540

# Play button that will go on the Instructions screen, and make the screen Game (initiates gameplay).
btnPlay_Instructions = Menu.Button(text="START", rect=(0, 0, 150, 75),
                      bg=UltraColor.Fog, fg=UltraColor.White, bgr=UltraColor.Green, tag=("Instructions", None))
# The above is creating an instance of the class.
btnPlay_Instructions.Left = 215 # Defining the x-axis position of the button (from the left)
btnPlay_Instructions.Top = WIN_HEIGHT - 120 # Defining y-axis position of the button (from the top)
btnPlay_Instructions.Command = Buttons.Play_Instructions # Defining the command of the button as I defined in the Buttons class above.

# Play button that will go on the Menu screen, and make the screen Instructions (displays the instructions).
btnPlay_Menu = Menu.Button(text="PLAY", rect=(0, 0, 150, 75),
                      bg=UltraColor.Fog, fg=UltraColor.White, bgr=UltraColor.Green, tag=("Menu", None))
btnPlay_Menu.Left = 525
btnPlay_Menu.Top = WIN_HEIGHT - 230
btnPlay_Menu.Command = Buttons.Play_Menu

# Exit button that will go on the Menu screen, and exit the game.
btnExit = Menu.Button(text="EXIT", rect=(0, 0, 150, 75), bg=UltraColor.Fog,
                      fg=UltraColor.White, bgr=UltraColor.Green, tag=("Menu", None))
btnExit.Left = btnPlay_Menu.Left + 200
btnExit.Top = btnPlay_Menu.Top 
btnExit.Command = Buttons.Exit

# Exit button that will go on the GameOver screen, and exit the game.
btnExit2 = Menu.Button(text="EXIT", rect=(0, 0, 160, 60), bg=UltraColor.Fog,
                       fg=UltraColor.White, bgr=UltraColor.Green, tag=("GameOver", None))
btnExit2.Left = WIN_WIDTH - 244
btnExit2.Top = WIN_HEIGHT - 320
btnExit2.Command = Buttons.Exit