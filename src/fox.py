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

    # right = 1; left = -1; up = 1; down = -1;
    def UpdateDir(self):
        if self.destination[0] - self.pos[0] >= 0:
            self.dir[0] = 1
        else:
            self.dir[0] = -1
        if self.destination[1] - self.pos[1] >= 0:
            self.dir[1] = -1
        else:
            self.dir[1] = 1

    def CheckSpeed(self, action=WALK):
        dx = self.destination[0] - self.pos[0]
        dy = self.destination[1] - self.pos[1]
        XNewSpeed = YNewSpeed = 0
        t = 0
        if abs(dx) > abs(dy):
            t = min(abs(dx) * 0.05, 20)
        else:
            t = min(abs(dy) * 0.05, 20)
        XNewSpeed = dx / t
        YNewSpeed = dy / t
        self.UpdateSpeed(XNewSpeed, YNewSpeed)

    def CheckRev(self):
        if self.dir[0] == -1:
            self.Xrev = True
        else:
            self.Xrev = False

    def UpdateDest(self, npos):
        self.destination = npos

    def CheckIfArrive(self):
        flagx = False
        flagy = False
        if self.dir[0] == 1 and self.pos[0] >= self.destination[0]:
            flagx = True
        if self.dir[1] == 1 and self.pos[1] <= self.destination[1]:
            flagy = True
        if self.dir[0] == -1 and self.pos[0] <= self.destination[0]:
            flagx = True
        if self.dir[1] == -1 and self.pos[1] >= self.destination[1]:
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
        self.CheckSpeed()
        self.CheckRev()

    def FoxCheck(self, npos):
        if npos != self.destination:
            self.StMove(npos)
            self.Debug(1)
        elif self.CheckIfArrive() and self.action != DOZE and self.action != SLEEP:
            self.StStop()
        if self.action == DOZE and self.pathIndex == IdxCount[DOZE] - 1:
            self.UpdateAction(SLEEP)

    def FoxUpdate(self):
        self.Update(self.speed, FoxActionPath[self.action], IdxCount[self.action])
        # print(self.action)

    def Debug(self, flag=None):
        DebugDict = {
            "Dest": self.destination,
            "Pos": self.pos,
            "Dir": self.dir,
            "Speed": self.speed,
        }
        if flag == 1:
            print(DebugDict)
        if self.action != WALK:
            print("Not walk")
            print(DebugDict)
