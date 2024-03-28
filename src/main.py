import pygame
import sys
import image
from const import *

pygame.init()

DS = pygame.display.set_mode(ScreenSize)
pygame.display.set_icon(pygame.image.load("pic/icon/fox-tail2.png"))

pygame.display.set_caption("akiba!")

Background = image.Image("pic/background/bg3.png", 0, (0, 0), ScreenSize)
Fox1 = image.Image("pic/fox/stand/%d.jpg", 1, (600, 300), (128, 128), IdxCount.stand)

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
