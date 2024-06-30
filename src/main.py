# from akiba import *
import pygame
import mouse
import fox
from const import *
import os
import sys
import gamemap

pygame.init()

DS = pygame.display.set_mode(ScreenSize)
pygame.display.set_icon(pygame.image.load("pic/icon/fox-tail2.png"))
pygame.display.set_caption("akiba!")

Background = gamemap.GameMap(1)
# Background = image.Image("pic/background/snowland1.png", 0, (0, 0), ScreenSize)
Fox2 = fox.Fox(WALK, (100, 500))
UserMouse = mouse.Mouse()

flag1 = 0
d1 = (500, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DS.fill(WHITE)
    Background.draw(DS)
    UserMouse.UpdateIsPressed()
    if UserMouse.IsLeftPressed:
        d1 = tuple(UserMouse.CheckPos(Background.mapidx))
    Fox2.FoxCheck(d1)
    Fox2.FoxUpdate()
    Fox2.draw(DS)

    pygame.display.update()
    pygame.time.Clock().tick(fps)
