import image
from const import *


class Fox(image.Image):
    def __init__(self, action, pos):
        super(Fox, self).__init__(
            FoxActionPath[action], 0, pos, Foxsize, IdxCount[action]
        )
        self.action = action

    def FoxUpdate(self):
        if self.action != SLEEP:
            self.Update(FoxSpeed[self.action])
        else:
            self.Update(FoxSpeed[SLEEP], 0.2)
