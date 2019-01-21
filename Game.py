"""
This is the main program. It carries out all the core functionalities of my Kim Possible game. 

I learned how to manipulate standard Pygame functionalities (displaying the screen, manipulating 
sprites, loading images, etc.) from the following sources:
- Anthony Biron (https://www.youtube.com/channel/UCy0eKoY5BVtcJHFQGKVe1yg)
- SentDex (https://www.youtube.com/user/sentdex)
- My brother, Sufiyaan Nadeem (https://github.com/SufiyaanNadeem) 
Pygame documentation (https://www.pygame.org/docs/).

Any code that I have borrowed has been referenced where it is found.
"""

# Importing all the main modules/functions needed.
import pygame
from pygame import *
import time
from pygame import Rect
import os # Used for bringing window to the centre of the screen. 

# Importing other programs created in Scripts/Globals, so specific functions can be used.
from Scripts.Buttons import * 
from Scripts.GUI import *
from Scripts.KeyInput import KeyInput_Handler
from Scripts.Kim_Sprites import *
from Scripts.Buttons import *
from Scripts.Coin_Sprite import *
from Globals import *

# Initializing all fonts needed.
font_130pt = pygame.font.SysFont("Default", 130)
font_30pt = pygame.font.SysFont("Default", 30)
font_25pt = pygame.font.SysFont("Default", 25)

# Defining the RGB values of the colours needed.
Fog = (20, 20, 20)
White = (255, 255, 255)
Green = (0, 128, 0)
Black = (0, 0, 0)

# Initializing Pygame to use all its functionalities.
pygame.init()

# Initializing music. 
pygame.mixer.music.load("BGMusic.mp3") # Loading Kim Possible theme song.
pygame.mixer.music.play(-1) # -1 for infinitely looping music.
pygame.mixer.music.set_volume(0.5) # Setting volume for the music, so it's half the volume.

# Initializing the coin sound effect, and setting its volume to full.
coinSound = pygame.mixer.Sound("Coin_Sound.wav")
coinSound.set_volume(1.0)

# Initalizing the window width and height, which will be the size of the screen.
WIN_WIDTH = 960
WIN_HEIGHT = 540

# Setting variables for half the window width and height (for complex_camera function).
HALF_WIDTH = WIN_WIDTH / float(2)
HALF_HEIGHT = WIN_HEIGHT / float(2)

# Initializing some variables used to display screen.
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32 # The number of bits that will be used for colour in game.
FLAGS = 0 # No additional built-in options for my display, so flags is 0.

# Creating an entities group (will contain characters, game objects) in a list. 
entities = pygame.sprite.Group() 
# Creating a coin group (will contain all the coins) in a list. 
coingroup = pygame.sprite.Group() 

# Sets the scene to Game (Level 1) when the function is called, and increases the player's health.
def Restart():
    Globals.scene = "Game"
    pygame.mixer.music.pause()
    Globals.player_health = 100
    Globals.current_level = 1
    main() # Main is called to re-initiate gameplay.

# Restart button is made in the Main program (not Buttons.py) because it uses the Restart function here.
btnRestart = Menu.Button(text="RESTART", rect=(0, 0, 160, 60),
                         bg=Fog, fg=White, bgr=Green, tag=("GameOver", None))
btnRestart.Left = WIN_WIDTH - 442
btnRestart.Top = WIN_HEIGHT - 320
btnRestart.Command = Restart

