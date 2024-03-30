import pygame
import sys
import image, fox
from const import *

pygame.init()

DS = pygame.display.set_mode(ScreenSize)
pygame.display.set_icon(pygame.image.load("pic/icon/fox-tail2.png"))

pygame.display.set_caption("akiba!")

Background = image.Image("pic/background/snowland1.png", 0, (0, 0), ScreenSize)
# Fox1 = fox.Fox("walk", (100, 500))
action1 = "walk"
Fox1 = image.Image(FoxActionPath[action1], 1, (100, 500), Foxsize, IdxCount[action1])
Fox2 = fox.Fox("walk", (100, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DS.fill((255, 255, 255))
    Background.draw(DS)
    Fox2.draw(DS)
    Fox1.draw(DS)
    Fox1.Update(FoxSpeed["walk"])
    Fox2._walk()

    pygame.display.update()
