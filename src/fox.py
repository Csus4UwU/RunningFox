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
        self.timer = 0

    def UpdateAction(self, newaction):
        self.action = newaction

    def UpdateSpeed(self, speedX, speedY):
        self.speed[0] = speedX
        self.speed[1] = speedY

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

    def CheckDir(self):
        for i in range(2):
            if self.dir[i] == -1:
                self.speed[i] = -self.speed[i]
        if self.dir[0] == -1:
            self.Xrev = True
        else:
            self.Xrev = False

    def UpdateDest(self, npos):
        self.destination = npos
        self.CheckSpeed()
        self.UpdateDir()
        self.CheckDir()

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

    def StStop(self):
        self.UpdateAction(REST)
        self.UpdateSpeed(0, 0)

    def StMove(self, npos):
        self.UpdateAction(WALK)
        self.UpdateDest(npos)
        self.UpdateDir()

    def FoxCheck(self, npos):
        if npos != self.destination:
            self.StMove(npos)
            self.Debug()
        elif self.CheckIfArrive() and self.action != DOZE and self.action != SLEEP:
            self.StStop()
        if self.action == DOZE and self.pathIndex == IdxCount[DOZE] - 1:
            self.UpdateAction(SLEEP)

    def FoxUpdate(self):
        self.Update(self.speed, FoxActionPath[self.action], IdxCount[self.action])
        # print(self.action)

    def Debug(self):
        DebugDict = {
            "Dest": self.destination,
            "Pos": self.pos,
            "Dir": self.dir,
            "Speed": self.speed,
        }
        print(DebugDict)
