"""
Instead of having to crop each of my sprites from the spritesheet, I'm using this Sprite Mapping functionality 
which allows me to save each sprite as its own surface and name it different variable names. THis is not used in the
actual gameplay; just makes it easier for me.
This code has been borrowed from: Sufiyaan Nadeem (https://github.com/SufiyaanNadeem/Ben-10-Game/blob/master/Scripts/Sprite_Mapping.py),
as adapted by Anthony Biron (https://www.youtube.com/watch?v=cSsurU0yFEw). 
Edited by: Suhana Nadeem.
I have edited Sufiyaan's code (and commented it) so I can now 
"""
# Imports
import pygame
from pygame import *
import sys

# Screen Dimensions

WIN_WIDTH = 768
WIN_HEIGHT = 672

# Screen Defaults

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

# Spritesheet

spritesheet = pygame.image.load("CoinSpriteSheet.png")

# Main Function

def main():
    isRunning = True
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Sprite Mapper")
    x = y = 0
    w = h = 100
    pygame.key.set_repeat(1, 30)
    counter = 0
    first = True
    while isRunning:
        print(str(h))
        for e in pygame.event.get():
            if e.type == QUIT:
                isRunning = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                isRunning = False
            if e.type == KEYDOWN and e.key == K_UP:
                y = y - 1
            if e.type == KEYDOWN and e.key == K_DOWN:
                y = y + 1
            if e.type == KEYDOWN and e.key == K_LEFT:
                x = x - 1
            if e.type == KEYDOWN and e.key == K_RIGHT:
                x = x + 1

            if e.type == KEYDOWN and e.key == K_i:
                y = y - 5
            if e.type == KEYDOWN and e.key == K_k:
                y = y + 5
            if e.type == KEYDOWN and e.key == K_j:
                x = x - 5
            if e.type == KEYDOWN and e.key == K_l:
                x = x + 5

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
            if e.type == KEYDOWN and e.key == K_SPACE:
                name = input("Name of Sprite?")

                f = open("GameObjectSprites.txt", "a")

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

                f = open("GameObject_Animates.txt", "a")

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

        screen.fill(Color("#000000"))

        character = Surface((w, h))
        character.fill(Color("#25f422"))

        character.blit(spritesheet, (x, y))
        character = pygame.transform.scale(character, (w * 3, h * 3))
        screen.blit(character, (0, 0))

        pygame.display.update()


selected_character = input("Which character?")
main()