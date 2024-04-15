import pygame
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

    def GetPos(self):
        return pygame.mouse.get_pos()

    def GetXpos(self):
        return pygame.mouse.get_pos()[0] - 64

    def GetYpos(self):
        return pygame.mouse.get_pos()[1] - 100
