class Position:
    positionX = None
    positionY = None

    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY

    def get_positionX(self):
        return self._positionX

    def set_positionX(self, x):
        self._positionX = x

    def get_positionY(self):
        return self._positionY

    def set_positionY(self, x):
        self._positionY = x
