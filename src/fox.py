import image
from const import *


class Fox(image.Image):
    def __init__(self, action, pos):
        super(Fox, self).__init__(
            FoxActionPath[action], 0, pos, Foxsize, IdxCount[action]
        )
        self.action = action
        self.destination = (0, 0)
        self.speed = list((0, 0))

    def ChangeAction(self, newaction):
        self.action = newaction

    def CheckDestination(self, npos):
        self.destination = npos

    def CheckSpeed(self, action=WALK):
        self.speed[0] = (self.destination[0] - self.pos[0]) / 60
        self.speed[1] = (self.destination[1] - self.pos[1]) / 60
        # for i in range(2):
        #     if abs((self.destination[0] - self.pos[i]) / fps) > abs(
        #         FoxSpeed[action][i]
        #     ):
        #         self.speed[i] = (self.destination[i] - self.pos[i]) / fps
        #     else:
        #         self.speed[i] = FoxSpeed[action][i]

    def FoxCheck(self, npos):
        self.CheckDestination(npos)
        self.CheckSpeed()
        if self.pos == self.destination:
            self.ChangeAction(SLEEP)

    def FoxUpdate(self):
        self.Update(self.speed)
