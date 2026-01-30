from arcana import Arcana
from constants import CONFIDENT_MAX_LVL


class Confident:
    def __init__(self, name: str, arcana: Arcana):
        self.name = name
        self.arcana = arcana
        self.lvl = 0
        
    def lvl_up(self):
        self.lvl += 1 if self.lvl < CONFIDENT_MAX_LVL else 0
        