# Main function starts the game.
def main():
    # Emptying sprite lists so new sprites are created every time game is restarted.
    entities.empty()
    coingroup.empty()
  
    # Centring the game window on user's screen using os library imported earlier.
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 100) # 200, 100 is centre of screen.
    
    # Displaying the screen, window icon, caption, and initializing the timer.
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Kim Possible")
    icon=pygame.image.load("Graphics\\GameIcon.jpg")
    pygame.display.set_icon(icon)
    timer = pygame.time.Clock()

    # Creating platforms list that will contain all platform game objects.
    platforms = []

    x = y = 0 # Initalizing x and y to be manipulated later (in creating my platforms and character)

    # Checking for the current level and adding coins to coingroup, displaying player to screen.
    if Globals.current_level==1:

        player = Kim(32*2, 32*14) # Creating an instance of the Kim class, displaying her in bottom left of the screen.
      
        # Adding coins to coin group by creating instances of the coin class to different places on screen.
        coingroup.add(Coin(32*9, 32*14))
        coingroup.add(Coin(32*16, 32*13))
        coingroup.add(Coin(32*24, 32*14))
        coingroup.add(Coin(32*20, 32*8))
        coingroup.add(Coin(32*14, 32*8))
        coingroup.add(Coin(32*10, 32*7))
        coingroup.add(Coin(32*2, 32*2))
        coingroup.add(Coin(32*13, 32*2))
        coingroup.add(Coin(32*16, 32*3))
        coingroup.add(Coin(32*2, 32*13))
        
        # Creating level list that will be iterated over.
        level = [
            "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
            "L                            L",
            "L                          E L",
            "L                            L",
            "L                            L",
            "L    PPCAAAADPPCAADPPPPCAADPPL",
            "L                            L",
            "L                            L",
            "L                            L",
            "L                            L",
            "L           R                L",
            "LPPPCAAAADPPPPPPCAAAADPPPP   L",
            "L                            L",
            "L                            L",
            "L                            L",
            "L            R               L",
            "PPPPCAAADPPPPPPPPCAAADPPAAPPPP"]

    elif Globals.current_level == 2:
        # Repeating steps taken with level 1, with coins at new places on the screen and new level layout.
     
        player = Kim(32*2, 32*14) # Creating an instance of the Kim class, displaying her in bottom left of the screen.

        coingroup.add(Coin(32*9, 32*13))
        coingroup.add(Coin(32*19, 32*13))
        coingroup.add(Coin(32*27, 32*12))
        coingroup.add(Coin(32*24, 32*8))
        coingroup.add(Coin(32*18, 32*8))
        coingroup.add(Coin(32*8, 32*6))
        coingroup.add(Coin(32*4, 32*3))
        coingroup.add(Coin(32*16, 32*3))
        coingroup.add(Coin(32*19, 32*4))
        coingroup.add(Coin(32*4, 32*14))

        level = [
            "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
            "L                            L",
            "L                          E L",
            "L                            L",
            "L             R              L",
            "L    PPCAAAADPPPPCAAADPPCADPPL",
            "L                            L",
            "L                            L",
            "L                            L",
            "L                            L",
            "L    R                       L",
            "LPPPPCAADPPPCAAAADPPCAADPP   L",
            "L                            L",
            "L                            L",
            "L                            L",
            "L      R                     L",
            "PPCAADPPPPCAAADPPPCAADPPCAPPPP"]

    elif Globals.current_level == 3:
        # Repeating steps taken with level 1 and 2, with coins at new places on the screen and new level layout.

        player = Kim(32*2, 32*14) # Creating an instance of the Kim class, displaying her in bottom left of the screen.

        coingroup.add(Coin(32*13, 32*13))
        coingroup.add(Coin(32*18, 32*15))
        coingroup.add(Coin(32*24, 32*13))
        coingroup.add(Coin(32*22, 32*7))
        coingroup.add(Coin(32*12, 32*7))
        coingroup.add(Coin(32*8, 32*3))
        coingroup.add(Coin(32*5, 32*9))
        coingroup.add(Coin(32*15, 32*3))
        coingroup.add(Coin(32*24, 32*2))
        coingroup.add(Coin(32*6, 32*14))

        level = [
            "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
            "L                            L",
            "L                          E L",
            "L                            L",
            "L           R                L",
            "L    PCAAADPPPCAAAADPPCAADPPPL",
            "L                            L",
            "L                            L",
            "L                            L",
            "L                            L",
            "L            R               L",
            "LPPCADPPCADPPPPCADPPCADPP    L",
            "L                            L",
            "L                            L",
            "L                            L",
            "L               R            L",
            "PPPPCAADPPCAADPPPPPCADPPCADPPP"]

    # Building the level by checking where each tile is in the level list.
    for row in level: # The rows are the items in the list.
        for col in row: # The columns are the indices in each item of the list.
            if col == "P" or col == "E" or col == "p" or col == "C" or col == "A" or col == "D" or col == "L"  or col == "l" or col == "c" or col == "a" or col == "d" or col == "R":
                p = Platform(x, y, col) # Creating an instance of the platform class (tile), passing its representative letter (col).
                platforms.append(p) # Adding the tile to the platforms list.
                entities.add(p) # Adding the tile to the entities list.
            x += 32 # Moving 32 bits to the right once each column is iterated.
        y += 32 # Moving 32 bits down once each row is iterated.
        x = 0 # Setting x to 0 after each row is iterated, so columns iteration starts from the left.

    # Setting window height and width using the columns and rows in level list (in bits), and passing it in the camera class to track it.
    total_level_width = len(level[0]) * 32
    total_level_height = len(level) * 32
    camera = Camera(complex_camera, total_level_width, total_level_height) # Passing the complex_camera class, and width and height of window and creating Camera class.

    entities.add(player) # Adding player to entities class.
    Globals.coins = 0 # Setting the coins the player has collected to 0.
    
    # The following will occur as long as the game is running.
    while Globals.isRunning:

        timer.tick(60) # Setting the FPS to 60.
        
        # Checking for user input through events.
        for e in pygame.event.get():
            # Quit the game if the user closes the window.
            if e.type == QUIT:
                Globals.isRunning = False
            KeyInput_Handler(e) # Calling the KeyInput_Handler function from the KeyInput program to identify the event and update Globals variables accordingly.
            # If the mouse button is pressed, carry out the command. 
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1: # The mouse button is pressed, so set this to True (1).
                    for btn in Menu.Button.All: # From all the buttons, if the button is pressed and its tag (in Buttons.py) is the Game scene, carry out the button command (if it exists).
                        if btn.Tag[0] == Globals.scene and btn.Rolling:
                            if btn.Command != None:
                                btn.Command() 
                            btn.Rolling == False
                            break  

        # Displaying different pictures, buttons, etc. to the screen depending on the scene.
        if Globals.scene == "Menu":
            # Displaying the background image of the Menu scene.
            BackgroundImage = pygame.image.load("Graphics/MenuPic.jpg") 
            screen.blit(BackgroundImage, (0, 0))
            
            # Creating the Play button with the Menu tag from Buttons.py.
            for btn in Menu.Button.All: # Checking all the buttons from the GUI program.
                if btn.Tag[0] == "Menu": # If the item at the first index of the Tag attribute of the button (which describes the scene) is Menu, display that button.
                    btn.Render(screen)
            pygame.display.update() 

        elif Globals.scene == "Instructions":
            # Displaying the background image of the Menu scene.
            InstructionsImg = pygame.image.load("Graphics/InstructionsImg.jpg") 
            screen.blit(InstructionsImg,(0,0))
           
            # Creating the Play button with the Instructions tag from Buttons.py.
            for btn in Menu.Button.All:
                if btn.Tag[0] == "Instructions":
                    btn.Render(screen)
            pygame.display.update() 

        elif Globals.scene == "GameOver":
            pygame.mixer.music.pause() # Pausing the music.

            # If Kim's health is greater than 0, meaning the game is over because she cleared the last level, define congratulatory messages.
            if Globals.player_health > 0: 
                End_Message=font_130pt.render("Awesome!", 1, Black)
                End_Bottom_Message=font_30pt.render("           You Won!", 1, Black)
            
            # Otherwise, it means the game is over because she hit an obstacle, so define appropriate end messages.
            else:
                End_Message=font_130pt.render("Nice Try!", 1, Black)
                End_Bottom_Message=font_30pt.render("You Reached Level "+str(Globals.current_level), 1, Black)
          
            # Display the image for the game over screen (same as menu).
            GameOverImg = pygame.image.load("Graphics/MenuPic.jpg") 
            screen.blit(GameOverImg,(0,0))
          
            # Creating the Exit button with the GameOver tag from Buttons.py.
            for btn in Menu.Button.All:
                if btn.Tag[0] == "GameOver":
                    btn.Render(screen)
          
            # Displaying both components of the end message to the screen (regardless of which conditional block was entered above).
            screen.blit(End_Message, (510,325))
            screen.blit(End_Bottom_Message, (590,450))
            pygame.display.update() 

        elif Globals.scene == "Game":

            # Displaying a different background image based on the current level.
            if Globals.current_level==1:
                L1_Image = pygame.image.load("Graphics/Level1.png") 
                screen.blit(L1_Image,(0,0))

            elif Globals.current_level==2:
                L2_Image = pygame.image.load("Graphics/Level2.png") 
                screen.blit(L2_Image,(0,0))

            elif Globals.current_level==3:
                L3_Image = pygame.image.load("Graphics/Level3.png") 
                screen.blit(L3_Image,(0,0))

            pygame.mixer.music.unpause() # Playing the music, or continuing to play from where it stopped in GameOver.
            
            # Displaying coin sprites from the coingroup.
            for e in coingroup:
                screen.blit(e.image,camera.apply(e))
                e.update(platforms,entities)

            # Updating the player, her location, movement, and the platforms on the screen.
            player.update(Globals.up, Globals.down, Globals.left, Globals.right, Globals.isRunning, platforms)

            # Displaying the player and other game objects from the entities group.
            for e in entities:
                screen.blit(e.image, camera.apply(e))

            # Checking how many coins the player has collected, displaying a small-scaled version of the coin and the number of coins to the top left of the screen.
            num_coins = "x " + str(Globals.coins)
            if Globals.coins==1:
                screen.blit(Coin_Sprite.coin,(9,9))
                screen.blit(font_25pt.render(num_coins, True, (White)), (30, 8))
            elif Globals.coins==2:
                screen.blit(Coin_Sprite.coin,(9,9))
                screen.blit(font_25pt.render(num_coins, True, (White)), (30, 8))
            elif Globals.coins==3:
                screen.blit(Coin_Sprite.coin,(9,9))
                screen.blit(font_25pt.render(num_coins, True, (White)), (30, 8))
            elif Globals.coins==4:
                screen.blit(Coin_Sprite.coin,(9,9))
                screen.blit(font_25pt.render(num_coins, True, (White)), (30, 8))
            elif Globals.coins==5:
                screen.blit(Coin_Sprite.coin,(9,9))
                screen.blit(font_25pt.render(num_coins, True, (White)), (30, 8))
            elif Globals.coins==6:
                screen.blit(Coin_Sprite.coin,(9,9))
                screen.blit(font_25pt.render(num_coins, True, (White)), (30, 8))
            elif Globals.coins==7:
                screen.blit(Coin_Sprite.coin,(9,9))
                screen.blit(font_25pt.render(num_coins, True, (White)), (30, 8))
            elif Globals.coins==8:
                screen.blit(Coin_Sprite.coin,(9,9))
                screen.blit(font_30pt.render("ONLY TWO COINS LEFT ON THIS LEVEL!", True, (White)), (523, 6))
                screen.blit(font_25pt.render(num_coins, True, (White)), (30, 8))
            elif Globals.coins==9:
                screen.blit(Coin_Sprite.coin,(9,9))
                screen.blit(font_25pt.render(num_coins, True, (White)), (30, 8))
                screen.blit(font_30pt.render("ONLY ONE COIN LEFT ON THIS LEVEL!", True, (White)), (520, 6))
            elif Globals.coins==10:
                screen.blit(Coin_Sprite.coin,(9,10))
                screen.blit(font_25pt.render(num_coins, True, (Fog)), (30, 8))
                screen.blit(font_30pt.render("ALL COINS ON THIS LEVEL COLLECTED!", True, (White)), (520, 6))
            
            # End the game if the player's health is ever lower than or equal to 0.
            if Globals.player_health <= 0:
                Globals.scene = "GameOver"

            # Updating the screen.
            pygame.display.flip() 
            pygame.display.update()            

