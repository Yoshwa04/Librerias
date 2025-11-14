from typing import Optional
from type import TypeA, TypeB
from arcana import Arcana

from nature import Nature


class Anima:
    def __init__(self, nAnimadex: str, lvl: int, nature: Optional[Nature] = None, status1: Optional[str] = None, status2: Optional[str] = None):
        self.animadex = animadex
        self.name = animadex[nAnimadex]["name"]
        self.lvl = lvl
        
        self.type_a = animadex[nAnimadex]["types"][0]
        self.type_b = animadex[nAnimadex]["types"][1]
        self.ability = animadex[nAnimadex]["ability"]
        self.arcana = animadex[nAnimadex]["arcana"]
        self.move_learning = animadex[nAnimadex]["move_learning"]
        self.growth = animadex[nAnimadex]["growth"]
        self.catch_rate = animadex[nAnimadex]["catch_rate"]
        self.evolves = animadex[nAnimadex]["evolves"]
        self.base_stats = animadex[nAnimadex]["base_stats"]
        
        
        self.nature = nature if nature else None #Aqui iria metodo para ponerle una naturaleza
        self.status1 = status1 if status1 else None # Aqui hay que poner el status normal
        self.status2 = status2 if status2 else None # Lo mismo
        
        
animadex = {
    "000": { #Ejemploc
        "name": "a",
        "types": ["typeA", "typeB"],
        "ability": "ab",
        "arcana": "ar",
        "growth": "g",
        "catch_rate" : 255,
        "evolves": None,
        "base_stats" : {
          "hp" : 1,
          "atk" : 1,
          "sp_atk" : 1,
          "def" : 1,
          "sp_def" : 1,
          "spe" : 1  
        },
        "move_learning": {
            4: "move",
        }
    },
    "001": {
        "name": "starter1",
        "types": [TypeA.ESSENTIA, TypeB.NEUTRO],
        "ability": "",
        "arcana": Arcana.TERRA,
        "growth": "parabolic",
        "catch_rate" : 45,
        "evolves": "002",
        "base_stats" : {
          "hp" : 44,
          "atk" : 40,
          "sp_atk" : 58,
          "def" : 62,
          "sp_def" : 61,
          "spe" : 49  
        },
        "move_learning": {
            
        }     
    },
}
'''A dictionary of every single Anima with his information that never changes'''


ani = Anima("001", 1)

print(ani.base_stats)