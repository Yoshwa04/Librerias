import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import Optional
import random
from sympy import Dict, symbols

from constants import INCREASE, DECREASE
from dict import  animadex, formula_dict, nature_dict, critical_index_dict
from status import Status1, Status2
from type import TypeA, TypeB
from arcana import Arcana
from nature import Nature
from technique import Technique

from logic.math import solve_equation, give_just_one_solution




class Anima:
    # Cosas que tiene que tener y aun hay que implementar: su moveset actual, la experiencia, item que lleva...
    def __init__(self, nAnimadex: str, min_lvl: int, max_lvl, nature: Optional[Nature] = None, object: Optional[str] = None):
        self.animadex = nAnimadex
        self.lvl = random.randint(min_lvl, max_lvl)
        self.status1, self.status2 = Status1.GOOD, Status2.GOOD
        self.name = animadex[nAnimadex]["name"]
        
        
        self.type_a = animadex[nAnimadex]["types"][0]
        self.type_b1 = animadex[nAnimadex]["types"][1]
        self.type_b2 = animadex[nAnimadex]["types"][2] if len(animadex[nAnimadex]["types"]) > 2 else None
        self.ability = animadex[nAnimadex]["abilitys"]["00H"] if random.randint(1, 100) == 100 else random.choice([animadex[nAnimadex]["abilitys"]["001"], animadex[nAnimadex]["abilitys"]["002"]])
        self.arcana = animadex[nAnimadex]["arcana"]
        self.technique_learning = animadex[nAnimadex]["technique_learning"]
        self.assisted_techniques = animadex[nAnimadex]["assisted_techniques"]
        self.growth = animadex[nAnimadex]["growth"]
        self.exp_base_given = animadex[nAnimadex]["exp_base_given"]
        self.catch_rate = animadex[nAnimadex]["catch_rate"]
        self.evolves = animadex[nAnimadex]["evolves"]
        self.base_stats = animadex[nAnimadex]["base_stats"]
        
        self.nature = nature if nature else self._random_nature()
        self.object = object  # Por implementar
        self._random_potentials()
        
        self.calculate_stats(first=True)
        
        self.technique_set: Dict[str, dict] = {}
        self.ability_uses: int = 0
        
        
    def _random_potentials(self):
        self.hp_potential = random.randint(1, 35)
        self.atk_potential = random.randint(1, 35)
        self.sp_atk_potential = random.randint(1, 35)
        self.def_potential = random.randint(1, 35)
        self.sp_def_potential = random.randint(1, 35)
        self.spe_potential = random.randint(1, 35)
     
    def _change_potentials(self, hp, atk, spatk, _def, spdef, spe):
        self.hp_potential = hp
        self.atk_potential = atk
        self.sp_atk_potential = spatk
        self.def_potential = _def
        self.sp_def_potential = spdef
        self.spe_potential = spe
        
    def _random_nature(self):
        if random.randint(1, 5) == 5:
            return Nature.NEUTRA
        return random.choice([n for n in Nature if n != Nature.NEUTRA])
    
    def _reset_type(self):
        self.type_a = animadex[self.animadex]["types"][0]    
        
    def change_lvl(self, lvl):
        self.lvl = lvl
        self.calculate_stats(True)
        
    def calculate_stats(self, first: Optional[bool] = False):
        nature_effects = nature_dict[self.nature]
        
        atk_modifier =      ("1.2" if nature_effects[INCREASE] == "atk" else 
                             "0.8" if nature_effects[DECREASE] == "atk" else 
                             "1.0")
        sp_atk_modifier =   ("1.2" if nature_effects[INCREASE] == "sp_atk" else
                             "0.8" if nature_effects[DECREASE] == "sp_atk" else 
                             "1.0")
        def_modifier =      ("1.2" if nature_effects[INCREASE] == "def" else
                             "0.8" if nature_effects[DECREASE] == "def" else
                             "1.0")
        sp_def_modifier =   ("1.2" if nature_effects[INCREASE] == "sp_def" else
                             "0.8" if nature_effects[DECREASE] == "sp_def" else 
                             "1.0")
        spe_modifier =      ("1.2" if nature_effects[INCREASE] == "spe" else
                             "0.8" if nature_effects[DECREASE] == "spe" else
                             "1.0")
        
        self.hp_max = int(give_just_one_solution(solve_equation(formula_dict["hp"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['hp']}", f"potential = {self.hp_potential}"), "hp"))
        if first:
            self.hp_now = self.hp_max
            self.exp = 0
            self.atk_inc_dec, self.sp_atk_inc_dec, self.def_inc_dec, self.sp_def_inc_dec, self.spe_inc_dec,self.acc_inc_dec, self.eva_inc_dec = 1
            self.crit = 0
        self.atk = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['atk']}", f"potential = {self.atk_potential}", f"nature = {atk_modifier}"), "stat"))
        self.sp_atk = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['sp_atk']}", f"potential = {self.sp_atk_potential}", f"nature = {sp_atk_modifier}"), "stat"))
        self.def_ = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['def']}", f"potential = {self.def_potential}", f"nature = {def_modifier}"), "stat"))
        self.sp_def = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['sp_def']}", f"potential = {self.sp_def_potential}", f"nature = {sp_def_modifier}"), "stat"))
        self.spe = int(give_just_one_solution(solve_equation(formula_dict["stat"], f"lvl = {self.lvl}", f"stat_base = {self.base_stats['spe']}", f"potential = {self.spe_potential}", f"nature = {spe_modifier}"), "stat"))
        
        self.exp_needed_to_lvl_up = -1 if self.lvl == 100 else int(give_just_one_solution(solve_equation(formula_dict["growth"][self.growth], f"lvl = {self.lvl + 1}"), "growth")) - int(give_just_one_solution(solve_equation(formula_dict["growth"][self.growth], f"lvl = {self.lvl}"), "growth"))
    
    def lvl_up(self):
        if self.exp >= self.exp_needed_to_lvl_up and self.exp_needed_to_lvl_up != -1:
            self.lvl += 1
            self.exp -= self.exp_needed_to_lvl_up
            
            self.calculate_stats(False)
    
    def recieve_damage(self, damage: int):
        self.hp_now -= damage 
        
    def cure_anima(self):
        self.hp_now = self.hp_max
        self.status1 = Status1.GOOD
        self.status2 = Status2.GOOD

    # Esto no se si ira aqui o en los metodos de combate
    def change_fluxor_type(self, technique: Technique):
        if technique.type == TypeA.UMBRA and self.type_a != TypeA.UMBRA:
            self.type_a = TypeA.UMBRA
        elif technique.type == TypeA.ESSENTIA and self.type_a != TypeA.ESSENTIA:
            self.type_a = TypeA.ESSENTIA






