import pygame
from const import *
import time


class Image(pygame.sprite.Sprite):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        self.pathFmt = pathFmt
        self.pathIndex = pathIndex
        self.pathIndexCount = pathIndexCount
        self.pos = list(pos)
        self.size = size
        self.UpdateImage()

    def UpdateImage(self):
        path = self.pathFmt
        if self.pathIndexCount != 0:
            path = path % self.pathIndex
        self.image = pygame.image.load(path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    def UpdateIndex(self, pathIndex):
        self.pathIndex = pathIndex
        self.UpdateImage()

    def UpdatePath(self, pathFmt, pathIndexCount):
        if pathFmt != self.pathFmt:
            self.pathIndex = 1
        self.pathFmt = pathFmt
        self.pathIndexCount = pathIndexCount
        self.UpdateImage()

    def UpdateSize(self, size):
        self.size = size
        self.UpdateImage()

    def CheckImageIndex(self):
        idx = (self.pathIndex + 1) % self.pathIndexCount
        self.UpdateIndex(idx)

    def CheckPosition(self, speed):
        self.pos[0] += speed[0]
        self.pos[1] += speed[1]

    def Update(self, speed, path, idxcount):
        self.UpdatePath(path, idxcount)
        self.CheckImageIndex()
        self.CheckPosition(speed)

    def GetRect(self):
        rect = self.image.get_rect()
        rect.x, rect.y = self.pos
        return rect

    def DoLeft(self):
        self.pos[0] -= 1

    def DoRight(self):
        self.pos[0] += 1

    def DoUp(self):
        self.pos[1] -= 1

    def DoDown(self):
        self.pos[1] += 1

    def draw(self, ds):
        ds.blit(self.image, self.GetRect())
