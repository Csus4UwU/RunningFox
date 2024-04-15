import image


class GameMap(image.Image):
    def __init__(self, index) -> None:
        self.mapidx = index

    def Correct(self, pos):
        pass

    def IsOut(self, pos):
        if self.mapidx == 1:
            if pos[1] <= 1:
                pass
