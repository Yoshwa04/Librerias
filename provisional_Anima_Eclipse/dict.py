from collections import defaultdict
from typing import Dict
from arcana import Arcana
from category import Category
from type import TypeA, TypeB
from nature import Nature
from ability import Ability
from constants import INCREASE, DECREASE


def animadex_base_stats_model(hp: int, atk: int, sp_atk: int, _def: int, sp_def: int, spe: int) -> Dict[str, int]:
    '''This method just returns a dict of the stats given its value'''
    return {
        "hp" : hp,
        "atk" : atk,
        "sp_atk" : sp_atk,
        "def" : _def,
        "sp_def" : sp_def,
        "spe" : spe  
    }

def animadex_abilitys_model(ability1: Ability, ability2: Ability, hidden: Ability) -> Dict[str, Ability]:
    '''This method just returns a dict of the abilitys given'''
    
    return {
        "001" : ability1,
        "002" : ability2,
        "00H" : hidden  
    }

growth_dict = {
    "fast": "growth = 4 * lvl**3 / 5",
    "normal": "growth = lvl**3",
    "slow": "growth = 5 * lvl**3 / 4",
    "parabolic": "growth = 6 * lvl**3 / 5 - 15 * lvl**2 + 100 * lvl -140"
}
'''Possible growth forms for the Animas'''

formula_dict = {
    "hp": "hp = (lvl/100 * ((stat_base*2) + potential)) + lvl",
    "stat": "stat = (5 + (lvl/100 * ((stat_base*2) + potential))) * nature",
    "catch": "catch = (hp_max*3 - hp_now*2) * catch_ratio * ball_ratio/hp_max*3 * status ",
    "damage": "damage = 1/100 * stab * eff * v * ((2/10 * lvl + 1) * atq * power/25 * def + 2)",
    "exp_given": "exp_given = (exp_base_given*lvl/participants/5) * ((2*lvl+10)**(5/2)) / ((lvl+ally_lvl+10)**(5/2)) + 1) * combat_type * object_modifier",
    "growth": growth_dict
}
'''A bunch of formulas'''


nature_dict = {
    Nature.BERSERKER:   {INCREASE: "atk", DECREASE: "def"},
    Nature.GLADIADOR:   {INCREASE: "atk", DECREASE: "sp_def"},
    Nature.ASALTANTE:   {INCREASE: "atk", DECREASE: "spe"},
    Nature.BRUTO:       {INCREASE: "atk", DECREASE: "sp_atk"},  
    
    Nature.GUARDIA:     {INCREASE: "def", DECREASE: "atk"},
    Nature.MURALLA:     {INCREASE: "def", DECREASE: "sp_atk"},
    Nature.CENTINELA:   {INCREASE: "def", DECREASE: "dp_def"},
    Nature.FORTIFICADO: {INCREASE: "def", DECREASE: "spe"},
    
    Nature.HECHICERO:   {INCREASE: "sp_atk", DECREASE: "atk"},
    Nature.ORACULO:     {INCREASE: "sp_atk", DECREASE: "def"},
    Nature.MISTICO:     {INCREASE: "sp_atk", DECREASE: "sp_def"},
    Nature.ERUDITO:     {INCREASE: "sp_atk", DECREASE: "spe"},
    
    Nature.MONJE:       {INCREASE: "sp_def", DECREASE: "atk"},
    Nature.ILUMINADO:   {INCREASE: "sp_def", DECREASE: "sp_atk"},
    Nature.ADIVINO:     {INCREASE: "sp_def", DECREASE: "def"},
    Nature.ESPIRITUAL:  {INCREASE: "sp_def", DECREASE: "spe"},  
    
    Nature.EXPLORADOR:  {INCREASE: "spe", DECREASE: "def"},
    Nature.CAZADOR:     {INCREASE: "spe", DECREASE: "sp def"},
    Nature.BROMISTA:    {INCREASE: "spe", DECREASE: "atk"},
    Nature.ESPADACHIN:  {INCREASE: "spe", DECREASE: "sp_atk"},
    
    Nature.NEUTRA:      {INCREASE: None, DECREASE: None},
}
'''The dictionary of which stats increase or decrease for each nature'''

