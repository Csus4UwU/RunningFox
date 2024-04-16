import image
from const import *


class GameMap(image.Image):
    def __init__(self, index) -> None:
        self.mapidx = index
        if index == 1:
            self.pathFmt = "pic/background/snowland1.png"
        elif index == 2:
            self.pathFmt = "pic/background/bg3.png"
        super().__init__(self.pathFmt, 0, (0, 0), ScreenSize)

    def Correct(self, pos):
        if self.mapidx == 1:
            if pos[1] > ScreenSize[1]:
                pos[1] = ScreenSize[1]
            elif pos[1] < -pos[0] * 0.234375 + 420:
                pos[1] = -pos[0] * 0.234375 + 420
        return pos
