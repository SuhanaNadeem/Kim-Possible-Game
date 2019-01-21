"""
The following program is what I use to display each of Kim's sprites (in the runloop, jumploop, and standloop).

For each sprite (from the spritesheet found online: https://www.spriters-resource.com/game_boy_advance/kimpossible2/sheet/49690/),
I have set its surface size, its location on the spritesheet, and then scaled it. 

The text file that SpriteMapping.py wrote to when I mapped all these sprites (KimPossibleSprite.txt) gave me the 
surface size of each sprite and its location on the spritesheet. I edited that raw code so each sprite is scaled 
with my desired scale factor, and change the variable names as well.
"""

import pygame

scale_factor = 1.5 # Setting the scale factor; Kim's sprites will be enlarged.

class Kim_Sprites:
    spritesheet = pygame.image.load("Graphics\\KimSprites.png")
    Kim = pygame.Surface((21,52),pygame.SRCALPHA) # Setting Kim as the original surface size (width and height) of the sprite.
    Kim.blit(spritesheet,(-14,-16)) # Blits the image (using its location on the spritesheet) on to the surface.
    Kim = pygame.transform.scale(Kim, (int(21*scale_factor),int(50*scale_factor))) # Scaling (enlarging) the sprite.
    stand1 = Kim # Defining the variable name of the above sprite, to be used in the Game program.

    Kim = pygame.Surface((22,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-79,-15))
    Kim = pygame.transform.scale(Kim, (int(22*scale_factor),int(50*scale_factor)))
    stand2 = Kim
    
    Kim = pygame.Surface((22,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-79,-15))
    Kim = pygame.transform.scale(Kim, (int(22*scale_factor),int(50*scale_factor)))
    stand3 = Kim

    Kim = pygame.Surface((22,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-110,-14))
    Kim = pygame.transform.scale(Kim, (int(22*scale_factor),int(50*scale_factor)))
    stand4 = Kim

    Kim = pygame.Surface((22,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-143,-13))
    Kim = pygame.transform.scale(Kim, (int(22*scale_factor),int(50*scale_factor)))
    stand5 = Kim

    Kim = pygame.Surface((22,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-173,-12))
    Kim = pygame.transform.scale(Kim, (int(22*scale_factor),int(50*scale_factor)))
    stand6 = Kim

    Kim = pygame.Surface((22,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-208,-12))
    Kim = pygame.transform.scale(Kim, (int(22*scale_factor),int(50*scale_factor)))
    stand7 = Kim

    Kim = pygame.Surface((22,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-242,-13))
    Kim = pygame.transform.scale(Kim, (int(22*scale_factor),int(50*scale_factor)))
    stand8 = Kim

    Kim = pygame.Surface((22,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-272,-13))
    Kim = pygame.transform.scale(Kim, (int(22*scale_factor),int(50*scale_factor)))
    stand9 = Kim

    Kim = pygame.Surface((21,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-305,-13))
    Kim = pygame.transform.scale(Kim, (int(21*scale_factor),int(50*scale_factor)))
    stand10 = Kim

    Kim = pygame.Surface((21,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-336,-13))
    Kim = pygame.transform.scale(Kim, (int(21*scale_factor),int(50*scale_factor)))
    stand11 = Kim

    Kim = pygame.Surface((20,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-368,-15))
    Kim = pygame.transform.scale(Kim, (int(20*scale_factor),int(50*scale_factor)))
    stand12 = Kim

    Kim = pygame.Surface((20,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-399,-15))
    Kim = pygame.transform.scale(Kim, (int(20*scale_factor),int(50*scale_factor)))
    stand13 = Kim

    Kim = pygame.Surface((20,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-429,-15))
    Kim = pygame.transform.scale(Kim, (int(20*scale_factor),int(50*scale_factor)))
    stand14 = Kim

    Kim = pygame.Surface((20,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-463,-15))
    Kim = pygame.transform.scale(Kim, (int(20*scale_factor),int(50*scale_factor)))
    stand15 = Kim

    Kim = pygame.Surface((20,52),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-493,-15))
    Kim = pygame.transform.scale(Kim, (int(20*scale_factor),int(50*scale_factor)))
    stand16 = Kim
    
    Kim = pygame.Surface((36,46),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-10,-84))
    Kim = pygame.transform.scale(Kim, (int(36*scale_factor),int(46*scale_factor)))
    run1 = Kim

    Kim = pygame.Surface((29,46),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-63,-84))
    Kim = pygame.transform.scale(Kim, (int(29*scale_factor),int(46*scale_factor)))
    run2 = Kim

    Kim = pygame.Surface((35,46),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-102,-84))
    Kim = pygame.transform.scale(Kim, (int(35*scale_factor),int(46*scale_factor)))
    run3 = Kim

    Kim = pygame.Surface((45,46),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-141,-85))
    Kim = pygame.transform.scale(Kim, (int(45*scale_factor),int(46*scale_factor)))
    run4 = Kim

    Kim = pygame.Surface((48,46),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-195,-83))
    Kim = pygame.transform.scale(Kim, (int(48*scale_factor),int(46*scale_factor)))
    run5 = Kim

    Kim = pygame.Surface((34,46),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-252,-87))
    Kim = pygame.transform.scale(Kim, (int(34*scale_factor),int(46*scale_factor)))
    run6 = Kim

    Kim = pygame.Surface((29,46),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-304,-86))
    Kim = pygame.transform.scale(Kim, (int(29*scale_factor),int(46*scale_factor)))
    run7 = Kim

    Kim = pygame.Surface((35,46),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-335,-88))
    Kim = pygame.transform.scale(Kim, (int(35*scale_factor),int(46*scale_factor)))
    run8 = Kim

    Kim = pygame.Surface((46,46),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-372,-87))
    Kim = pygame.transform.scale(Kim, (int(46*scale_factor),int(46*scale_factor)))
    run9 = Kim

    Kim = pygame.Surface((48,46),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-428,-85))
    Kim = pygame.transform.scale(Kim, (int(48*scale_factor),int(46*scale_factor)))
    run10 = Kim

    Kim = pygame.Surface((33,49),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-284,-326))
    Kim = pygame.transform.scale(Kim, (int(33*scale_factor),int(49*scale_factor)))
    jump10 = Kim

    Kim = pygame.Surface((32,49),pygame.SRCALPHA)
    Kim.blit(spritesheet,(-164,-330))
    Kim = pygame.transform.scale(Kim, (int(32*scale_factor),int(49*scale_factor)))
    jump11 = Kim