"""This is the main game, which carries out all the core functionalities of the Kim Possible game. Doing basic Pygame tasks like
displaying the screen, loading images and music, were learned and adapted from: Anthony Biron (), A Bit Racey Dude (), """

# Importing all the main modules needed.
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
from Scripts.GameObject_Sprites import *
from Globals import *

# Initializing all fonts needed.
font_130pt = pygame.font.SysFont("Neucha", 130)
font_30pt = pygame.font.SysFont("Neucha", 30)
font_15pt = pygame.font.SysFont("Neucha", 15)
font_25pt = pygame.font.SysFont("Neucha", 15)

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

# Setting variables for half the window width and height, for future reference (complex_camera function).
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
                         bg=UltraColor.Fog, fg=UltraColor.White, bgr=UltraColor.Green, tag=("GameOver", None))
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
        #player = Kim(32*16, 32*4)
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
            "L                   R        L",
            "L    PPCAAAADPPCAADPPPCAAADPPL",
            "L                            L",
            "L                            L",
            "L                            L",
            "L                            L",
            "L           R          R     L",
            "LPPPCAAAADPPPPPPCAAAADPPPP   L",
            "L                            L",
            "L                            L",
            "L                            L",
            "L            R               L",
            "PPPPCAAADPPPPPPPPCAAADPPAAPPPP"]

    elif Globals.current_level == 2:
        # Repeating steps taken with level 1, with coins at new places on the screen and new level layout.
        player = Kim(32*2, 32*14)
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
            "L    R    R                  L",
            "LPPPPCAADPPPCAAAADPPCAADPP   L",
            "L                            L",
            "L                            L",
            "L                            L",
            "L      R                R    L",
            "PPCAADPPPPCAAADPPPCAADPPPCAPPP"]

    elif Globals.current_level == 3:
        # Repeating steps taken with level 1 and 2, with coins at new places on the screen and new level layout.

        player = Kim(32*2, 32*14)
        #player = Kim(32*7, 32*4)

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
            "PPPCAAADPPCAADPPPPCAADPPCADPPP"]

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
            #Globals.menu_counter += 1
            # Displaying the background image of the Menu scene.
            BackgroundImage = pygame.image.load("Graphics/MenuPic.jpg") 
            screen.blit(BackgroundImage, (0, 0))
            pygame.display.flip() 
            
            # Creating the Play button with the Menu tag from Buttons.py.
            for btn in Menu.Button.All: # Checking all the buttons from the GUI program.
                if btn.Tag[0] == "Menu": # If the item at the first index of the Tag attribute of the button (which describes the scene) is Menu, display that button.
                    btn.Render(screen)
            pygame.display.update() 

        elif Globals.scene == "Instructions":
            # Displaying the background image of the Menu scene.
            InstructionsImg = pygame.image.load("Graphics/InstructionsImg.jpg") 
            screen.blit(InstructionsImg,(0,0))
            pygame.display.flip() 
           
            # Creating the Play button with the Instructions tag from Buttons.py.
            for btn in Menu.Button.All:
                if btn.Tag[0] == "Instructions":
                    btn.Render(screen)
            pygame.display.update() 

        elif Globals.scene == "GameOver":
            pygame.mixer.music.pause() # Pausing the music.
            # If Kim's health is greater than 0, meaning the game is over because she cleared the last level, define congratulatory messages.
       
            if Globals.player_health > 0: 
                End_Message=font_130pt.render("Fantastic!", 1, UltraColor.Black)
                End_Bottom_Message=font_30pt.render("       You Won!", 1, UltraColor.Black)
            # Otherwise, it means the game is over because she hit an obstacle, so define appropriate end messages.
          
            else:
                End_Message=font_130pt.render("Nice Try!", 1, UltraColor.Black)
                End_Bottom_Message=font_30pt.render("You Reached Level "+str(Globals.current_level), 1, UltraColor.Black)
          
            # Display the image for the game over screen (same as menu).
            GameOverImg = pygame.image.load("Graphics/MenuPic.jpg") 
            screen.blit(GameOverImg,(0,0))
          
            # Creating the Exit button with the GameOver tag from Buttons.py.
            for btn in Menu.Button.All:
                if btn.Tag[0] == "GameOver":
                    btn.Render(screen)
          
            # Displaying both components of the end message to the screen (regardless of which conditional block was entered above).
            screen.blit(End_Message, (485,285))
            screen.blit(End_Bottom_Message, (600,450))
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
            player.update(Globals.up, Globals.down, Globals.left,
                        Globals.right, Globals.isRunning, platforms)

            # Displaying the player and other game objects from the entities group.
            for e in entities:
                screen.blit(e.image, camera.apply(e))

            # Checking how many coins the player has collected, displaying a small-scaled version of the coin and the number of coins to the top left of the screen.
            num_coins = "x " + str(Globals.coins)
            if Globals.coins==1:
                screen.blit(GameObject_Sprites.coin,(9,9))
                screen.blit(font_15pt.render(num_coins, True, (UltraColor.White)), (30, 8))
            elif Globals.coins==2:
                screen.blit(GameObject_Sprites.coin,(9,9))
                screen.blit(font_15pt.render(num_coins, True, (UltraColor.White)), (30, 8))
            elif Globals.coins==3:
                screen.blit(GameObject_Sprites.coin,(9,9))
                screen.blit(font_15pt.render(num_coins, True, (UltraColor.White)), (30, 8))
            elif Globals.coins==4:
                screen.blit(GameObject_Sprites.coin,(9,9))
                screen.blit(font_15pt.render(num_coins, True, (UltraColor.White)), (30, 8))
            elif Globals.coins==5:
                screen.blit(GameObject_Sprites.coin,(9,9))
                screen.blit(font_15pt.render(num_coins, True, (UltraColor.White)), (30, 8))
            elif Globals.coins==6:
                screen.blit(GameObject_Sprites.coin,(9,9))
                screen.blit(font_15pt.render(num_coins, True, (UltraColor.White)), (30, 8))
            elif Globals.coins==7:
                screen.blit(GameObject_Sprites.coin,(9,9))
                screen.blit(font_15pt.render(num_coins, True, (UltraColor.White)), (30, 8))
            elif Globals.coins==8:
                screen.blit(GameObject_Sprites.coin,(9,9))
                screen.blit(font_30pt.render("ONLY TWO COINS LEFT ON THIS LEVEL!", True, (UltraColor.Fog)), (523, 0.5))
                screen.blit(font_15pt.render(num_coins, True, (UltraColor.White)), (30, 8))
            elif Globals.coins==9:
                screen.blit(GameObject_Sprites.coin,(9,9))
                screen.blit(font_15pt.render(num_coins, True, (UltraColor.White)), (30, 8))
                screen.blit(font_30pt.render("ONLY ONE COIN LEFT ON THIS LEVEL!", True, (UltraColor.Fog)), (520, 0.5))
            elif Globals.coins==10:
                screen.blit(GameObject_Sprites.coin,(9,10))
                screen.blit(font_25pt.render(num_coins, True, (UltraColor.Fog)), (30, 8))
                screen.blit(font_30pt.render("ALL COINS ON THIS LEVEL COLLECTED!", True, (UltraColor.Fog)), (520, 0.5))
            
            # End the game if the player's health is ever lower than or equal to 0.
            if Globals.player_health <= 0:
                Globals.scene = "GameOver"

            # Updating the screen.
            pygame.display.flip() 
            pygame.display.update()            

