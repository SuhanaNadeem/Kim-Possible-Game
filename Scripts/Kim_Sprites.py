import pygame

scale_factor=1.5

class Kim_Sprites:
    spritesheet = pygame.image.load("Graphics\\KimSprites.png")

    character = pygame.Surface((21,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-14,-16))
    character = pygame.transform.scale(character, (int(21*scale_factor),int(52*scale_factor)))
    stand1 = character

    character = pygame.Surface((22,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-79,-15))
    character = pygame.transform.scale(character, (int(22*scale_factor),int(52*scale_factor)))
    stand2 = character
    
    character = pygame.Surface((22,52),pygame.SRCALPHA)
    
    character.blit(spritesheet,(-79,-15))
    character = pygame.transform.scale(character, (int(22*scale_factor),int(52*scale_factor)))
    stand3 = character

    character = pygame.Surface((22,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-110,-14))
    character = pygame.transform.scale(character, (int(22*scale_factor),int(52*scale_factor)))
    stand4 = character

    character = pygame.Surface((22,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-143,-13))
    character = pygame.transform.scale(character, (int(22*scale_factor),int(52*scale_factor)))
    stand5 = character

    character = pygame.Surface((22,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-173,-12))
    character = pygame.transform.scale(character, (int(22*scale_factor),int(52*scale_factor)))
    stand6 = character

    character = pygame.Surface((22,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-208,-12))
    character = pygame.transform.scale(character, (int(22*scale_factor),int(52*scale_factor)))
    stand7 = character

    character = pygame.Surface((22,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-242,-13))
    character = pygame.transform.scale(character, (int(22*scale_factor),int(52*scale_factor)))
    stand8 = character

    character = pygame.Surface((22,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-272,-13))
    character = pygame.transform.scale(character, (int(22*scale_factor),int(52*scale_factor)))
    stand9 = character

    character = pygame.Surface((21,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-305,-13))
    character = pygame.transform.scale(character, (int(21*scale_factor),int(52*scale_factor)))
    stand10 = character

    character = pygame.Surface((21,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-336,-13))
    character = pygame.transform.scale(character, (int(21*scale_factor),int(52*scale_factor)))
    stand11 = character

    character = pygame.Surface((20,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-368,-15))
    character = pygame.transform.scale(character, (int(20*scale_factor),int(52*scale_factor)))
    stand12 = character

    character = pygame.Surface((20,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-399,-15))
    character = pygame.transform.scale(character, (int(20*scale_factor),int(52*scale_factor)))
    stand13 = character

    character = pygame.Surface((20,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-429,-15))
    character = pygame.transform.scale(character, (int(20*scale_factor),int(52*scale_factor)))
    stand14 = character

    character = pygame.Surface((20,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-463,-15))
    character = pygame.transform.scale(character, (int(20*scale_factor),int(52*scale_factor)))
    stand15 = character

    character = pygame.Surface((20,52),pygame.SRCALPHA)
    character.blit(spritesheet,(-493,-15))
    character = pygame.transform.scale(character, (int(20*scale_factor),int(52*scale_factor)))
    stand16 = character

    character = pygame.Surface((36,46),pygame.SRCALPHA)
    character.blit(spritesheet,(-10,-84))
    character = pygame.transform.scale(character, (int(36*scale_factor),int(46*scale_factor)))
    run1 = character

    character = pygame.Surface((29,46),pygame.SRCALPHA)
    character.blit(spritesheet,(-63,-84))
    character = pygame.transform.scale(character, (int(29*scale_factor),int(46*scale_factor)))
    run2 = character

    character = pygame.Surface((35,46),pygame.SRCALPHA)
    character.blit(spritesheet,(-102,-84))
    character = pygame.transform.scale(character, (int(35*scale_factor),int(46*scale_factor)))
    run3 = character

    character = pygame.Surface((45,46),pygame.SRCALPHA)
    character.blit(spritesheet,(-141,-85))
    character = pygame.transform.scale(character, (int(45*scale_factor),int(46*scale_factor)))
    run4 = character

    character = pygame.Surface((48,46),pygame.SRCALPHA)
    character.blit(spritesheet,(-195,-83))
    character = pygame.transform.scale(character, (int(48*scale_factor),int(46*scale_factor)))
    run5 = character

    character = pygame.Surface((34,46),pygame.SRCALPHA)
    character.blit(spritesheet,(-252,-87))
    character = pygame.transform.scale(character, (int(34*scale_factor),int(46*scale_factor)))
    run6 = character

    character = pygame.Surface((29,46),pygame.SRCALPHA)
    character.blit(spritesheet,(-304,-86))
    character = pygame.transform.scale(character, (int(29*scale_factor),int(46*scale_factor)))
    run7 = character

    character = pygame.Surface((35,46),pygame.SRCALPHA)
    character.blit(spritesheet,(-335,-88))
    character = pygame.transform.scale(character, (int(35*scale_factor),int(46*scale_factor)))
    run8 = character

    character = pygame.Surface((46,46),pygame.SRCALPHA)
    character.blit(spritesheet,(-372,-87))
    character = pygame.transform.scale(character, (int(46*scale_factor),int(46*scale_factor)))
    run9 = character

    character = pygame.Surface((48,46),pygame.SRCALPHA)
    character.blit(spritesheet,(-428,-85))
    character = pygame.transform.scale(character, (int(48*scale_factor),int(46*scale_factor)))
    run10 = character

    character = pygame.Surface((27,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-131,-330))
    character = pygame.transform.scale(character, (int(27*scale_factor),int(61*scale_factor)))
    jump4 = character

    character = pygame.Surface((33,49),pygame.SRCALPHA)
    character.blit(spritesheet,(-284,-326))
    character = pygame.transform.scale(character, (int(33*scale_factor),int(49*scale_factor)))
    jump10 = character

    character = pygame.Surface((32,49),pygame.SRCALPHA)
    character.blit(spritesheet,(-164,-330))
    character = pygame.transform.scale(character, (int(32*scale_factor),int(49*scale_factor)))
    jump11 = character

    """
    #Old jump sprites are below. The above are the two new ones in JumpAnimates.
    character = pygame.Surface((33,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-10,-317))
    character = pygame.transform.scale(character, (int(33*scale_factor),int(61*scale_factor)))
    jump1 = character

    character = pygame.Surface((24,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-49,-319))
    character = pygame.transform.scale(character, (int(24*scale_factor),int(61*scale_factor)))
    jump2 = character

    character = pygame.Surface((26,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-92,-328))
    character = pygame.transform.scale(character, (int(26*scale_factor),int(61*scale_factor)))
    jump3 = character

    character = pygame.Surface((27,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-131,-330))
    character = pygame.transform.scale(character, (int(27*scale_factor),int(61*scale_factor)))
    jump4 = character

    character = pygame.Surface((32,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-164,-332))
    character = pygame.transform.scale(character, (int(32*scale_factor),int(61*scale_factor)))
    jump5 = character

    character = pygame.Surface((37,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-200,-330))
    character = pygame.transform.scale(character, (int(37*scale_factor),int(61*scale_factor)))
    jump6 = character

    character = pygame.Surface((39,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-242,-327))
    character = pygame.transform.scale(character, (int(39*scale_factor),int(61*scale_factor)))
    jump7 = character

    character = pygame.Surface((33,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-284,-326))
    character = pygame.transform.scale(character, (int(33*scale_factor),int(61*scale_factor)))
    jump8 = character

    character = pygame.Surface((31,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-324,-318))
    character = pygame.transform.scale(character, (int(31*scale_factor),int(61*scale_factor)))
    jump9 = character

    character = pygame.Surface((25,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-369,-322))
    character = pygame.transform.scale(character, (int(25*scale_factor),int(61*scale_factor)))
    jump10 = character

    character = pygame.Surface((29,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-407,-316))
    character = pygame.transform.scale(character, (int(29*scale_factor),int(61*scale_factor)))
    jump11 = character

    character = pygame.Surface((28,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-447,-316))
    character = pygame.transform.scale(character, (int(28*scale_factor),int(61*scale_factor)))
    jump12 = character

    character = pygame.Surface((28,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-486,-317))
    character = pygame.transform.scale(character, (int(28*scale_factor),int(61*scale_factor)))
    jump13 = character

    character = pygame.Surface((28,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-527,-317))
    character = pygame.transform.scale(character, (int(28*scale_factor),int(61*scale_factor)))
    jump14 = character

    character = pygame.Surface((28,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-572,-323))
    character = pygame.transform.scale(character, (int(28*scale_factor),int(61*scale_factor)))
    jump15 = character

    character = pygame.Surface((28,61),pygame.SRCALPHA)
    character.blit(spritesheet,(-615,-325))
    character = pygame.transform.scale(character, (int(28*scale_factor),int(61*scale_factor)))
    jump16 = character
    """
