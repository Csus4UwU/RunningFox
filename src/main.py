import pygame
import sys
import image
from const import *

pygame.init()

DS = pygame.display.set_mode(ScreenSize)
pygame.display.set_icon(pygame.image.load("pic/icon/fox-tail2.png"))

pygame.display.set_caption("akiba!")

Background = image.Image("pic/background/bg1.png", 0, (0, 0), ScreenSize)
Fox1 = image.Image("pic/fox/walk/%d.jpg", 1, (100, 500), Foxsize, IdxCount.walk)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DS.fill((255, 255, 255))
    Background.draw(DS)
    Fox1.draw(DS)
    Fox1.Update()

    pygame.display.update()
