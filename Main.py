__author__ = 'blacKnight'
#Bodulfr pre-alpha
#By: Nathan Black, 8/29/2014
import random
import copy
import os
import sys
import Vars
import MainMenu
import Game
import pygame
from pygame.locals import *


#TODO Main Menu - MainMenu.py
#TODO Options
#TODO SinglePlayer Launch
#----------------------------------------------
#TODO: Get example thumbstick inputs from a controller
#       TODO: -Program Thumb Angle, Thumb Dist, Thumb Dir

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

    extras = MainMenu.main()
    print(extras)
    if extras == 'dev':
        Game.mainLoop('dev')
    else:
        Game.mainLoop('')


#Splash Screen Function
def SplashScreen():
    #TODO Splash screen - SKIP FOR NOW
    pass


#Intro Videos Function
def IntroVids():
    #TODO: INTRO VID - SKIP FOR NOW
    pass


#Displays push a button text till a button is pushed and main cont is set
def InitConts():
    for i in range(Vars.CONTROLLERCOUNT):
        Vars.CONTROLLERS.append(pygame.joystick.Joystick(i))
        Vars.CONTROLLERS[i].init()
        introText = Vars.Text('Push a Button', Vars.TESTFONT2, 30, Vars.WHITE, Vars.BLACK)
        introText.rect.center = Vars.WINXCTR, Vars.WINYCTR
        notDone = True
        while notDone:
            Vars.DISPLAYSURF.fill(Vars.BLACK)
            introText.Draw()
            for event in pygame.event.get():
                if event.type == JOYBUTTONDOWN:
                    if Vars.MAINCONT == -1:
                        Vars.MAINCONT = event.joy
                        notDone = False
            pygame.display.update()
            Vars.FPSCLOCK.tick(Vars.FPS)


#Exits program
def Terminate():
    Vars.PREFFILE.close()
    pygame.quit()
    sys.exit()

#starts program with "main" function
if __name__ == '__main__':
    main()