"""
The following Camera Class and Complex Camera function were borrowed from Anthony Biron (https://www.youtube.com/watch?v=FpufbRZxKRM).
This complex camera function follows my player until he hits the edge of the map
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
"""
def complex_camera(camera, target_rect):
    x, y, w, h = target_rect
    return Rect(HALF_WIDTH - x, HALF_HEIGHT - y, w, h)
"""
# The complex camera tracks entities from a fixed point of view.
def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l + HALF_WIDTH, -t + HALF_HEIGHT, w, h

    l = min(0, l) 
    l = max(-(camera.width - WIN_WIDTH), l)
    t = max(-(camera.height - WIN_HEIGHT), t) 
    t = min(0, t) 
    return Rect(l, t, w, h)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Kim(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.health=Globals.player_health

        self.x = x
        self.y = y

        self.faceright = True
        self.destroyed = False
        self.counter_stand = 0
        self.counter_run = 0
        self.counter_jump = 0
        self.onGround = False

        self.moving = False
        self.airborne = False
        self.destroyed = False

        self.fade = True

        self.image = Kim_Sprites.stand1
        self.rect = Rect(x,y,21*1.5, 52*1.5)

    def update(self, up, down, left, right, running, platforms):

        if not self.destroyed:
            """
            if Globals.timer<=0:
                Globals.timer=0
            """
            
            if up:
                #print('up')
                if self.onGround:
                    self.yvel -= 16

            if down:
                pass

            if left:
                self.xvel = -11               
                self.faceright = False

            if right:
                self.xvel = 11
                self.faceright = True
                
            if not self.onGround:
                self.yvel += 0.6
                # Maximum falling speed.
                if self.yvel > 100:
                    self.yvel = 100

            if not (left or right):
                self.xvel = 0

            # increment in x direction
            self.rect.left += self.xvel
            
            # do x-axis collisions
            self.collide(self.xvel, 0, platforms, up, down, left, right)
            
            # increment in y direction
            self.rect.top += self.yvel
            # assuming we're in the air
            self.onGround = False
            
            if self.health<=0:
                self.destroyed=True
    
            # do y-axis collisions
            self.collide(0, self.yvel, platforms, up, down, left, right)
            
            if self.fade==False:
                for p in platforms:
                    if p.tile=="E":
                        p.change_level()

            #self.updatecharacter(Kim_Sprites.run1)

            if self.yvel < 0 or self.yvel > 9:
                self.airborne = True
            else:
                self.airborne=False
        #print( self.yvel)
        self.animate()

    def collide(self, xvel, yvel, platforms, up, down, left, right):

        for p in platforms:
            if pygame.sprite.collide_rect(self, p):

                if p.tile=="E":
                    p.change_level()
                    self.fade=False
                    self.destroyed=True
                    self.rect.midbottom=p.rect.midbottom           

                else:
                    if xvel==0 and yvel==0 and self.faceright:
                        self.rect.right=p.rect.left

                    if xvel > 0:                        
                        self.rect.right = p.rect.left
                        if p.tile=="A" or p.tile=="R":
                            self.health=0
                            Globals.player_health = self.health
                            self.destroyed=True
                            self.dead()

                    if xvel < 0:
                        self.rect.left = p.rect.right
                        if p.tile=="A" or p.tile=="R":
                            self.health=0
                            Globals.player_health = self.health
                            self.destroyed=True
                            self.dead()

                    if yvel > 0:
                        if p.tile=="A" or p.tile=="R":
                            self.health=0
                            Globals.player_health = self.health
                            self.destroyed=True
                            self.dead()
                        
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.counter_jump = 0
                        self.airborne = False
                        self.yvel = 0

                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        
                        #touching top
                        if (self.rect.top <= p.rect.bottom):
                            #print("touching")
                            self.yvel+=1.3
                
                """
                if p.tile=="E":
                    if Globals.current_level == 3:
                        Globals.scene = "GameOver"
                    else:
                        Globals.current_level += 1
                """

            """
    def collide(self, xvel, yvel, platforms):
        #Collide Platforms
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel = -2
                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel = 2
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                """

    def animate(self):
        if not self.destroyed:
            if self.xvel > 0 or self.xvel < 0:
                self.counter_stand=0
                #self.updatecharacter(Kim_Sprites.stand1)
                if self.airborne:
                    #self.move = True
                    self.jumploop()
                    self.counter_run = 0
                else:
                    self.runloop()
            else:
                if self.airborne:
                    self.jumploop()
                    self.counter_run = 0
                else:
                    #print ("stand")
                    self.standloop()
    
    def dead(self):
        pygame.mixer.music.pause()
        Globals.scene="GameOver"
        Globals.player_health = 0

    def updatecharacter(self, ansurf):
        if not self.faceright:
            ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf
    
    def standloop(self):
        #print ("entered stand loop")
        if self.counter_stand==1:
            self.updatecharacter(Kim_Sprites.stand1)
            self.rect.size=(21*1.5, 52*1.5)
        elif self.counter_stand==4:
            self.updatecharacter(Kim_Sprites.stand2)
            self.rect.size=(22*1.5, 52*1.5)
        elif self.counter_stand==7:
            self.updatecharacter(Kim_Sprites.stand3)
            self.rect.size=(22*1.5,52*1.5)
        elif self.counter_stand==10:
            self.updatecharacter(Kim_Sprites.stand4)
            self.rect.size=(22*1.5,52*1.5)
        elif self.counter_stand==13:
            self.updatecharacter(Kim_Sprites.stand5)
            self.rect.size=(22*1.5,52*1.5)
        elif self.counter_stand==16:
            self.updatecharacter(Kim_Sprites.stand6)
            self.rect.size=(22*1.5,52*1.5)
        elif self.counter_stand==19:
            self.updatecharacter(Kim_Sprites.stand7)
            self.rect.size=(22*1.5, 52*1.5)
        elif self.counter_stand==22:
            self.updatecharacter(Kim_Sprites.stand8)
            self.rect.size=(22*1.5, 52*1.5)
        elif self.counter_stand==25:
            self.updatecharacter(Kim_Sprites.stand9)
            self.rect.size=(22*1.5,52*1.5)
        elif self.counter_stand==28:
            self.updatecharacter(Kim_Sprites.stand10)
            self.rect.size=(21*1.5,52*1.5)
        elif self.counter_stand==31:
            self.updatecharacter(Kim_Sprites.stand11)
            self.rect.size=(21*1.5,52*1.5)
        elif self.counter_stand==34:
            self.updatecharacter(Kim_Sprites.stand12)
            self.rect.size=(20*1.5,52*1.5)
        elif self.counter_stand==37:
            self.updatecharacter(Kim_Sprites.stand13)
            self.rect.size=(20*1.5,52*1.5)
        elif self.counter_stand==40:
            self.updatecharacter(Kim_Sprites.stand14)
            self.rect.size=(20*1.5,52*1.5)
        elif self.counter_stand==43:
            self.updatecharacter(Kim_Sprites.stand15)
            self.rect.size=(20*1.5,52*1.5)
            """elif self.counter_stand==75:
            
            self.updatecharacter(Kim_Sprites.stand16)
            self.rect.size=(int(20*2),int(52/3))
            """
            #print("last stand")
            self.counter_stand = 0
        self.counter_stand += 1
        #print(self.counter_stand)

    def runloop(self):
        if self.counter_run==1:
            self.updatecharacter(Kim_Sprites.run1)
            self.rect.size=(36*1.5, 52*1.5)
        elif self.counter_run==2:
            self.updatecharacter(Kim_Sprites.run1)
            self.rect.size=(36*1.5, 52*1.5)
        elif self.counter_run==3:
            self.updatecharacter(Kim_Sprites.run2)
            self.rect.size=(29*1.5, 52*1.5)
        elif self.counter_run==4:
            self.updatecharacter(Kim_Sprites.run3)
            self.rect.size=(35*1.5, 52*1.5)
        elif self.counter_run==5:
            self.updatecharacter(Kim_Sprites.run4)
            self.rect.size=(45*1.5, 52*1.5)
        elif self.counter_run==6:
            self.updatecharacter(Kim_Sprites.run5)
            self.rect.size=(48*1.5, 52*1.5)
        elif self.counter_run==7:
            self.updatecharacter(Kim_Sprites.run6)
            self.rect.size=(34*1.5, 52*1.5)
        elif self.counter_run==8:
            self.updatecharacter(Kim_Sprites.run7)
            self.rect.size=(29*1.5, 52*1.5)
        elif self.counter_run==9:
            self.updatecharacter(Kim_Sprites.run8)
            self.rect.size=(35*1.5, 52*1.5)
        elif self.counter_run==10:
            self.updatecharacter(Kim_Sprites.run9)
            self.rect.size=(52*1.5, 52*1.5)
        elif self.counter_run==11:
            self.counter_run = 0
        self.counter_run+=1

    def jumploop(self):
        #self.counter_jump += 1
        if self.yvel < 0:
            #print("I entered")
            self.updatecharacter(Kim_Sprites.jump11)
            self.rect.size=(int(33*1.5),int(52*1.5))
        elif self.yvel >= 0:
            #print("Im working")
            self.updatecharacter(Kim_Sprites.jump10)
            self.rect.size=(int(32*1.5),int(52*1.5))

class Coin(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.destroyed = False
        self.counter_dead = 0
        self.x = x
        self.y = y
        self.image = GameObject_Sprites.coin
        self.rect = Rect(x, y, 16, 16)

    def update(self, platforms, entities):
        self.collide(platforms, entities)
        self.animate()
        
    def collide(self, platforms, entities):
        for player in entities:
            if pygame.sprite.collide_rect(self, player):
                self.destroyed = True
                coingroup.remove(self)

    def animate(self):
        if self.destroyed:
            coinSound.play()
            self.destroyloop()

    def destroyloop(self):
        Globals.coins+=1
        self.kill()

#Platform Class that handles blitting specific tiles depending on the type of letter in the levels list
class Platform(Entity):
    def __init__(self, x, y, tile):
        Entity.__init__(self)
        self.counter_change = 0
        self.tile = tile
        
        if self.tile=="E":
            self.image = pygame.image.load("Graphics/DoorClosed.png")
        elif self.tile=="R":
            self.image = pygame.image.load("Graphics/Rock.png")
        elif self.tile=="P":
            self.image = pygame.image.load("Graphics/Tile2.png").convert()
        elif self.tile=="C":
            self.image = pygame.image.load("Graphics/Tile1.png").convert()
        elif self.tile=="A":
            self.image = pygame.image.load("Graphics/Lava.png")
        elif self.tile=="D":
            self.image = pygame.image.load("Graphics/Tile3.png").convert()
        elif self.tile=="L":
            self.image = pygame.image.load("Graphics/Tile4.png").convert()

        if self.tile=="E":
            self.image = pygame.transform.scale(self.image, (58,96))
        else:
            self.image = pygame.transform.scale(self.image, (32,32))
        
        if self.tile=="E":
            self.rect = Rect(x, y, 58, 96)
        
        else:
            self.rect = Rect(x, y, 32, 32)  # change according to pic width
            
    #Changing Door sprite when player collects 3 keys
    def change_level(self):
        if self.counter_change==1:
            self.image = GameObject_Sprites.Door_Open
        elif self.counter_change==2:
            if Globals.current_level == 3:
                Globals.scene = "GameOver"
            else:
                Globals.current_level+=1
                main()     
        self.counter_change+=1
    
    def update(self):
        pass

main()
pygame.quit()