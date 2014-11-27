__author__ = 'blacKnight'
#Created: Aug 31,2013
#By: Nathan Black
import pygame
import MainMenu
import copy
import math
from pygame.locals import *

#This file will hold global variables/functions needed
#  at almost every level of the architecture along with
#   functions asssociated with those global variables
#EX - DisplaySurface, ControllerData, Controller/Text/Font Class
pygame.init()

DISPLAYSURF = None
WINWIDTH = 1000
WINHEIGHT = 1000
WINXCTR = WINWIDTH/2
WINYCTR = WINHEIGHT/2
FPS = 10  # frames per second to update the screen
FPSCLOCK = None
CONTROLLERCOUNT = pygame.joystick.get_count()
CONTROLLERS = []
MAINCONT = 0
BTNDICT = {'0': 'select', '1': 'back', '2': 'options'}
AXISDICT = {'0': 'vertMove', '1': 'horiMove', '2': 'trigger'}
PREFFILE = open('Preferences.txt', 'r')
PREFFILE.close()

#anglosaxonrunes, floki-Hard, Gaya Z, rune_ice, RUNENG1, RUNENG2, Viking
TESTFONT = 'anglosaxonrunes.ttf'
TESTFONT2 = 'floki-Hard.ttf'

BLACK       = (0,   0,   0)
WHITE       = (255, 255, 255)
RED         = (50,  0,   0)
DARKRED     = (175, 0,   0)
GREEN       = (0,   255, 0)
TOOLBARGREY = (50,  50,  50)
DARKGREY    = (100, 100, 100)
MEDGREY     = (150, 150, 150)
LIGHTGREY   = (200, 200, 200)
#TODO: Angle of thumbstick input
#TODO: Abs Distance of thumbstick input
#TODO: Floor based on increment?!?!
#TODO: Change thumbstick input (floor amount)


class Controllers():
    def __init__(self):
        self.cont = None
        self.buttonCnt = None
        self.axisCnt = None

    def Setup(self, aCont):
        self.cont = aCont
        self.buttonCnt = aCont.get_numbuttons()
        self.axisCnt = aCont.get_numaxes()


class Font():
    def __init__(self, aFile, aSize):
        self.fontFile = aFile
        self.fontSize = aSize
        self.font = None
        self.Setup()

    def Setup(self):
        self.font = pygame.font.Font(self.fontFile, self.fontSize)


class Text():
    def __init__(self, someText, aFontFile, aFontSize, textColor=WHITE, bgColor=BLACK):
        self.text = someText
        self.selected = False   #TODO: Add selected change in draw
        self.loc = [0, 0]
        self.font = Font(aFontFile, aFontSize)
        self.surf = None
        self.rect = None
        self.color = textColor
        self.bgColor = bgColor
        self.Setup()

    #Initialize fontRect
    def Setup(self):
        self.surf = self.font.font.render(self.text, 1, self.color, self.bgColor)
        self.surf = self.surf.convert_alpha()
        self.rect = self.surf.get_rect()

    #Draws border if selected, else just output to DisplaySurf
    def Draw(self):
        if not self.selected:
            pass
        DISPLAYSURF.blit(self.surf, self.rect)

    def ChangeSize(self, increment):
        #TODO: changes size of font, change to font as well
        pass

    def ChangeAlpha(self, aVal):
        self.surf.set_alpha(aVal)


#mainMenuTtlFont = Font(70, 'celticmd2.ttf')
#mainMenuTtlText = Text('Bodulfr', mainMenuTtlFont, WHITE, BLACK):
#mainMenuTtlText.fontRect.Top = 100
#mainMenuTtlText.fontRect.centerx = WINXCTR