effectiveness_chart = {
    TypeA.ESSENTIA:     defaultdict(lambda: 1,{TypeA.UMBRA: 2, TypeA.FORMA: 0.5,}),
    TypeA.FORMA:        defaultdict(lambda: 1,{TypeA.UMBRA: 0.5, TypeA.ESSENTIA: 2,}),
    TypeA.UMBRA:        defaultdict(lambda: 1,{TypeA.FORMA: 2, TypeA.ESSENTIA: 0.5,}),
    
    TypeB.IGNIS:        defaultdict(lambda: 1,{TypeB.PLANTA: 2, TypeB.GLACIES: 2, TypeB.METALLUM: 2, TypeB.AQUA: 0.5, TypeB.RUPES: 0.5, TypeB.TERRA: 0.5,}),
    TypeB.AQUA:         defaultdict(lambda: 1,{TypeB.IGNIS: 2, TypeB.RUPES: 2, TypeB.TERRA: 2, TypeB.PLANTA: 0.5,}),
    TypeB.PLANTA:       defaultdict(lambda: 1,{TypeB.AQUA: 2, TypeB.RUPES: 2, TypeB.TERRA: 2, TypeB.SINISTER: 2, TypeB.IGNIS: 0.5, TypeB.METALLUM: 0.5, TypeB.VENENUM: 0.5,}),
    TypeB.ELECTRITAS:   defaultdict(lambda: 1,{TypeB.AQUA: 2, TypeB.VENTUS: 2, TypeB.PLANTA: 0.5, TypeB.METALLUM: 0.5, TypeB.TERRA: 0}),
    TypeB.GLACIES:      defaultdict(lambda: 1,{TypeB.PLANTA: 2, TypeB.VENTUS: 2, TypeB.TERRA: 2, TypeB.METALLUM: 0.5,}),
    TypeB.TERRA:        defaultdict(lambda: 1,{TypeB.IGNIS: 2, TypeB.ELECTRITAS: 2, TypeB.METALLUM: 2, TypeB.VENTUS: 0,}),
    TypeB.VENTUS:       defaultdict(lambda: 1,{TypeB.PLANTA: 2, TypeB.TERRA: 2,TypeB.ELECTRITAS: 0.5, TypeB.IGNIS: 0.5, TypeB.METALLUM: 0.5,}),
    TypeB.VENENUM:      defaultdict(lambda: 1,{TypeB.PLANTA: 2, TypeB.LUX: 2,TypeB.GLACIES: 0.5,  TypeB.TERRA: 0.5,TypeB.METALLUM: 0,}),
    TypeB.METALLUM:     defaultdict(lambda: 1,{TypeB.GLACIES: 2, TypeB.RUPES: 2, TypeB.LUX: 0.5, TypeB.ELECTRITAS: 0.5, TypeB.AQUA: 0.5, TypeB.TERRA: 0.5, TypeB.SINISTER: 0.5,}),
    TypeB.LUX:          defaultdict(lambda: 1,{TypeB.SINISTER: 2, TypeB.VENENUM: 0.5,}),
    TypeB.SINISTER:     defaultdict(lambda: 1,{TypeB.LUX: 2, TypeB.PLANTA: 0.5,}),
    TypeB.RUPES:        defaultdict(lambda: 1,{TypeB.IGNIS: 2, TypeB.GLACIES: 2, TypeB.METALLUM: 0.5,}),
}
'''A dictionary that contains the effectiveness of each type against others'''

critical_index_dict = {   
    0: 6.25,
    1: 12.5,
    2: 25,
    3: 33.3,
    4: 50,
}
'''A dictionary that contains the critical hit chance percentages based on the index'''

techdex = {
    "000": { #Ejemplo
        "name": "a",
        "power": 1,
        "type": TypeA.UMBRA,
        "category": Category.PHYSICAL,
        "accuracy": 100,
        "pp": 15,
        "secondary_effects": None,
    },
}
'''A dictionary of every single Technique with its information that never changes'''

