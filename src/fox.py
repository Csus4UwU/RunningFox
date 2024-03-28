import pygame
import image
from const import *


class Fox:
    def __init__(self, pos, Xspeed=0, Yspeed=0):
        self.pos = pos
        self.Xspeed = Xspeed
        self.Yspeed = Yspeed

    def UpdateSpeed(self, NewXspeed, NewYspeed):
        self.Xspeed = NewXspeed
        self.Yspeed = NewYspeed

    def UpdatePosition(self):
        pass
