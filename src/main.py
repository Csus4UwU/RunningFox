import pygame
import sys
import image, fox
from const import *

pygame.init()

DS = pygame.display.set_mode(ScreenSize)
pygame.display.set_icon(pygame.image.load("pic/icon/fox-tail2.png"))

pygame.display.set_caption("akiba!")

Background = image.Image("pic/background/snowland1.png", 0, (0, 0), ScreenSize)
# action1 = "walk"
# Fox1 = image.Image(FoxActionPath[action1], 1, (100, 500), Foxsize, IdxCount[action1])
Fox2 = fox.Fox(WALK, (0, 600))
Fox3 = fox.Fox(SLEEP, (500, 500))
walktime = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DS.fill((255, 255, 255))
    Background.draw(DS)
    # Fox1.draw(DS)
    # Fox1.Update(FoxSpeed["walk"])
    if walktime <= 50:
        Fox2.draw(DS)
        Fox2.FoxUpdate()
        walktime += 1
    else:
        Fox3.pos = Fox2.pos
        Fox3.draw(DS)
        Fox3.FoxUpdate()
    pygame.display.update()
