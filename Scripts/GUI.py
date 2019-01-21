"""
The following GUI Framework was borrwed from: Meloonatic Melons, Harry Hitchen
This source was referred to me by my brother, Sufiyaan Nadeem.

This is a program helps me make buttons, with text and tags (that I access from my main program),
and allows the user to interact with them, with a hover-over functionality. 

Given that this is a small part of my game's functionality and a multistep process complex, creating 
this GUI framework myself would take too long and be unnecessary.

Modified and commented by: Suhana Nadeem
"""

import pygame 

pygame.init() # Initializing all pygame functionalities.

Lime = (0, 255, 0) # Defining the colour needed.

# This function locates the position of the mouse on the screen, and checks if the mouse touches the button rectangles.
def MouseOver(rect):
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > rect[0] and mouse_pos[0] < rect[0] + rect[2] and mouse_pos[1] > rect[1] and mouse_pos[1] < rect[1] + rect[3]:
        return True
    else:
        return False

# This class defines the default font that I will be using.
class Font:
    Default = pygame.font.SysFont("Neucha", 45)

class Menu:

    class Button:

        # All the buttons will go in this list.
        All = []

        def __init__(self, text, rect, bg, fg, bgr, font=Font.Default, tag=("Menu", None)):
            self.Text = text
            self.Left = rect[0]
            self.Top = rect[1]
            self.Width = rect[2]
            self.Height = rect[3]
            self.Command = None
            self.Rolling = False # Keeps track of whether or not the user has engaged the method.
            self.Tag = tag

            # Original button.
            self.Normal = pygame.Surface(
                (self.Width, self.Height), pygame.HWSURFACE | pygame.SRCALPHA)
            self.Normal.fill(bg)
            RText = font.render(text, True, fg) # Creating the text.
            txt_rect = RText.get_rect() # Creating the surface rectangle. 
            self.Normal.blit(RText, (self.Width / 2 - txt_rect[2] / 2, self.Height / 2 - txt_rect[3] / 2)) 

            # Hovered-over button.
            self.High = pygame.Surface(
                (self.Width, self.Height), pygame.HWSURFACE | pygame.SRCALPHA)
            self.High.fill(bgr)
            self.High.blit(
                RText, (self.Width / 2 - txt_rect[2] / 2, self.Height / 2 - txt_rect[3] / 2))

            # Saving the button.
            Menu.Button.All.append(self)

        # Rendering the button to the screen, based on the dimensions provided.
        def Render(self, to, pos=(0, 0)):
            if MouseOver((self.Left + pos[0], self.Top + pos[1], self.Width, self.Height)):
                to.blit(self.High, (self.Left + pos[0], self.Top + pos[1]))
                self.Rolling = True
            else:
                to.blit(self.Normal, (self.Left + pos[0], self.Top + pos[1]))
                self.Rolling = False

    class Text:

        # All the text will go in this list.
        All = []

        # The text is created with set properties (colour, etc.), which I will use when creating the math.
        def __init__(self, text, font=Font.Default, color=Lime, bg=None):
            self.Text = text
            self.LastText = text
            self.Font = font
            self.Color = color
            self.Left = 0
            self.Top = 0
            self.Bg = bg

            # This process of creating a bitmap allows for dynamic text rendering, which means I can change the text on the same surface (button).
            bitmap = font.render(text, True, color)
            self.Bitmap = pygame.Surface(
                bitmap.get_size(), pygame.SRCALPHA | pygame.HWSURFACE)
            if bg != None:
                self.Bitmap.fill(bg)
            self.Bitmap.blit(bitmap, (0, 0))

            self.Width = self.Bitmap.get_width()
            self.Height = self.Bitmap.get_height()

        def Render(self, to, pos=(0, 0)):
            if self.Text != self.LastText:
                # If I change the text in my buttons...
                self.LastText = self.Text

                # Recreating the Bitmap to render new text.
                bitmap = self.Font.render(self.Text, True, self.Color)
                self.Bitmap = pygame.Surface(
                    bitmap.get_size(), pygame.SRCALPHA | pygame.HWSURFACE)
                if self.Bg != None:
                    self.Bitmap.fill(self.Bg)
                self.Bitmap.blit(bitmap, (0, 0))

                self.Width = self.Bitmap.get_width()
                self.Height = self.Bitmap.get_height()

            to.blit(self.Bitmap, (self.Left + pos[0], self.Top + pos[1]))

    class Image:
        # Defining the image of my buttons.
        def __init__(self, bitmap, pos=(0, 0)):
            self.Bitmap = bitmap
            self.Left = pos[0]
            self.Top = pos[1]
            self.Height = bitmap.get_height()
            self.Width = bitmap.get_width()

        # Blitting the Bitmap image to the screen.
        def Render(self, to, pos=(0, 0)):
            to.blit(self.Bitmap, (self.Left + pos[0], self.Top + pos[1]))