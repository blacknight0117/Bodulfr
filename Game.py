__author__ = 'Black'
import sys
import os
import copy
import math
import Main
import Vars
import pygame
import decimal
from decimal import *
from pygame.locals import *

CHARSPEED = 10


#Starts the GameState
def mainLoop(initial):
    if initial == 'dev':
        devState = None
        theGameState = GameStateManager(DeveloperState())
    else:
        theGameState = None

        while True:
            theGameState.Interact()
            theGameState.Update()
            theGameState.Draw()


#Center of the main GameState
class GameStateManager():
    def __init__(self, initialState):
        self.currentState = initialState
        self.backState = MenuState()
        self.mainChar = MainChar()
        self.actors = []
        self.background = None
        self.dirtyRects = []
        self.dirtyActors = []
        self.joyData = Joy()

    def Interact(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                Main.Terminate()
            elif event.type == JOYAXISMOTION:
                if event.axis == 0:
                    self.joyData.leftX = Decimal(event.value)
                    self.mainChar.Move(self.joyData.leftX, self.joyData.leftY)
                elif event.axis == 1:
                    self.joyData.leftY = Decimal(event.value)
                    self.mainChar.Move(self.joyData.leftX, self.joyData.leftY)
                elif event.axis == 2:
                    self.joyData.trigger = Decimal(event.value)
                elif event.axis == 3:
                    self.joyData.rightY = Decimal(event.value*-1)
                    self.mainChar.Turn(self.joyData.rightX, self.joyData.rightY)
                elif event.axis == 4:
                    self.joyData.rightX = Decimal(event.value)
                    self.mainChar.Turn(self.joyData.rightX, self.joyData.rightY)
                #TODO: Move or turn main char
            elif event.type == JOYBUTTONDOWN:
                pass
            elif event.type == JOYHATMOTION:
                pass

    #updates all actors
    def Update(self):
        for i in range(len(self.actors)):
            if self.actors[i].needsUpdate:
                self.actors[i].Update()

    #refills dirty rects(overlaps allowed)
    #Draws all dirty actors that need drawing
    def Draw(self):
        while len(self.dirtyRects) > 0:
            Vars.DISPLAYSURF.blit(self.background, self.dirtyRects[0], self.dirtyRects[0])
            self.dirtyRects.remove(0)
        while len(self.dirtyActors) > 0:
            self.dirtyActors[0].Draw()
            self.dirtyActors.remove(0)


#Menus for in game
class MenuState():
    def __init__(self):
        pass


#Main Char controls
class MainChar():
    def __init__(self):
        self.screenPos = [0, 0]
        self.imageList = []     # depending on conditions
        self.rects = []
        self.direction = 4   # 0 is up, 8 pos clockwise
        self.inventory = []
        self.equipped = []
        self.Setup()

    def Setup(self):
        self.imageList.append(pygame.image.load('MainUp.png'))
        self.imageList.append(pygame.image.load('MainUpRt.png'))
        self.imageList.append(pygame.image.load('MainRt.png'))
        self.imageList.append(pygame.image.load('MainDnRt.png'))
        self.imageList.append(pygame.image.load('MainDn.png'))
        self.imageList.append(pygame.image.load('MainDnLt.png'))
        self.imageList.append(pygame.image.load('MainLt.png'))
        self.imageList.append(pygame.image.load('MainUpLt.png'))
        self.rects.append(pygame.Rect(0, 0, 12, 20))
        self.rects.append(pygame.Rect(0, 0, 20, 12))
        self.rects.append(pygame.Rect(0, 0, 20, 20))

    def Draw(self):
        if self.direction == 0 or self.direction == 4:
            Vars.DISPLAYSURF.blit(self.imageList[self.direction], self.rects[0])
        elif self.direction == 2 or self.direction == 6:
            Vars.DISPLAYSURF.blit(self.imageList[self.direction], self.rects[1])
        else:
            Vars.DISPLAYSURF.blit(self.imageList[self.direction], self.rects[2])

    def Move(self, axisX, axisY):
        self.screenPos[0] += Vars.MOVESPEED * axisX
        self.screenPos[1] += Vars.MOVESPEED * axisY
        self.rects[0].center = self.screenPos
        self.rects[1].center = self.screenPos
        self.rects[2].cetner = self.screenPos

    def Turn(self, axisX, axisY):
        if (Vars.DIRLIMIT * -1) <= axisX <= Vars.DIRLIMIT:
            if axisY > Vars.DIRLIMIT:
                self.direction = 0
            elif axisY < (Vars.DIRLIMIT * -1):
                self.direction = 4
        elif axisX < (Vars.DIRLIMIT * -1):
            if axisY > Vars.DIRLIMIT:
                self.direction = 7
            elif axisY < (Vars.DIRLIMIT * -1):
                self.direction = 5
            else:
                self.direction = 6
        elif axisX > Vars.DIRLIMIT:
            if axisY > Vars.DIRLIMIT:
                self.direction = 1
            elif axisY < (Vars.DIRLIMIT * -1):
                self.direction = 3
            else:
                self.direction = 2


#Actor Class
class Actor():
    def __init__(self):
        pass


class DeveloperState():
    def __init__(self):
        pass


class Joy():
    def __init__(self):
        self.leftX = 0
        self.leftY = 0
        self.rightX = 0
        self.rightY = 0
        self.trigger = 0


def GetAngle(axisX, axisY):
    axisX = Decimal(axisX)
    axisY = Decimal(axisY)
    axisY *= -1
    return math.degrees(math.atan2(axisY, axisX))