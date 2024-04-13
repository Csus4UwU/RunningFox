import pygame
from const import *


class Mouse:
    def __init__(self) -> None:
        self.pos = [0, 0]
        self.IsLeftPressed = 0
        self.IsMidPressed = 0
        self.IsRightPressed = 0

    def UpdateIsPressed(self):
        self.IsLeftPressed = pygame.mouse.get_pressed()[0]
        self.IsMidPressed = pygame.mouse.get_pressed()[1]
        self.IsRightPressed = pygame.mouse.get_pressed()[2]

    def GetPos(self):
        return pygame.mouse.get_pos()
