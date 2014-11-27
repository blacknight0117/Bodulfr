__author__ = 'blacknight'
import sys
import os
import copy
import random
import pygame
from pygame.locals import *


keyDict = {'a': K_a,
           'b': K_b,
           'c': K_c,
           'd': K_d,
           'e': K_e,
           'f': K_f,
           'g': K_g,
           'h': K_h,
           'i': K_i,
           'j': K_j,
           'k': K_k,
           'l': K_l,
           'm': K_m,
           'n': K_n,
           'o': K_o,
           'p': K_p,
           'q': K_q,
           'r': K_r,
           's': K_s,
           't': K_t,
           'u': K_u,
           'v': K_v,
           'w': K_w,
           'x': K_x,
           'y': K_y,
           'z': K_z,
           '0': K_0,
           '1': K_1,
           '2': K_2,
           '3': K_3,
           '4': K_4,
           '5': K_5,
           '6': K_6,
           '7': K_7,
           '8': K_8,
           '9': K_9,
           'space': K_SPACE,
           'tab': K_TAB,
           'ctrl': KMOD_CTRL,
           'alt': KMOD_ALT,
           'shift': KMOD_SHIFT,
           'caps': KMOD_CAPS,
           'enter': K_KP_ENTER,
           }

#This hold key bindings for the game, initializes of file
class Keys():
    def __init__(self, aFile):
        self.bindings = {}
        self.Setup(aFile)

    def Setup(self, file):
        fileData = open(file, 'r')
        for line in fileData:
            self.SetBind(line)

    def SetBind(self, aLine):
        counter = 0
        temp = ''
        key = ''
        aVal = None
        aList = []
        while counter < len(aLine):
            if str(aLine[counter]) != ' ':
                temp += aLine[counter].lower()
            else:
                if key == '':
                    key = temp
                    temp = ''
                elif aVal is None:
                    aVal = temp
                else:
                    aList.append(copy.deepcopy(aVal))