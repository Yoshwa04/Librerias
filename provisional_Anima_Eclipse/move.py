from dict import movedex


class Move:
    def __init__(self, nMovedex: str):
        self.name = movedex[nMovedex]["name"]
        self.move_type = movedex[nMovedex]["move_type"]
        self.category = movedex[nMovedex]["category"]
        self.accuracy = movedex[nMovedex]["accuracy"]
        self.pp_max = movedex[nMovedex]["pp"]
        self.power = movedex[nMovedex]["power"]
        self.secondary_effects = movedex[nMovedex]["secondary_effects"]