ani = Anima("001", 5, 5, Nature.ADIVINO) 


# '''Esto es en batalla - Ejemplo de como se aplicarian los modificadores de stats en batalla'''

# Esto al iniciar la pelea
atk_btl_increase_decrease = 1
acc_btl_increase_decrease = 1
atk_btl_mod = 1
crit_index = critical_index_dict[0] # Indice de crítico
critical = True

# Imaginamos que el rival nos a dado y se ha activado el efecto de bajarnos el atk
if atk_btl_increase_decrease > 0.25:
    atk_btl_increase_decrease -= 0.25
else:
    pass # Ya no puede bajar más

# Imaginamos que hemos usado un movimiento que nos sube el atk
if atk_btl_increase_decrease < 1.75:
    atk_btl_increase_decrease += 0.25
else:
    pass # Ya no puede subir más

# Imaginamos que hemos usado un movimiento que sube la precisión
if acc_btl_increase_decrease < 1.75:
    acc_btl_increase_decrease += 0.25
else:
    pass # Ya no puede subir más
# Imaginamos que hemos usado un movimiento que baja la precisión del rival
if acc_btl_increase_decrease > 0.25:
    acc_btl_increase_decrease -= 0.25
else:
    pass # Ya no puede bajar más
# Y la misma comprobacion para la evasion y demas.

critical = True if random.randint(1, 100) <= crit_index else False

if critical:
    if atk_btl_increase_decrease < 1:
        atk_btl_increase_decrease = 1
    atk_btl_mod = atk_btl_increase_decrease * 1.5
else:
    atk_btl_mod = atk_btl_increase_decrease

atk_btl_mod *=  0.5 if "burned" else 1
daññño = 100 / (50 if not critical else 100) # Representacion de la parte de la formula del daño que ignora la subida de def del rival en caso de crítico
damage_dealt = 1 * atk_btl_mod

