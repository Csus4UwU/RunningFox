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
        self.dir = [0, 0]  # 1,-1,0(init)

    def UpdateAction(self, newaction):
        self.action = newaction

    def CheckSpeed(self, action=WALK):
        # self.speed[0] = (self.destination[0] - self.pos[0]) / 60
        # self.speed[1] = (self.destination[1] - self.pos[1]) / 60
        for i in range(2):
            if abs((self.destination[0] - self.pos[i]) / fps) > abs(
                FoxSpeed[action][i]
            ):
                self.speed[i] = (self.destination[i] - self.pos[i]) / fps
            else:
                self.speed[i] = FoxSpeed[action][i]

    def UpdateDest(self, npos):
        self.destination = npos
        self.CheckSpeed()

    def UpdateDir(self):
        if self.destination[0] - self.pos[0] >= 0:
            self.dir[0] = 1
        else:
            self.dir[0] = -1
        if self.destination[1] - self.pos[1] >= 0:
            self.dir[1] = -1
        else:
            self.dir[1] = 1

    def CheckIfArrive(self):
        flagx = False
        flagy = False
        if self.dir[0] == 1 and self.pos[0] >= self.destination[0]:
            flagx = True
        if self.dir[1] == 1 and self.pos[1] >= self.destination[1]:
            flagy = True
        if self.dir[0] == -1 and self.pos[0] <= self.destination[0]:
            flagx = True
        if self.dir[1] == -1 and self.pos[1] <= self.destination[1]:
            flagy = True
        if flagx and flagy:
            return True
        return False

    def FoxCheck(self, npos):
        if npos != self.destination:
            self.UpdateDest(npos)
            self.UpdateDir()
        # self.CheckSpeed()
        if self.CheckIfArrive():
            self.UpdateAction(SLEEP)

    def FoxUpdate(self):
        self.Update(self.speed, FoxActionPath[self.action])
        print(self.action)