"""
The following camera functionalities were borrowed from Martian Marty (codergopher YouTube channel).
Camera class: https://youtu.be/AO_mUnSIMoU
Complex camera function: https://youtu.be/-5KEhsEdFus
They allow me to navigate the entities on my screen.
"""

# This class helps me track the location and movement of the entities in my game (like coins, player, etc.).
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height) # Defining field of vison from top left corner.

    def apply(self, target):
        return target.rect.move(self.state.topleft) # Detects if the entity is in motion.

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect) # Will update when it sees the movement of the entity.

def complex_camera(camera, target_rect):
    x, y, w, h = target_rect
    return Rect(HALF_WIDTH - x, HALF_HEIGHT - y, w, h)

# Base class I will use for all my entities, which has properties of a Pygame sprite base class for all visible game objects.
class Entity(pygame.sprite.Sprite):
    # Will initialize all my entities as Pygame sprites, so I can manipulate them with Pygame functionalities.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 

# Main character class that handles her movement, location, collisions, etc.
class Kim(Entity):
    # Sets up the initial location, movement, and properties of the player.
    def __init__(self, x, y):
        Entity.__init__(self) # Makes game object functionalities from Pygame available to player.

        # Sets the initial speed the player is moving up/down or left/right.
        self.xvel = 0
        self.yvel = 0
        self.health = Globals.player_health # Sets player's health to 100.

        # Defines location of the player based on what's passed to the class instantiation (x and y).
        self.x = x
        self.y = y

        # Defines attributes to be used in detecting collisions and sprite animations.        
        self.faceright = True
        self.destroyed = False
        self.counter_stand = 0
        self.counter_run = 0
        self.counter_jump = 0
        self.onGround = False
        self.moving = False
        self.airborne = False
        self.level_transition = False 

        # Setting initial image as first standing sprite and surface rect at the same location as the player, with a specific size.
        self.image = Kim_Sprites.stand1
        self.rect = Rect(x, y, 21*1.5, 49*1.5)

    # Updates Kim as she moves across the screen.
    def update(self, up, down, left, right, running, platforms):

        # Only updates if Kim is not destroyed.
        if not self.destroyed:
            # The following will occur by checking Global variables that will be passed to this function, manipulated by the KeyInput program.

            # Move Kim up at a constant y-velocity if the user presses the up arrow key and Kim is on the ground.   
            if up:
                if self.onGround:
                    self.yvel -= 16
            # Do nothing if the user presses the down arrow key.   
            if down:
                pass
            # Move Kim to the left at a set x-velocity (negative because it's left) if the user presses the left arrow key.   
            if left:
                self.xvel = -8
                self.faceright = False # Kim should face left.
            # Move Kim to the right at a set x-velocity if the user presses the right arrow key.   
            if right:
                self.xvel = 8
                self.faceright = True # Kim should face right. 
            # Move Kim down at a constant y-velocity if she is airborne.   
            if not self.onGround:
                self.yvel += 0.6 # Initial falling speed.
                # Defining the maximum falling speed.
                if self.yvel > 100:
                    self.yvel = 100
            # If the user hasn't pressed the let or right arrow key, Kim should not move horizontally.
            if not (left or right):
                self.xvel = 0

            # Increment Kim's horizontal position as she moves.    
            self.rect.left += self.xvel
            # Perform Kim's x-axis collisions.    
            self.collide(self.xvel, 0, platforms, up, down, left, right)

            # Increment Kim's vertical position as she moves.    
            self.rect.top += self.yvel
            
            # Setting Kim's onGround variable to False for her update function.  
            self.onGround = False

            # Update Kim's health.
            if self.health <= 0:
                self.destroyed = True
    
            # Perform Kim's y-axis collisions.    
            self.collide(0, self.yvel, platforms, up, down, left, right)
            
            # Change the level if Kim touches a door (part of the platforms list).
            if self.level_transition == True:
                for p in platforms:
                    if p.tile=="E":
                        p.change_level()

            # If Kim's y-axis movement has a falling or jumping velocity, she is in the air.
            if self.yvel < 0 or self.yvel > 9:
                self.airborne = True
            # Otherwise, she is not.
            else:
                self.airborne = False
        
        # Animating Kim's sprites based on all the above variable updates.
        self.animate()

    # Collides Kim with platforms in the platforms list.
    def collide(self, xvel, yvel, platforms, up, down, left, right):

        # For each game object in the platforms list, depending on what Kim collided with, perform certain actions.
        for p in platforms:
            # Detecting the collision between Kim and the platform.
            if pygame.sprite.collide_rect(self, p):

                # If Kim the tile Kim collided with is a door, change the kevel.
                if p.tile == "E":
                    # Change the level.
                    p.change_level()
                    #self.level_transition = True 
                    self.destroyed = True 
                    self.rect.midbottom = p.rect.midbottom # Collide in the centre of the door.

                # Otherwise, perform certain actions based on what Kim collided with.
                else:
                    # If Kim is not moving and facing right, collide her right side with the platform's left side.
                    if xvel == 0 and yvel == 0 and self.faceright:
                        self.rect.right = p.rect.left
                    
                    # If Kim is moving right...
                    if xvel > 0:                        
                        self.rect.right = p.rect.left # Collide Kim's right side with the platform's left side.
                        # If Kim collided with a lava or rock tile, update hear health and destroyed variables, and call the dead function.
                        if p.tile=="A" or p.tile=="R":    
                            self.health=0
                            Globals.player_health = self.health
                            self.destroyed=True
                            self.dead()

                    # If Kim is moving left...
                    if xvel < 0:
                        self.rect.left = p.rect.right # Collide Kim's left side with the platform's right side.
                        # If Kim collided with a lava or rock tile, update her health and destroyed variables, and call the dead function.                       
                        if p.tile=="A" or p.tile=="R":    
                            self.health = 0
                            Globals.player_health = self.health
                            self.destroyed = True
                            self.dead()

                    # If Kim is moving down...
                    if yvel > 0:
                        # If Kim collided with a lava or rock tile, update her health and destroyed variables, and call the dead function.
                        if p.tile=="A" or p.tile=="R":    
                            self.health = 0
                            Globals.player_health = self.health
                            self.destroyed = True
                            self.dead()
                        
                        self.rect.bottom = p.rect.top # Collide Kim's rect's bottom with the platform's rect's top.

                        # Update Kim's movement variables.
                        self.onGround = True
                        self.counter_jump = 0
                        self.airborne = False
                        self.yvel = 0

                    # If Kim is moving up, collide her rect's top with the platform's rect's bottom.
                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        
                        # If Kim is touching the bottom of a platform, make her fall back down at a constant y-velocity.
                        if (self.rect.top <= p.rect.bottom):
                            self.yvel += 1.3

    # Animates Kim as she moves, by calling her sprite animation loops based on her motion.
    def animate(self):  

        if not self.destroyed:
            # If Kim's x-axis movement has a moving left or right velocity, she should jump or run.
            if self.xvel > 0 or self.xvel < 0:
                self.counter_stand = 0

                # If Kim is in the air, initiate jump animation.
                if self.airborne:
                    self.jumploop()

                # Otherwise, initiate run animation.
                else:
                    self.runloop()

            # If Kim is not in horizontal motion, she should jump or stand.
            else:
                # If Kim is in the air, initiate jump animation.
                if self.airborne:
                    self.jumploop()

                # Otherwise, initiate stand animation.
                else:
                    self.standloop()
    
    # If Kim has been destroyed, pause the music, display the GameOver screen, and update her health.
    def dead(self):
        pygame.mixer.music.pause()
        Globals.scene = "GameOver"
        Globals.player_health = 0

    # Updating Kim's image with her animated surface.
    def updatecharacter(self, ansurf):
        if not self.faceright:
            ansurf = pygame.transform.flip(ansurf, True, False) # Making Kim's animation face left by flipping surface horizontally.
        self.image = ansurf


    # Checks and increments counter_stand's value to loop through Kim's standing sprites.
    def standloop(self):
        # The following uses the code written to a text file by SpriteMapping.py. The numbers between each check for counter_stand controls the speed of the animation.
        if self.counter_stand==1:
            self.updatecharacter(Kim_Sprites.stand1) # Updates the animated surface.
            self.rect.size=(21*1.5, 49*1.5) # Defines the rect size of the surface.
        elif self.counter_stand==4:
            self.updatecharacter(Kim_Sprites.stand2)
            self.rect.size=(22*1.5, 49*1.5)
        elif self.counter_stand==7:
            self.updatecharacter(Kim_Sprites.stand3)
            self.rect.size=(22*1.5,49*1.5)
        elif self.counter_stand==10:
            self.updatecharacter(Kim_Sprites.stand4)
            self.rect.size=(22*1.5,49*1.5)
        elif self.counter_stand==13:
            self.updatecharacter(Kim_Sprites.stand5)
            self.rect.size=(22*1.5,49*1.5)
        elif self.counter_stand==16:
            self.updatecharacter(Kim_Sprites.stand6)
            self.rect.size=(22*1.5,49*1.5)
        elif self.counter_stand==19:
            self.updatecharacter(Kim_Sprites.stand7)
            self.rect.size=(22*1.5, 49*1.5)
        elif self.counter_stand==22:
            self.updatecharacter(Kim_Sprites.stand8)
            self.rect.size=(22*1.5, 49*1.5)
        elif self.counter_stand==25:
            self.updatecharacter(Kim_Sprites.stand9)
            self.rect.size=(22*1.5,49*1.5)
        elif self.counter_stand==28:
            self.updatecharacter(Kim_Sprites.stand10)
            self.rect.size=(21*1.5,49*1.5)
        elif self.counter_stand==31:
            self.updatecharacter(Kim_Sprites.stand11)
            self.rect.size=(21*1.5,49*1.5)
        elif self.counter_stand==34:
            self.updatecharacter(Kim_Sprites.stand12)
            self.rect.size=(20*1.5,49*1.5)
        elif self.counter_stand==37:
            self.updatecharacter(Kim_Sprites.stand13)
            self.rect.size=(20*1.5,49*1.5)
        elif self.counter_stand==40:
            self.updatecharacter(Kim_Sprites.stand14)
            self.rect.size=(20*1.5,49*1.5)
        elif self.counter_stand==43:
            self.updatecharacter(Kim_Sprites.stand15)
            self.rect.size=(20*1.5,49*1.5)
            self.counter_stand = 0 # Set counter_stand to 0 to re-loop through the animation.
        self.counter_stand += 1 # Increment counter_stand each time a sprite is displayed, to display the next sprite in the animation.

    # Checks and increments counter_run's value to loop through Kim's running sprites.
    def runloop(self):
        # The following uses the code written to a text file by SpriteMapping.py. The numbers between each check for counter_stand controls the speed of the animation.
        if self.counter_run==1:
            self.updatecharacter(Kim_Sprites.run1) # Updates the animated surface.
            self.rect.size=(36*1.5, 49*1.5) # Defines the rect size of the surface.
        elif self.counter_run==3:
            self.updatecharacter(Kim_Sprites.run1)
            self.rect.size=(36*1.5, 49*1.5)
        elif self.counter_run==5:
            self.updatecharacter(Kim_Sprites.run2)
            self.rect.size=(29*1.5, 49*1.5)
        elif self.counter_run==7:
            self.updatecharacter(Kim_Sprites.run3)
            self.rect.size=(35*1.5, 49*1.5)
        elif self.counter_run==9:
            self.updatecharacter(Kim_Sprites.run4)
            self.rect.size=(45*1.5, 49*1.5)
        elif self.counter_run==11:
            self.updatecharacter(Kim_Sprites.run5)
            self.rect.size=(48*1.5, 49*1.5)
        elif self.counter_run==13:
            self.updatecharacter(Kim_Sprites.run6)
            self.rect.size=(34*1.5, 49*1.5)
        elif self.counter_run==15:
            self.updatecharacter(Kim_Sprites.run7)
            self.rect.size=(29*1.5, 49*1.5)
        elif self.counter_run==17:
            self.updatecharacter(Kim_Sprites.run8)
            self.rect.size=(35*1.5, 49*1.5)
        elif self.counter_run==19:
            self.updatecharacter(Kim_Sprites.run9)
            self.rect.size=(52*1.5, 49*1.5)
        elif self.counter_run==21:
            self.counter_run = 0 # Set counter_run to 0 to re-loop through the animation.
        self.counter_run += 1 # Increment counter_run each time a sprite is displayed, to display the next sprite in the animation.

    def jumploop(self):
        #self.counter_jump += 1
        # If Kim's moving up, display the jumping sprite. 
        if self.yvel < 0:
            #print("I entered")
            self.updatecharacter(Kim_Sprites.jump11) # Updates the animated surface.
            self.rect.size=(int(33*1.5),int(49*1.5)) # Defines the rect size of the surface.
        # If Kim's moving down, display the landing sprite. 
        elif self.yvel >= 0:
            #print("Im working")
            self.updatecharacter(Kim_Sprites.jump10)
            self.rect.size=(int(32*1.5),int(49*1.5))

