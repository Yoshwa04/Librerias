
from typing import Callable, Literal, TypedDict

from category import Category
from anima import Anima
from secondary_effect import SecondaryEffect
from type import TypeA, TypeB

from logic.math import solve_equation, give_just_one_solution
from logic.generate.boolean import fifty_fifty

from random import randint
from dict import formula_dict, effectiveness_chart

class Technique(TypedDict):
    name: str
    power: int
    type: TypeA | TypeB
    category: Category
    accuracy: int | Literal["always"] # Un número o "always"
    pp: int
    secondary_effects: SecondaryEffect | None
    priority: bool
    heal: bool
    objective: Literal["self", "one", "all", "only_enemies"]   
    battle_method: Callable


def just_damage(atack_anima: Anima, defense_Anima: Anima, tech: Technique): 
    if isinstance(tech.type, TypeA):
        eff = effectiveness_chart[tech.type][defense_Anima.type_a]
    else:
        eff = effectiveness_chart[tech.type][defense_Anima.type_b1]
        if defense_Anima.type_b2 is not None:
            eff2 = effectiveness_chart[tech.type][defense_Anima.type_b2]
            eff *= eff2
    
    stab = "stab = 1.5" if tech.type in (atack_anima.type_a, atack_anima.type_b1, atack_anima.type_b2) else "stab = 1"        
    eff = f"eff = {eff}"      
    v = f"v = {randint(75, 100)}" # Me gustaria que si sale 75 ponga min damage y si sale 100 ponga max damage
    lvl = f"lvl = {atack_anima.lvl}"
    atq = f"atq = {atack_anima.atk if tech.category is Category.PHYSICAL else atack_anima.sp_atk}"
    def_ = f"def = {defense_Anima.def_ if tech.category is Category.PHYSICAL else defense_Anima.sp_def}"
    power = f"power = {tech.power}"
    
    return int(give_just_one_solution(solve_equation(formula_dict["damage"], stab, eff, v, lvl, atq, power, def_), "damage"))
     
     
''' Orden movimientos en combate 
an1 = 0
an2 = 0
mov1 = True
mov2 = True

if mov1.priority and !mov2.priority:
    pass
    #mov1()
    #mov2()
elif mov2.priority and !mov1.priority:
    pass
    #mov2()
    #mov1()
else:
    if an1.spe > an2.spe:
        pass
        #mov1()
        #mov2()
    elif an2.spe > an1.spe:
        pass
        #mov2()
        #mov1()
    else:
        if fifty_fifty():
            pass
            #mov1()
            #mov2()
        else:
            pass
            #mov2()
            #mov1()
'''


        
techdex: dict[str, Technique] = { # Guardar tambien -> prioridad? curacion? objetivo? metodo?
    "000": { #Ejemplo
        "name": "a",
        "power": 1,
        "type": TypeA.UMBRA,
        "category": Category.PHYSICAL,
        "accuracy": 100, # un numero o un str = "always"
        "pp": 15,
        "secondary_effects": None,
        "priority": False,
        "heal": False,
        "objective": "self",
    },
    "001": {
        "name": "Strike",
        "power": 40,
        "type": TypeB.NEUTRO,
        "category": Category.PHYSICAL,
        "accuracy": 100,
        "pp": 30,
        "secondary_effects": None,
    },
    "002": {
        "name": "Double Punch",
        "power": 20,
        "type": TypeB.NEUTRO,
        "category": Category.PHYSICAL,
        "accuracy": 90,
        "pp": 10,
        "secondary_effects": None,
    },
    "003": {
        "name": "Mega Punch",
        "power": 80,
        "type": TypeB.NEUTRO,
        "category": Category.PHYSICAL,
        "accuracy": 80,
        "pp": 10,
        "secondary_effects": None,
    },
    "004": {
        "name": "Swift",
        "power": 60,
        "type": TypeB.NEUTRO,
        "category": Category.SPECIAL,
        "accuracy": "always",
        "pp": 20,
        "secondary_effects": None,
    },
    "005": {
        "name": "Tri Attack",
        "power": 80,
        "type": TypeB.NEUTRO,
        "category": Category.SPECIAL,
        "accuracy": 100,
        "pp": 15,
        "secondary_effects": {SecondaryEffect.BURN: 33, SecondaryEffect.FREEZE: 66, SecondaryEffect.PARALIZE: 100} # revisar
    },
    "006": {
        "name": "Restore",
        "power": None,
        "type": TypeB.NEUTRO,
        "category": Category.STATUS,
        "accuracy": "always",
        "pp": 5,
        "secondary_effects": None,
    },        
}
'''A dictionary of every single Technique with its information that never changes'''