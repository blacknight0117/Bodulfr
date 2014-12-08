__author__ = 'blacKnight'
#Bodulfr pre-alpha
#By: Nathan Black, 8/29/2014
import random
import copy
import os
import sys
import pygame
import Vars
import MainMenu
from pygame.locals import *

#TODO Splash screen - SKIP FOR NOW
#TODO Main Menu - MainMenu.py
#TODO Options
#TODO SinglePlayer Launch
#----------------------------------------------
#TODO: Get example thumbstick inputs from a controller
#       TODO: -Program Thumb Angle, Thumb Dist, Thumb Dir

#needed stuff
#Menu class
#Popup class
#Toolbar class
#general layout with default functions

#INGAME
#environment class
#enemy class
#player class

#General Shit
#l = topLeft base location [lx,ly]
#for g in blah, h in blah, i in blah


#Main Start Function
def main():

    pygame.init()

    Vars.DISPLAYSURF = pygame.display.set_mode((Vars.WINWIDTH, Vars.WINHEIGHT))
    Vars.FPSCLOCK = pygame.time.Clock()

    SplashScreen()
    IntroVids()
    InitConts()

    MainMenu.main()

    #while exitBool == 0, gameLoop keeps being looped
    exitBool = False
    while not exitBool:
        pass
        '''
        #interactions
        #update
        #save/load
        #draw

            #background tiles
            #player movement and action
            #enemy random movement
            #Controller Based Design
        '''


#Splash Screen Function
def SplashScreen():
    pass


#Intro Videos Function
def IntroVids():
    pass


def InitConts():
    for i in range(Vars.CONTROLLERCOUNT):
        Vars.CONTROLLERS.append(pygame.joystick.Joystick(i))
        Vars.CONTROLLERS[i].init()


#Exits program
def Terminate():
    Vars.PREFFILE.close()
    pygame.quit()
    sys.exit()

#starts program with "main" function
if __name__ == '__main__':
    main()