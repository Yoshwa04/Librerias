from typing import Optional
import random
import os, sys
from sympy import symbols
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dict import animadex, formula_dict, nature_dict
from status import status1, status2
from type import TypeA, TypeB
from arcana import Arcana
from nature import Nature

from logic.math import solve_equation, give_just_one_solution



class Anima:
    # Cosas que tiene que tener y aun hay que implementar: su moveset actual, la experiencia, item que lleva...
    def __init__(self, nAnimadex: str, lvl: int, nature: Optional[Nature] = None):
        self.animadex = nAnimadex
        self.lvl = lvl
        self.status1, self.status2 = status1.GOOD, status2.GOOD
        self.name = animadex[nAnimadex]["name"]
        
        
        self.type_a = animadex[nAnimadex]["types"][0]
        self.type_b = animadex[nAnimadex]["types"][1]
        self.ability = animadex[nAnimadex]["abilitys"]["00H"] if random.randint(1, 100) == 100 else random.choice([animadex[nAnimadex]["abilitys"]["001"], animadex[nAnimadex]["abilitys"]["002"]])
        self.arcana = animadex[nAnimadex]["arcana"]
        self.move_learning = animadex[nAnimadex]["move_learning"]
        self.growth = animadex[nAnimadex]["growth"]
        self.exp_base_given = animadex[nAnimadex]["exp_base_given"]
        self.catch_rate = animadex[nAnimadex]["catch_rate"]
        self.evolves = animadex[nAnimadex]["evolves"]
        self.base_stats = animadex[nAnimadex]["base_stats"]
        
        self.nature = nature if nature else self._random_nature()
        self._random_potentials()
        
        self.calculate_stats(first=True)
        
        
        
    def _random_potentials(self):
        self.hp_potential = random.randint(1, 35)
        self.atk_potential = random.randint(1, 35)
        self.sp_atk_potential = random.randint(1, 35)
        self.def_potential = random.randint(1, 35)
        self.sp_def_potential = random.randint(1, 35)
        self.spe_potential = random.randint(1, 35)
        
    def _random_nature(self):
        return random.choice(list(Nature))
    
    def calculate_stats(self, first: bool = False):
        nature_effects = nature_dict[self.nature]
        
        atk_modifier =      ("1.2" if nature_effects["+"] == "atk" else 
                             "0.8" if nature_effects["-"] == "atk" else 
                             "1.0")
        sp_atk_modifier =   ("1.2" if nature_effects["+"] == "sp_atk" else
                             "0.8" if nature_effects["-"] == "sp_atk" else 
                             "1.0")
        def_modifier =      ("1.2" if nature_effects["+"] == "def" else
                             "0.8" if nature_effects["-"] == "def" else
                             "1.0")
        sp_def_modifier =   ("1.2" if nature_effects["+"] == "sp_def" else
                             "0.8" if nature_effects["-"] == "sp_def" else 
                             "1.0")
        spe_modifier =      ("1.2" if nature_effects["+"] == "spe" else
                             "0.8" if nature_effects["-"] == "spe" else
                             "1.0")
        
        self.hp_max = int(give_just_one_solution(solve_equation(formula_dict["hp"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['hp']}", f"potential = {self.hp_potential}"), "hp"))
        if first:
            self.hp_now = self.hp_max
        self.atk = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['atk']}", f"potential = {self.atk_potential}", f"nature = {atk_modifier}"), "stat"))
        self.sp_atk = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['sp_atk']}", f"potential = {self.sp_atk_potential}", f"nature = {sp_atk_modifier}"), "stat"))
        self.defense = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['def']}", f"potential = {self.def_potential}", f"nature = {def_modifier}"), "stat"))
        self.sp_def = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['sp_def']}", f"potential = {self.sp_def_potential}", f"nature = {sp_def_modifier}"), "stat"))
        self.spe = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['spe']}", f"potential = {self.spe_potential}", f"nature = {spe_modifier}"), "stat"))
        
        self.exp_needed_to_lvl_up = int(give_just_one_solution(solve_equation(formula_dict["growth"][self.growth], f"lvl = {self.lvl + 1}"), "growth")) - int(give_just_one_solution(solve_equation(formula_dict["growth"][self.growth], f"lvl = {self.lvl}"), "growth"))
    
    def recieve_damage(self, damage: int):
        self.hp_now -= damage 
        
    def cure_anima(self):
        self.hp_now = self.hp_max
        self.status1 = status1.GOOD
        self.status2 = status2.GOOD


ani = Anima("000", 100)


# '''Esto es en batalla - Ejemlplo de como se aplicarian los modificadores de stats en batalla'''

# Esto al iniciar la pelea
atk_btl_increase = 1
atk_btl_decrease = 1
atk_btl_mod = 1


# Imaginamos que el rival nos a dado y se ha activado el efecto de bajarnos el atk
if atk_btl_decrease > 0.25:
    atk_btl_decrease -= 0.25
else:
    pass # Ya no puede bajar más

# Imaginamos que hemos usado un movimiento que nos sube el atk
if atk_btl_increase < 1.75:
    atk_btl_increase += 0.25
else:
    pass # Ya no puede subir más

atk_btl_mod = atk_btl_increase * atk_btl_decrease * 0.5 if "burned" else 1
damage_dealt = 1 * atk_btl_mod


print(ani.hp_now, ani.hp_max)