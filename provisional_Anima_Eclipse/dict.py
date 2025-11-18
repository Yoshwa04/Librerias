from typing import Dict
from arcana import Arcana
from type import TypeA, TypeB
from nature import Nature



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
    "exp": "exp_given = (exp_base_given*lvl/participants/5) * ((2*lvl+10)**(5/2)) / ((lvl+ally_lvl+10)**(5/2)) + 1) * combat_type * object_modifier",
    "growth": growth_dict
}
'''A bunch of formulas'''

natures_dict = {
    Nature.BERSERKER:   {"+": "atk", "-": "def"},
    Nature.GLADIADOR:   {"+": "atk", "-": "sp_def"},
    Nature.ASALTANTE:   {"+": "atk", "-": "spe"},
    Nature.BRUTO:       {"+": "atk", "-": "sp_atk"},
    
    Nature.GUARDIA:     {"+": "def", "-": "atk"},
    Nature.MURALLA:     {"+": "def", "-": "sp_atk"},
    Nature.CENTINELA:   {"+": "def", "-": "dp_def"},
    Nature.FORTIFICADO: {"+": "def", "-": "spe"},
    
    Nature.HECHICERO:   {"+": "sp_atk", "-": "atk"},
    Nature.ORACULO:     {"+": "sp_atk", "-": "def"},
    Nature.MISTICO:     {"+": "sp_atk", "-": "sp_def"},
    Nature.ERUDITO:     {"+": "sp_atk", "-": "spe"},
    
    Nature.MONJE:       {"+": "sp_def", "-": "atk"},
    Nature.ILUMINADO:   {"+": "sp_def", "-": "sp_atk"},
    Nature.ADIVINO:     {"+": "sp_def", "-": "def"},
    Nature.ESPIRITUAL:  {"+": "sp_def", "-": "spe"},
    
    Nature.EXPLORADOR:  {"+": "spe", "-": "def"},
    Nature.CAZADOR:     {"+": "spe", "-": "sp_def"},
    Nature.BROMISTA:    {"+": "spe", "-": "atk"},
    Nature.ESPADACHIN:  {"+": "spe", "-": "sp_atk"},
    
    Nature.NEUTRA:      {"+": None, "-": None}
}
'''The dictionary of which stats increase or decrease for each nature'''


# NOMBRE PROVISIONAL
def generate_base_stats(hp: int, atk: int, sp_atk: int, _def: int, sp_def: int, spe: int) -> Dict[str, int]:
    '''This method just returns a dict of the stats given its value'''
    return {
        "hp" : hp,
        "atk" : atk,
        "sp_atk" : sp_atk,
        "def" : _def,
        "sp_def" : sp_def,
        "spe" : spe  
    }
animadex = {
    "000": { #Ejemplo
        "name": "a",
        "types": ["typeA", "typeB"],
        "ability": "ab",
        "arcana": "ar",
        "growth": "g",
        "exp_base_given": 1,
        "catch_rate" : 255,
        "evolves": None,
        "base_stats" : generate_base_stats(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
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
        "base_stats" : generate_base_stats(44, 40, 58, 62, 61, 49),
        "move_learning": {
            
        }     
    },
}
'''A dictionary of every single Anima with its information that never changes'''
