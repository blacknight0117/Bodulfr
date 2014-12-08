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
        pygame.display.update()
        Vars.FPSCLOCK.tick(Vars.FPS)


class MainMenuState():
    def __init__(self):
        self.state = FrontState()
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
                        self.state = self.state.Select()
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
        self.titleString = 'Bodulfr'
        self.titleText = []
        self.menuText = []
        self.highlight = -1
        self.entering = True
        self.timeStep = 0

        self.Setup()

    def Setup(self):
        self.menuText = [Vars.Text('New Game', Vars.TESTFONT2, 30, Vars.WHITE, Vars.BLACK),
                         Vars.Text('Continue', Vars.TESTFONT2, 30, Vars.WHITE, Vars.BLACK),
                         Vars.Text('Options', Vars.TESTFONT2, 30, Vars.WHITE, Vars.BLACK),
                         Vars.Text('Settings', Vars.TESTFONT2, 30, Vars.WHITE, Vars.BLACK),
                         Vars.Text('Extras', Vars.TESTFONT2, 30, Vars.WHITE, Vars.BLACK)]
        temp1 = []
        temp2 = []
        for char in self.titleString:
            temp1.append(Vars.Text(char, Vars.TESTFONT, 90, Vars.WHITE, Vars.BLACK))
            temp2.append(Vars.Text(char, Vars.TESTFONT2, 70, Vars.WHITE, Vars.BLACK))
        self.titleText.append(temp1)
        self.titleText.append(temp2)
        self.titleText[0][3].rect.centerx = Vars.WINXCTR
        self.titleText[1][3].rect.centerx = Vars.WINXCTR
        for i in range(2, -1, -1):
            if self.titleText[0][i+1].rect.left < self.titleText[1][i+1].rect.left:
                self.titleText[0][i].rect.right = self.titleText[0][i+1].rect.left
                self.titleText[1][i].rect.right = self.titleText[0][i+1].rect.left
            else:
                self.titleText[0][i].rect.right = self.titleText[1][i+1].rect.left
                self.titleText[1][i].rect.right = self.titleText[1][i+1].rect.left
        for i in range(4, 7, 1):
            if self.titleText[0][i-1].rect.right > self.titleText[1][i-1].rect.right:
                self.titleText[0][i].rect.left = self.titleText[0][i-1].rect.right
                self.titleText[1][i].rect.left = self.titleText[0][i-1].rect.right
            else:
                self.titleText[0][i].rect.left = self.titleText[1][i-1].rect.right
                self.titleText[1][i].rect.left = self.titleText[1][i-1].rect.right
        for i in range(7):
            self.titleText[1][i].ChangeAlpha(0)
            self.titleText[0][i].rect.centery = Vars.WINYCTR
            self.titleText[1][i].rect.centery = 150

        for i in range(len(self.menuText)):
            self.menuText[i].surf.set_alpha(0)
            self.menuText[i].rect.left = (Vars.WINXCTR/2)
            if i == 0:
                self.menuText[i].rect.top = 300
            else:
                self.menuText[i].rect.top = self.menuText[i-1].rect.bottom+10

    def Select(self):
        print('Select')
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
        print('Up')
        if self.highlight > 0:
            self.highlight -= 1

    def Dn(self):
        print('Down')
        if self.highlight < 4:
            self.highlight += 1

    def Draw(self):
        #self.titleTemp.Draw()
        for i in range(7):
            self.titleText[0][i].Draw()
            self.titleText[1][i].Draw()
        for i in range(len(self.menuText)):
            self.menuText[i].Draw()
        if self.highlight >= 0:
            temp = self.menuText[self.highlight].rect
            pygame.draw.rect(Vars.DISPLAYSURF, Vars.WHITE, (temp.left-20, temp.top, temp.width+40, 2))
            pygame.draw.rect(Vars.DISPLAYSURF, Vars.WHITE, (temp.left-20, temp.bottom, temp.width+40, 2))

    def Update(self):
        if self.timeStep > 239:
            self.entering = False
        if self.entering and self.timeStep < 90:
            changePer = float((Vars.WINYCTR-150)/90)
            temp = math.floor(changePer*self.timeStep)
            temp = Vars.WINYCTR - temp
            if temp < self.titleText[0][0].rect.centery:
                for i in range(7):
                    self.titleText[0][i].rect.centery = temp
            self.timeStep += 1
        elif self.entering and self.timeStep < 120:
            changePer = float(256/30)
            temp = math.floor(changePer*(self.timeStep-90))
            for i in range(len(self.menuText)):
                self.menuText[i].ChangeAlpha(temp)
            self.timeStep += 1
        elif self.entering and self.timeStep < 240:
            changePer = float(256/120)
            temp = math.floor(changePer*(self.timeStep-120))
            tempB = 256-temp
            for i in range(7):
                self.titleText[0][i].ChangeAlpha(tempB)
                self.titleText[1][i].ChangeAlpha(temp)
            self.timeStep += 1


class tempState():
    def __init__(self):
        pass


#TODO: Determine if a terminate is required for this file
def Terminate():
    pass