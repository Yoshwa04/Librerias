import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import Optional
import random

from logic.math_core.solver import solve_equation, give_just_one_solution

from arcana import Arcana
from animadex import animadex
from constants import INCREASE, DECREASE, MAX_LVL, MAX_STAT_INCREASE_DECREASE
from dict import  formula_dict
from nature import Nature, nature_dict
from status import Status1, Status2
from type import TypeA, TypeB
from technique import Technique


class Anima:
    # Cosas que tiene que tener y aun hay que implementar: la experiencia?, item que lleva...
    def __init__(self, nAnimadex: str, min_lvl: int, max_lvl, nature: Optional[Nature] = None, object: Optional[str] = None):
        self.animadex = nAnimadex
        
        self.lvl = random.randint(min_lvl, max_lvl)
        self.status1, self.status2 = Status1.GOOD, Status2.GOOD
        self.name = animadex[self.animadex]["name"]
        
        
        self.type_a = animadex[self.animadex]["types"][0]
        self.is_fluxor = True if self.type_a == TypeA.FLUXOR else False # Esto me servirá para no perder la info de que es fluxor cuando en combate se cambie a otro tipo
        self.type_b1 = animadex[self.animadex]["types"][1]
        self.type_b2 = animadex[self.animadex]["types"][2] if len(animadex[self.animadex]["types"]) > 2 else None
        self._random_ability()
        self.arcana = animadex[self.animadex]["arcana"]
        self.technique_learning = animadex[self.animadex]["technique_learning"]
        self.assisted_techniques = animadex[self.animadex]["technique_capsules"]
        self.growth = animadex[self.animadex]["growth"]
        self.exp_base_given = animadex[self.animadex]["exp_base_given"]
        self.catch_rate = animadex[self.animadex]["catch_rate"]
        self.evolves = animadex[self.animadex]["evolves"]
        self.base_stats = animadex[nAnimadex]["base_stats"]
        
        self.object = object
        
        self.nature = nature if nature else self._random_nature()
        self._random_potentials()
        self._assign_nature_effects()
        self.calculate_stats()
        self.hp_now = self.hp_max
        self.stats_inc_dec = {
            "atk_inc_dec": 0,
            "sp_atk_inc_dec": 0,
            "def_inc_dec": 0,
            "sp_def_inc_dec": 0,
            "spe_inc_dec": 0,
            "sp_spe_inc_dec": 0,
            "acc_inc_dec": 0,
            "eva_inc_dec": 0
        }
        if self.ability["when"] == "always":
            pass # Aqui va el metodo de la habilidad en cuestion
        
        self.exp = 0
        self._init_technique_set()
        
        self.ability_uses: int = 0 # ?
        
        
    def _random_potentials(self):
        self.potentials = {
            "hp": random.randint(1, 35),
            "atk": random.randint(1, 35),
            "sp_atk": random.randint(1, 35),
            "def": random.randint(1, 35),
            "sp_def": random.randint(1, 35),
            "spe": random.randint(1, 35)
        }
    
    def _init_technique_set(self):
        learned = []
        
        for lvl, tech in self.technique_learning.items():
            if lvl <= self.lvl:
                learned.append((lvl, tech))
                
        learned.sort(key=lambda x: x[0])
        
        learned = learned[-4:]
        
        self.technique_set = {}
        
        for i, (_, tech) in enumerate(learned, start=1):
            slot = f"{i:03}"
            self.technique_set[slot] = tech
     
    def _change_potentials(self, hp, atk, spatk, _def, spdef, spe): 
        self.potentials = {
            "hp": hp,
            "atk": atk,
            "sp_atk": spatk,
            "def": _def,
            "sp_def": spdef,
            "spe": spe
        }
        
    def _random_nature(self):
        if random.randint(1, 5) == 5:
            return Nature.NEUTRA
        return random.choice([n for n in Nature if n != Nature.NEUTRA])
    
    def _reset_type(self):
        self.type_a = animadex[self.animadex]["types"][0]    
        
        # Esto no se si ira aqui o en los metodos de combate
    
    def change_fluxor_type(self, technique: Technique):
        if technique.type == TypeA.UMBRA and self.type_a != TypeA.UMBRA:
            self.type_a = TypeA.UMBRA
        elif technique.type == TypeA.ESSENTIA and self.type_a != TypeA.ESSENTIA:
            self.type_a = TypeA.ESSENTIA    
        
    def change_lvl(self, lvl):
        self.lvl = lvl
        self.calculate_stats(True)
    
    def _random_ability(self):
        self.ability = animadex[self.animadex]["abilities"]["00H"] if random.randint(1, 100) == 100 else random.choice([animadex[self.animadex]["abilities"]["001"], animadex[self.animadex]["abilities"]["002"]])
        
    def change_ability(self, ability: str):
        self.ability = self.animadex["abilities"][ability]  
    
    def _assign_nature_effects(self):
        nature_effects = nature_dict[self.nature]
        
        self.atk_modifier =     ("1.2" if nature_effects[INCREASE] == "atk" else
                                "0.8" if nature_effects[DECREASE] == "atk" else
                                "1.0")
        self.sp_atk_modifier =  ("1.2" if nature_effects[INCREASE] == "sp_atk" else
                                "0.8" if nature_effects[DECREASE] == "sp_atk" else
                                "1.0")
        self.def_modifier =     ("1.2" if nature_effects[INCREASE] == "def" else
                                "0.8" if nature_effects[DECREASE] == "def" else
                                "1.0")
        self.sp_def_modifier =  ("1.2" if nature_effects[INCREASE] == "sp_def" else
                                "0.8" if nature_effects[DECREASE] == "sp_def" else
                                "1.0")
        self.spe_modifier =     ("1.2" if nature_effects[INCREASE] == "spe" else
                                "0.8" if nature_effects[DECREASE] == "spe" else
                                "1.0")
            
    def calculate_stats(self, first: Optional[bool] = False):
        self.hp_max = int(give_just_one_solution(solve_equation(formula_dict["hp"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['hp']}", f"potential = {self.potentials['hp']}"), "hp"))
            
        self.atk = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['atk']}", f"potential = {self.potentials['atk']}", f"nature = {self.atk_modifier}"), "stat"))
        
        self.sp_atk = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['sp_atk']}", f"potential = {self.potentials['sp_atk']}", f"nature = {self.sp_atk_modifier}"), "stat"))
        
        self.def_ = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['def']}", f"potential = {self.potentials['def']}", f"nature = {self.def_modifier}"), "stat"))
        
        self.sp_def = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['sp_def']}", f"potential = {self.potentials['sp_def']}", f"nature = {self.sp_def_modifier}"), "stat"))
        
        self.spe = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['spe']}", f"potential = {self.potentials['spe']}", f"nature = {self.spe_modifier}"), "stat"))
        
        self.exp_next_lvl = -1 if self.lvl >= MAX_LVL else int(give_just_one_solution(solve_equation(formula_dict["growth"][self.growth], f"lvl = {self.lvl + 1}"), "growth")) - int(give_just_one_solution(solve_equation(formula_dict["growth"][self.growth], f"lvl = {self.lvl}"), "growth"))
    
    def lvl_up(self):
        if self.exp >= self.exp_next_lvl and self.exp_next_lvl != -1:
            self.lvl += 1
            self.exp -= self.exp_next_lvl # La resta es asi porque aún no se ha calculado la exp del sig lvl.
            
            self.calculate_stats(False)
    
    def recieve_damage(self, damage: int):
        self.hp_now -= damage 
        
    def cure_anima(self):
        self.hp_now = self.hp_max
        self.status1 = Status1.GOOD
        self.status2 = Status2.GOOD


    def reset_status(self): # Para cuando termina el turno
        self.status1 = Status1.GOOD if self.status1 == Status1.PROTECTED else self.status1

    def reset_stats_inc_dec(self): # Para cuando salen de combate y cuando termina el combate
        for stat in self.stats_inc_dec:
            self.stats_inc_dec[stat] = 0




ani = Anima("001", 5, 5, Nature.ADIVINO) 