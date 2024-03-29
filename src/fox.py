import image
from const import *


class Fox(image.Image):
    def __init__(self, action, pos):
        super(Fox, self).__init__(
            "pic/fox/" + action + "/%d.png", pos, Foxsize, IdxCount[action]
        )
