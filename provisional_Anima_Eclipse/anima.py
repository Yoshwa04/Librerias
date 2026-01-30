import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import Optional
import random

from logic.math_core.solver import solve_equation, give_just_one_solution

from animadex import animadex
from constants import INCREASE, DECREASE, ANIMA_MAX_LVL
from dict import  formula_dict
from nature import Nature, nature_dict
from status import *
from type import TypeA
from technique import Technique


class Anima:
    # Cosas que tiene que tener y aun hay que implementar: la experiencia?, item que lleva...
    def __init__(self, nAnimadex: str, min_lvl: int, max_lvl, nature: Optional[Nature] = None, object: Optional[str] = None):
        self.animadex = nAnimadex
        
        self.lvl = random.randint(min_lvl, max_lvl)
        self.alive_status = AliveStatus.ALIVE; self.element_status = ElementStatus.NOTHING; self.behave_status = BehaveStatus.NOTHING; self.special_status = SpecialStatus.NOTHING; 
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
        
        if self.ability["when"] == "always_stats":
            pass # Aqui va el metodo de la habilidad en cuestion??? 
        
        self.object = object
        
        self.nature = nature if nature else self._random_nature()
        self._random_potentials()
        self._assign_nature_effects()
        self.calculate_stats()
        self.hp_now = self.hp_max
        self.stats_inc_dec = {
            "atk": 0,
            "sp_atk": 0,
            "def": 0,
            "sp_def": 0,
            "spe": 0,
            "acc": 0,
            "eva": 0,
        }
        self.crit_index = 0
        
        
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
            
    def calculate_stats(self):
        self.hp_max = int(give_just_one_solution(solve_equation(formula_dict["hp"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['hp']}", f"potential = {self.potentials['hp']}"), "hp"))
            
        self.atk = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['atk']}", f"potential = {self.potentials['atk']}", f"nature = {self.atk_modifier}"), "stat"))
        
        self.sp_atk = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['sp_atk']}", f"potential = {self.potentials['sp_atk']}", f"nature = {self.sp_atk_modifier}"), "stat"))
        
        self.def_ = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['def']}", f"potential = {self.potentials['def']}", f"nature = {self.def_modifier}"), "stat"))
        
        self.sp_def = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['sp_def']}", f"potential = {self.potentials['sp_def']}", f"nature = {self.sp_def_modifier}"), "stat"))
        
        self.spe = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['spe']}", f"potential = {self.potentials['spe']}", f"nature = {self.spe_modifier}"), "stat"))
        
        self.exp_next_lvl = -1 if self.lvl >= ANIMA_MAX_LVL else int(give_just_one_solution(solve_equation(formula_dict["growth"][self.growth], f"lvl = {self.lvl + 1}"), "growth")) - int(give_just_one_solution(solve_equation(formula_dict["growth"][self.growth], f"lvl = {self.lvl}"), "growth"))
    
    def lvl_up(self):
        self.lvl += 1
        self.exp -= self.exp_next_lvl
            
        self.calculate_stats()
        
        possible = self._can_evolve()
        if possible:
            return possible
     
    def _can_evolve(self, used_item: str | None = None) -> list[str]:
        evolutions = animadex[self.animadex]["evolves"]
        possible = []
        
        for evo in evolutions:
            if evo["method"] == "level" and self.lvl >= evo["value"]:
                possible.append(evo["to"])
            elif evo["method"] == "item" and used_item == evo["value"]:
                possible.append(evo["to"])
                
        return possible
    
    def evolve(self, evolution_id: str):
        data = animadex[evolution_id]
        
        self.animadex = evolution_id
        self.name = data["name"]
        self.type_a = data["types"][0]
        self.type_b1 = data["types"][1]
        self.type_b2 = data["types"][2] if len(data["types"]) > 2 else None
        self.arcana = data["arcana"]
        self.exp_base_given = data["exp_base_given"]
        self.evolves = data["evolves"]
        self.base_stats = data["base_stats"]
        self.technique_learning = data["technique_learning"]
        self.assisted_techniques = data["technique_capsules"]

        self.calculate_stats()
            
    def add_exp(self, exp: int):
        self.exp += exp
        
        if self.exp >= self.exp_next_lvl and self.exp_next_lvl != -1:
            self.lvl_up()
        
    def recieve_damage(self, damage: int):
        self.hp_now -= damage 
        
    def cure_anima(self):
        self.hp_now = self.hp_max
        self.alive_status = AliveStatus.ALIVE
        self.element_status = ElementStatus.NOTHING
        self.behave_status = BehaveStatus.NOTHING
        self.special_status = SpecialStatus.NOTHING


    def reset_status(self): # Para cuando termina el turno
        self.special_status = SpecialStatus.NOTHING if self.special_status == SpecialStatus.PROTECTED else self.special_status

    def reset_stats_inc_dec(self): # Para cuando salen de combate y cuando termina el combate
        for stat in self.stats_inc_dec:
            self.stats_inc_dec[stat] = 0




ani = Anima("001", 5, 5, Nature.ADIVINO) 