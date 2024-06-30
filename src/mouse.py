import pygame
import gamemap
from const import *


class Mouse:
    def __init__(self) -> None:
        self.pos = [0, 0]
        self.IsLeftPressed = False
        self.IsMidPressed = False
        self.IsRightPressed = False

    def UpdateIsPressed(self):
        self.IsLeftPressed = pygame.mouse.get_pressed()[0]
        self.IsMidPressed = pygame.mouse.get_pressed()[1]
        self.IsRightPressed = pygame.mouse.get_pressed()[2]

    def CheckPos(self, mapidx):
        self.GetPos()
        self.Correct(mapidx)
        return self.pos

    def GetPos(self):
        self.pos = list(pygame.mouse.get_pos())
        self.pos[0] = self.pos[0] - 64
        self.pos[1] = self.pos[1] - 100

    def Correct(self, mapidx):
        self.pos[0]=min(self.pos[0],1280)
        self.pos[0]=max(self.pos[0],0)
        self.pos[1]=min(self.pos[1],720)
        self.pos[1]=max(self.pos[1],0)
        if mapidx==1 :
            pass
