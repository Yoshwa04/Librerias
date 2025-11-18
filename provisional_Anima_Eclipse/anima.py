from typing import Optional

from dict import animadex
from status import status1, status2
from type import TypeA, TypeB
from arcana import Arcana
from nature import Nature


class Anima:
    def __init__(self, nAnimadex: str, lvl: Optional[int], nature: Optional[Nature]):
        self.animadex = animadex
        self.name = animadex[nAnimadex]["name"]
        # self.lvl = lvl if lvl else #metodo 
        self.status1, self.status2 = status1.GOOD, status2.GOOD
        
        self.type_a = animadex[nAnimadex]["types"][0]
        self.type_b = animadex[nAnimadex]["types"][1]
        self.ability = animadex[nAnimadex]["ability"]
        self.arcana = animadex[nAnimadex]["arcana"]
        self.move_learning = animadex[nAnimadex]["move_learning"]
        self.growth = animadex[nAnimadex]["growth"]
        self.exp_base_given = animadex[nAnimadex]["exp_base_given"]
        self.catch_rate = animadex[nAnimadex]["catch_rate"]
        self.evolves = animadex[nAnimadex]["evolves"]
        self.base_stats = animadex[nAnimadex]["base_stats"]
        
        self.nature = nature if nature else None #Aqui iria metodo para ponerle una naturaleza

        
        



ani = Anima("001", 1)

print(ani.base_stats)