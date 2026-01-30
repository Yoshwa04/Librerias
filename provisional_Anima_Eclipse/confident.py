from arcana import Arcana


LVL_MAX = 10

class Confident:
    def __init__(self, name: str, arcana: Arcana):
        self.name = name
        self.arcana = arcana
        self.lvl = 0
        
    def lvl_up(self):
        self.lvl += 1 if self.lvl < LVL_MAX else 0
        