class Coin(Entity):
    def __init__(self, x, y):
        Entity.__init__(self) # Makes game object functionalities from Pygame available to coin.

        # Defines attributes to be used in detecting collisions and sprite animations.        
        self.destroyed = False 
        self.counter_dead = 0

        # Defines location of the coin based on what's passed to the class instantiation (x and y).
        self.x = x
        self.y = y

        self.image = Coin_Sprite.coin # Sets the coin's image to the coin sprite from Coin_Sprite.py.
        self.rect = Rect(x, y, 16, 16) # Setting the desired size of the coin's surface rect.

    # Collide the coin with platforms and entities, and animate it ()
    def update(self, platforms, entities):
        self.collide(platforms, entities)
        self.animate()
        
    def collide(self, platforms, entities):
        # Check collision of the player with the coin occured, and if so, update the destroyed variable and remove the coin from the coingroup.
        for player in entities:
            if pygame.sprite.collide_rect(self, player):
                self.destroyed = True
                coingroup.remove(self)

    def animate(self):
        # Play the coin sound effect, increment the player's coins collected, and kill the coin/
        if self.destroyed:
            coinSound.play()
            Globals.coins += 1
            self.kill()

#Platform Class that handles blitting specific tiles depending on the type of letter in the levels list
class Platform(Entity):
    def __init__(self, x, y, tile):
        Entity.__init__(self) # Makes game object functionalities from Pygame available to platform.
        self.counter_change = 1 # Used to change the level upon door collision.
        self.tile = tile # Defining platform tile.
        
        # Load the platform game object depending on the letter entered in the level.
        if self.tile=="E":
            self.image = pygame.image.load("Graphics/DoorClosed.png")
        elif self.tile=="R":
            self.image = pygame.image.load("Graphics/Rock.png")
        elif self.tile=="P":
            self.image = pygame.image.load("Graphics/Tile2.png")
        elif self.tile=="C":
            self.image = pygame.image.load("Graphics/Tile1.png")
        elif self.tile=="A":
            self.image = pygame.image.load("Graphics/Lava.png")
        elif self.tile=="D":
            self.image = pygame.image.load("Graphics/Tile3.png")
        elif self.tile=="L":
            self.image = pygame.image.load("Graphics/Tile4.png")

        # Scale the door's to a custom size, otherwise the standard 32 by 32 regardless of the tile.
        if self.tile=="E":
            self.image = pygame.transform.scale(self.image, (58,96))
        else:
            self.image = pygame.transform.scale(self.image, (32,32))
        
        # Set the door's surface rect to a custom size, otherwise the standard 32 by 32 regardless of the tile.
        if self.tile=="E":
            self.rect = Rect(x, y, 58, 96)
        else:
            self.rect = Rect(x, y, 32, 32)  
            
    # Changing the level when Kim collides with the door.
    def change_level(self):

        # Change the level/scene.
        # If Kim collided with the door on level three, player won the game, so go to GameOver screen.
        if Globals.current_level == 3:
            Globals.scene = "GameOver"
        # Otherwise, increment the level and call the main function again.
        else:
            Globals.current_level += 1
            main()

main() # Calling the main function to initiate gameplay.
pygame.quit() # Quit the game once the main function execution is complete.