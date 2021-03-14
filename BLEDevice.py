class BLEDevice:
    id = None
    lastPacketSendTime = None

    def __init__(self, id):
        self.id = id
        # self.lastPacketSendTime = lastPacketSendTime

    def get_id(self):
        return self._id

    def set_id(self, x):
        self._id = x

    def get_lastPacketSendTime(self):
        return self._lastPacketSendTime

    def set_lastPacketSendTime(self, x):
        self._lastPacketSendTime = x