animadex = { 
    "000": { #Ejemplo
        "name": "a",
        "types": [TypeA.NEUTRO, TypeB.NEUTRO],
        "abilitys": animadex_abilitys_model(Ability.PHYSICAL_POWER, Ability.MAGIC_POWER, Ability.EXAMPLE_ABILITY),
        "arcana": Arcana.ABYSSUS,
        "growth": "parabolic",
        "exp_base_given": 1,
        "catch_rate" : 255,
        "evolves": None,
        "base_stats" : animadex_base_stats_model(hp=250, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
            4: techdex["000"],   
        },
        "assisted_techinques": {
            "001" : techdex["000"],
        }
    }, 
    "001": { 
        "name": "starter", 
        "types": [TypeA.ESSENTIA, TypeB.NEUTRO],
        "abilitys": animadex_abilitys_model(Ability.PHYSICAL_POWER, Ability.MAGIC_POWER, Ability.EXAMPLE_ABILITY),
        "arcana": Arcana.TERRA,
        "growth": "parabolic",
        "exp_base_given": 64,
        "catch_rate": 45,
        "evolves": {"lvl" : 20, "to": "002"},
        "base_stats": animadex_base_stats_model(44, 40, 58, 62, 61, 49),
        "move_learning": {
            
        },
        "assisted_techinques": {
            "001" : techdex["000"],
            
        }     
    },
    "002": { 
        "name": "evolved_starter",
        "types": [TypeA.ESSENTIA, TypeB.LUX],
        "abilitys": "",
        "arcana": Arcana.TERRA,
        "growth": "parabolic",
        "exp_base_given": 141,
        "catch_rate" : 45,
        "evolves": {"lvl": 38, "to": "003"},
        "base_stats": animadex_base_stats_model(58, 54, 72, 79, 77, 56),
        "move_learning": {
            
        },
        "assisted_techinques": {
            "001" : techdex["000"],
            
        },
    },
    "003": { 
        "name": "final_starter",
        "types": [TypeA.ESSENTIA, TypeB.LUX],
        "abilitys": "",
        "arcana": Arcana.TERRA,
        "growth": "fast",
        "exp_base_given": 208,
        "catch_rate": 45,
        "evolves": None,
        "base_stats": animadex_base_stats_model(80, 68, 90, 121, 90, 70),
        "move_learning": {
            
        },
        "assisted_techinques": {
            "001" : techdex["000"],
            
        }
    },
    "004": {
        "name": "rival_starter",
        "types": [TypeA.UMBRA, TypeB.NEUTRO],
        "abilitys": "",
        "arcana": Arcana.ABYSSUS,
        "growth": "parabolic",
        "exp_base_given": 64,
        "catch_rate": 45,
        "evolves": {"lvl" : 20, "to": "005"},
        "base_stats": animadex_base_stats_model(hp=49, atk=55, sp_atk=44, _def=60, sp_def=60, spe=53),
        "move_learning": {
        },
        "assisted_techinques": {
            "001" : techdex["000"],
        }
    },
    "005": { 
        "name": "evolved_rival_starter",
        "types": [TypeA.UMBRA, TypeB.SINISTER],
        "abilitys": "",
        "arcana": Arcana.ABYSSUS,
        "growth": "parabolic",
        "exp_base_given": 141,
        "catch_rate": 45,
        "evolves": {"lvl": 38, "to": "006"},
        "base_stats": animadex_base_stats_model(hp=61, atk=70, sp_atk=59, _def=81, sp_def=74, spe=61),
        "move_learning": {
        },
        "assisted_techinques": {
            "001" : techdex["000"],
        }
    },
    "006": { 
        "name": "final_rival_starter",
        "types": [TypeA.UMBRA, TypeB.SINISTER],
        "abilitys": "",
        "arcana": Arcana.ABYSSUS,
        "growth": "parabolic",
        "exp_base_given": 208,
        "catch_rate": 45,
        "evolves": None,
        "base_stats": animadex_base_stats_model(hp=90, atk=92, sp_atk=61, _def=100, sp_def=113, spe=72),
        "move_learning": {
        },
        "assisted_techinques": {
            "001" : techdex["000"],
        }
    },
    
}
'''A dictionary of every single Anima with its information that never changes'''


tfug = effectiveness_chart[TypeA.ESSENTIA][TypeA.UMBRA]

# print(anssanj["move_learning"])