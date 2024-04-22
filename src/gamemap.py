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
