"""
Instead of having to crop each of my sprites from the spritesheet, I'm using this Sprite Mapping 
functionality. This is not used in the actual gameplay; just makes it easier for me to locate and size the 
sprites for Kim, from my spritesheet.

This code has been borrowed from: Sufiyaan Nadeem (https://github.com/SufiyaanNadeem/Ben-10-Game/blob/master/Scripts/Sprite_Mapping.py),
as adapted by Anthony Biron (https://www.youtube.com/watch?v=cSsurU0yFEw). 

As I mapped each of my sprites, this program wrote to two text files: KimPossibleSprite.txt and Kim_Animates.txt.
In KimPossibleSprite.txt, this program wrote what I used to locate and size the sprites in Kim_Sprites.py. 
In Kim_Animates.txt, this program wrote what I used in my animation loops in Game.py (runloop, etc.).

I edited what this program wrote to both the text files to customize it for my game. See Kim_Sprites.py 
and Game.py for my edits, and the two original text files (mentioned above) for more details.

Modified and commented by: Suhana Nadeem. 
"""

# Importing modules/functions needed. 
import pygame
from pygame import *
import sys

# Setting the window dimensions.
WIN_WIDTH = 768
WIN_HEIGHT = 672

# Setting the screen defaults.
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

# Loading the spritesheeet from the Graphics folder.
spritesheet = pygame.image.load("Graphics/KimSprites.png")

# Main function that carries out sprite mapping process.
def main():
    # Initializing variables and pygame, customizing window.
    isRunning = True
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Sprite Mapper")
    x = y = 0
    w = h = 100
    pygame.key.set_repeat(1, 30)
    counter = 0
    first = True

    # Handling KeyBoard inputs to "crop" each sprite.
    while isRunning:
        print(str(h))
        for e in pygame.event.get():

            if e.type == QUIT:
                isRunning = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                isRunning = False

            """

            The commands I kept in the program (the ones I used):
            'up' for moving the sprite map up,
            'down' for moving the sprite map down, 
            'z' for decreasing the height of the sprite map, 
            'x' for increasing the height of the sprite map,
            'c' for decreasing the width of the sprite map, and
            'v' for increasing the width of the sprite map.
            
            """

            if e.type == KEYDOWN and e.key == K_UP:
                y = y - 1
            if e.type == KEYDOWN and e.key == K_DOWN:
                y = y + 1
            if e.type == KEYDOWN and e.key == K_LEFT:
                x = x - 1
            if e.type == KEYDOWN and e.key == K_RIGHT:
                x = x + 1

            if e.type == KEYDOWN and e.key == K_z:
                h = h - 1
            if e.type == KEYDOWN and e.key == K_x:
                h = h + 1
            if e.type == KEYDOWN and e.key == K_c:
                w = w - 1
            if e.type == KEYDOWN and e.key == K_v:
                w = w + 1

            if e.type == KEYDOWN and e.key == K_q:
                counter = 0

            # Pressing the spacebar initiates writing to both the text files.
            if e.type == KEYDOWN and e.key == K_SPACE:
                name = input("Name of Sprite?")

                f = open("KimPossibleSprite.txt", "a") # Sprite details code - KimPossibleSprite.txt.

                savedcode = "character = pygame.Surface((" + str(w) + \
                    "," + str(h) + "),pygame.SRCALPHA)" + "\n"
                f.write(savedcode)

                savedcode = "character.blit(spritesheet,(" + \
                    str(x) + "," + str(y) + "))" + "\n"
                f.write(savedcode)

                savedcode = "character = pygame.transform.scale(character, (int(" + str(
                    w) + "/3),int(" + str(h) + "/3)))" + "\n"
                f.write(savedcode)

                savedcode = name + " = character" + "\n" + "\n"
                f.write(savedcode)
                f.close()

                f = open("Kim_Animates.txt", "a") # Animation code - Kim_Animates.txt.

                if counter == 0:
                    if not first:
                        savedcode = "\t" + "\t" + "elif self." + counter_type + "==xxxxxx:" + "\n"
                        f.write(savedcode)

                        savedcode = "\t" + "\t" + "\t" + "self." + counter_type + "=0" + "\n"
                        f.write(savedcode)
                    first = False
                    counter_type = input("Counter Type:")

                    savedcode = "\n" + "\n" + "\n" + "\n"
                    f.write(savedcode)
                    savedcode = "\t" + "elif selected_character == " + \
                        str(selected_character) + ": " + "\n"
                    f.write(savedcode)

                    if counter_type == "counter_jump":
                        savedcode = "\t" + "\t" + "if self." + counter_type + "==" + \
                            str(counter + 1) + "and self.yvel<0" + ":" + "\n"
                        f.write(savedcode)
                    else:
                        savedcode = "\t" + "\t" + "if self." + counter_type + "==" + \
                            str(counter * 5 + 1) + ":" + "\n"
                        f.write(savedcode)
                else:
                    if counter_type == "counter_jump":
                        savedcode = "\t" + "\t" + "elif self.yvel>=0:" + "\n"
                        f.write(savedcode)
                    else:
                        savedcode = "\t" + "\t" + "elif self." + counter_type + "==" + \
                            str(counter * 5) + ":" + "\n"
                        f.write(savedcode)
                

                savedcode = "\t" + "\t" + "\t" + \
                    "self.updatecharacter(Player_Sprites." + name + ")" + "\n"
                f.write(savedcode)

                savedcode = "\t" + "\t" + "\t" + "self.rect.size=(int(" + str(w) + \
                    "*2),int(" + str(h) + "/3)" + ")" + "\n"
                f.write(savedcode)

                f.close()
                counter += 1

        # Customize the screen.
        screen.fill(Color("#000000"))

        character = Surface((w, h))
        character.fill(Color("#25f422"))

        character.blit(spritesheet, (x, y))
        character = pygame.transform.scale(character, (w * 3, h * 3))
        screen.blit(character, (0, 0))

        pygame.display.update()

# Run the program.
selected_character = input("Which character?")
main()