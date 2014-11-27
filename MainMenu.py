__author__ = 'blacknight'
import sys
import os
import copy
import math
import Main
import Vars
import pygame
from pygame.locals import *

#TODO: NEWGAME State
#TODO: Options State
#TODO: SAVE FILE IO -> Vars.py
#TODO: PREF FILE IO -> Vars.py


#Everything in this script are reasonably self-suficient and does not require
#other functions (other than vars from Vars.py) to draw and update/interact
def main():
    toGame = False
    manager = MainMenuState()
    while not toGame:
        manager.Input()
        toGame = manager.Update()
        manager.Draw()


class MainMenuState():
    def __init__(self):
        self.state = None
        self.buttons = []
        self.axes = []
        self.hats = []
        self.entering = True
        self.Setup()

    def Setup(self):
        #populate buttons, axes, state, enviro, menus, actors
        for i in range(Vars.CONTROLLERS[Vars.MAINCONT].get_numbuttons()):
            self.buttons.append(Vars.CONTROLLERS[Vars.MAINCONT].get_button(i))
        for i in range(Vars.CONTROLLERS[Vars.MAINCONT].get_numaxes()):
            self.axes.append(Vars.CONTROLLERS[Vars.MAINCONT].get_axis(i))

    def Input(self):
        for event in pygame.event.get():
            if self.entering:
                pass
            if event.type == QUIT:
                Main.Terminate()
            elif event.type == JOYBUTTONDOWN:
                if event.joy == Vars.MAINCONT:
                    if event.button == 0:           # a button
                        self.state.Select()
                    elif event.button == 1:         # b button
                        self.state.Back()
            elif event.type == JOYHATMOTION:
                if event.joy == Vars.MAINCONT:
                    if event.hat == 0:
                        if event.value[0] == 1:     # Hat right
                            self.state.Rt()
                        elif event.value[0] == -1:  # Hat Left
                            self.state.Lt()
                        if event.value[1] == 1:     # Hat Up
                            self.state.Up()
                        elif event.value[1] == -1:  # Hat Down
                            self.state.Dn()

    def Update(self):
        self.state.Update()
        return False

    def Draw(self):
        Vars.DISPLAYSURF.fill(Vars.BLACK)
        self.state.Draw()


#This state handles the initial front screen of main menu
#New Game, Continue, Options, Settings, Extra
class FrontState():
    def __init__(self):
        self.titleText = Vars.Text('Bodulfr', Vars.TESTFONT, 30)
        self.menuText = []
        self.highlight = -1
        self.entering = True
        self.timeStep = 0

        self.Setup()

    def Setup(self):
        self.menuText = [Vars.Text('New Game', Vars.TESTFONT2, 20),
                         Vars.Text('Continue', Vars.TESTFONT2, 20),
                         Vars.Text('Options', Vars.TESTFONT2, 20),
                         Vars.Text('Settings', Vars.TESTFONT2, 20),
                         Vars.Text('Extras', Vars.TESTFONT2, 20)]

    def Select(self):
        if 4 >= self.highlight >= 0:
            if self.highlight == 0:
                return tempState()      # NewGameState
            elif self.highlight == 1:
                return tempState()      # ContinueState
            elif self.highlight == 2:
                return tempState()      # OptionState
            elif self.highlight == 3:
                return tempState()      # SettingState
            elif self.highlight == 4:
                return tempState()      # ExtraState

    def Back(self):
        pass

    def Rt(self):
        pass

    def Lt(self):
        pass

    def Up(self):
        if self.highlight > 0:
            self.highlight -= 1

    def Dn(self):
        if self.highlight < 4:
            self.highlight += 1

    def Draw(self):
        self.titleText.Draw()
        for i in range(len(self.menuText)):
            self.menuText[i].Draw()

    def Update(self):
        if self.timeStep > 119:
            self.entering = False
        elif self.timeStep > 89:
            step = 1
        else:
            step = 0
        if self.entering and step == 0:
            changePer = float((Vars.WINHEIGHT-100)/90)
            temp = math.floor(changePer*self.timeStep)
            temp += Vars.WINYCTR
            if temp > self.titleText.rect.centery:
                self.titleText.rect.centery = temp
            self.timeStep += 1
        elif self.entering and step == 1:
            changePer = float(256/30)
            temp = math.floor(changePer*self.timeStep-90)
            for i in range(len(self.menuText)):
                self.menuText[i].ChangeAlpha(temp)
            self.timeStep += 1

'''
titleFont = Vars.Font('celticmd2.ttf', 70)
        self.title = Vars.Text('Bodulfr', titleFont, Vars.WHITE, None)
        self.title.rect.centerx = Vars.WINXCTR
        self.title.rect.top = 100
'''


class tempState():
    def __init__(self):
        pass


#TODO: Determine if a terminate is required for this file
def Terminate():
    pass