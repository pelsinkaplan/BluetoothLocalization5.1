class Visitor:
    id = None
    name = None
    bio = None
    device = None

    def __init__(self, id, name, bio, device):
        self.id = id
        self.name = name
        self.bio = bio
        self.device = device

    def get_id(self):
        return self._id

    def set_id(self, x):
        self._id = x

    def get_name(self):
        return self._name

    def set_name(self, x):
        self._name = x

    def get_bio(self):
        return self._bio

    def set_bio(self, x):
        self._bio = x

    def get_device(self):
        return self._device

    def set_device(self, x):
        self._device = x
